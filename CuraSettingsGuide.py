#Copyright (C) 2018 Aleksei Sasin
#Copyright (C) 2022 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import os  # To find the article files and other resources.
import urllib.parse  # For unquote_plus to create preference keys for forms.
try:
	from PyQt6.QtCore import pyqtSlot, pyqtProperty, pyqtSignal, QObject, QUrl  # To expose data to the GUI and adjust the size of setting tooltips.
except ImportError:  # Older version of Cura.
	from PyQt5.QtCore import pyqtSlot, pyqtProperty, pyqtSignal, QObject, QUrl  # In Cura 4.x, use Qt5 instead of Qt6.
import re  # To get images from the descriptions.
import shutil  # To copy the theme.
import threading  # Screenshot refresh is done on a separate thread.
from typing import Dict, List

from cura.CuraApplication import CuraApplication  # To get the setting version to load the correct definition file, and to create QML components.
from UM.Extension import Extension  # We're implementing a Cura extension.
from UM.Logger import Logger
from UM.Job import Job  # To load articles as a background task.
from UM.JobQueue import JobQueue  # To load articles as a background task.
from UM.PluginRegistry import PluginRegistry  # To find the path of the resources.
from UM.Qt.Bindings.PointingRectangle import PointingRectangle  # To adjust the width of setting tooltips.
from UM.Resources import Resources  # To find the themes in order to adjust them.
from UM.Settings.ContainerRegistry import ContainerRegistry  # To register the non-setting entries.
from UM.Settings.DefinitionContainer import DefinitionContainer  # To register the non-setting entries.
from UM.Version import Version  # To parse Cura's version number.

from . import MenuItemHandler  # To register the context menu item in the settings list.
from . import QtMarkdownRenderer  # To match Mistune's output to Qt's supported HTML subset.
try:
	from . import ScreenshotTool  # To refresh screenshots using the Cura client.
	has_screenshot_tool = True
except ImportError:
	has_screenshot_tool = False
from .Mistune import mistune  # To parse the Markdown files.

class CuraSettingsGuide(Extension, QObject):
	"""
	The main manager and entry point for the Cura Settings Guide.

	This adds a menu item to the extensions menu and to the context menu of
	every article. It creates a dialogue window to display the guide in, and
	makes the menu items open said dialogue window.

	This class is also exposed to the QML code, which can use it to request the
	articles and metadata about the article.
	"""

	def __init__(self, parent=None) -> None:
		"""
		Executed during registration of the plug-in.

		This adds a menu item to the extensions menu and the context menu of the
		settings.
		:param parent: The parent QObject this is located in. Unused by this
		particular object.
		"""
		QObject.__init__(self, parent)
		Extension.__init__(self)

		self.setMenuName("Ѕettings Guide")  # Using Cyrillic Ѕ instead of normal S to prevent MacOS detecting the word "setting" and pulling this menu item out of context.
		self.addMenuItem("Ѕettings Guide", self.startWelcomeGuide)
		self.addMenuItem("Рreferences", lambda: self.startWelcomeGuideAndSelectArticle("preferences"))
		self._dialog = None  # Cached instance of the dialogue window.
		self.definition_container = None  # Setting definitions that provide not only the normal settings but also the extra articles added by this guide.

		self._markdown_per_folder = {}  # For each directory containing Markdown files, create one renderer that correctly dereferences images relatively.

		self.articles = {}  # type: Dict[str, Dict[str, List[List[str]]]]  # All of the articles by key and language. Key: article ID, value: Dict with language as key and lists of items in each article as value.
		self.articles_rich_text = {}  # type: Dict[str, Dict[str, str]]  # For each article and language, the complete Rich Text that should get shown in the tooltip.
		self.articles_source = {}  # type: Dict[str, Dict[str, str]]  # For each article and language, the original Markdown source the article is derived from.
		self.load_definitions()
		self.article_locations = self.find_articles()
		self._selected_article_id = ""  # Which article is currently shown for the user. Empty string indicates it's the welcome screen.
		self.completed_loading = False  # Only after loading is completed can we set the tooltips.

		# Add context menu item to the settings list to open the guide for that setting.
		application = CuraApplication.getInstance()
		application.getCuraAPI().interface.settings.addContextMenuItem({
			"name": "Settings Guide",
			"icon_name": "help-contents",
			"actions": ["sidebarMenuItemOnClickHandler"],
			"menu_item": MenuItemHandler.MenuItemHandler(self)
		})

		preferences = application.getPreferences()
		preferences.addPreference("settings_guide/language", "cura_default")
		preferences.addPreference("settings_guide/show+articles+in+setting+tooltips+%28requires+restart%29", True)
		preferences.addPreference("settings_guide/window+always+in+front", False)
		preferences.addPreference("settings_guide/screenshot_tool", False)

		self.adjust_theme()
		application.initializationFinished.connect(self.load_all_in_background)
		application.initializationFinished.connect(self.widen_tooltips)
		application.globalContainerStackChanged.connect(self.set_tooltips)

	def adjust_theme(self):
		"""
		Makes the tooltips wider, if displaying articles in the tooltips.
		"""
		# Previous versions of the Settings Guide may create a theme, which may become outdated in newer versions.
		# We need to remove it and widen the tooltips in a different way.
		application = CuraApplication.getInstance()
		preferences = application.getPreferences()
		preferences.addPreference("general/theme", application.default_theme)  # May not exist yet at this point.
		current_theme = preferences.getValue("general/theme")
		if current_theme and current_theme.endswith("_settingsguideadjust"):
			preferences.setValue("general/theme", current_theme[:-len("_settingsguideadjust")])
		# Look for Settings Guide adjusted themes in the resources folder.
		theme_path = os.path.dirname(Resources.getStoragePath(Resources.Themes, ""))
		try:
			for theme_folder in os.listdir(theme_path):
				if theme_folder.endswith("_settingsguideadjust"):
					shutil.rmtree(os.path.join(theme_path, theme_folder))
		except EnvironmentError as e:
			# Perhaps no rights? Well, just leave the extra theme in then. Nothing to be done about it.
			Logger.error("Unable to remove Settings Guide deprecated theme: {err}".format(err=str(e)))

	def widen_tooltips(self):
		"""
		Make tooltips wider, so that they are easier to read.

		This really only works in Qt 5.14 and higher, so only Cura 4.9 and up can enjoy the wider tooltips.
		"""
		application = CuraApplication.getInstance()
		if application.getPreferences().getValue("settings_guide/show+articles+in+setting+tooltips+%28requires+restart%29"):
			try:
				main_window = application._qml_engine.rootObjects()[0]
				if main_window is not None:
					tooltips = main_window.findChildren(PointingRectangle)  # There are multiple instances of this (currently 3). It's indistinguishable which is the setting tooltip. Collateral damage!
					for tooltip in tooltips:
						tooltip.setWidth(tooltip.width() * 2.5)
			except IndexError:  # rootObjects() returned an empty list, meaning the main window failed to load.
				pass  # Let's skip widening the tooltips then.

	def load_all_in_background(self):
		"""
		Runs the load_all() function as a background task.
		"""
		class ArticleLoadJob(Job):
			"""
			A background task that loads all articles of the guide.
			"""

			def __init__(self, guide):
				"""
				Creates the background task.
				:param guide: The CuraSettingsGuide object which has the
				function to call.
				"""
				super().__init__()
				self.guide = guide

			def run(self):
				"""
				Runs the background task.

				Cura will call this function from a different thread.
				"""
				self.guide.load_all()
		JobQueue.getInstance().add(ArticleLoadJob(self))

	def load_all(self):
		"""
		Pre-cache all articles in all languages.

		This is meant to run as a background task. This makes sure all setting
		descriptions are loaded so that they can load faster next time the
		article is requested. It also makes sure that the setting description
		is correctly displayed (after a while).
		"""
		for article_id in self.article_locations:
			for language in self.article_locations[article_id]:
				self._getArticle(article_id, language)  # Load articles one by one.
		self.completed_loading = True
		self.set_tooltips()
		Logger.log("i", "Finished loading Settings Guide articles.")

	def load_definitions(self):
		"""
		Load all the setting definitions into a custom definition container.

		This definition container also contains extra entries for the articles
		that are not settings.

		The result is stored in `self.definition_container`.
		"""
		if self.definition_container:
			return  # Already done earlier. Don't re-load.
		with open(os.path.join(os.path.dirname(__file__), "resources", "settings_guide_definitions.def.json")) as f:
			definitions_serialised = f.read()
		self.definition_container = DefinitionContainer("settings_guide_definitions")
		self.definition_container.deserialize(definitions_serialised)
		ContainerRegistry.getInstance().addContainer(self.definition_container)

	def set_tooltips(self):
		"""
		Set the tooltips to the contents of the articles in the current
		language.
		"""
		if not self.completed_loading:
			return  # This got triggered via the global stack changed signal before all articles completed loading. It will trigger again when loading is complete.
		if not CuraApplication.getInstance().getPreferences().getValue("settings_guide/show+articles+in+setting+tooltips+%28requires+restart%29"):
			return  # User doesn't want tooltips changed.
		language = CuraApplication.getInstance().getPreferences().getValue("settings_guide/language")
		global_stack = CuraApplication.getInstance().getGlobalContainerStack()
		if not global_stack:
			return  # Fail.
		for article_id in self.articles_rich_text:
			if article_id in global_stack.getAllKeys():
				definition = global_stack.definition.findDefinitions(key=article_id)[0]
				if language in self.articles_rich_text[article_id]:
					definition._SettingDefinition__property_values["description"] = self.preprocess_tooltips(self.articles_rich_text[article_id][language])
				elif "en_US" in self.articles_rich_text[article_id]:  # Fall back to English. Or don't change it if the article doesn't exist.
					definition._SettingDefinition__property_values["description"] = self.preprocess_tooltips(self.articles_rich_text[article_id]["en_US"])

	def preprocess_tooltips(self, original_text):
		"""
		Preprocess the articles for display in tooltips.

		The tooltips need slightly different formatting. This function transforms text for display in the tooltips.
		:param original_text: Rich text that is being displayed in the main articles.
		:return: Rich text that can be displayed in the tooltips.
		"""
		# Remove all hyperlinks from this text.
		# Hyperlinks don't work when clicked on here (Cura's tooltip display code won't activate weblinks, and it can't open up the Settings Guide to display different articles).
		# However they do break through having a different colour in system-styled tooltips in the setting visibility list.
		remove_links_regex = re.compile(r"(?:<a href=\".*\">|</a>)")
		return re.sub(remove_links_regex, "", original_text)

	def find_articles(self):
		"""
		For each article and language, find where the Markdown file is
		located.
		:return: A nested dictionary mapping article ID to language to file
		path.
		"""
		result = {}
		# Find the English translations first.
		for root, _, files in os.walk(os.path.join(os.path.dirname(__file__), "resources", "articles")):
			for filename in files:
				base_name, extension = os.path.splitext(filename)
				if extension != ".md":
					continue  # Only interested in article files.
				result[base_name] = {"en_US": os.path.join(root, filename)}

		# Find the translated articles in the translations folder.
		for language in os.listdir(os.path.join(os.path.dirname(__file__), "resources", "translations")):
			language_path = os.path.join(os.path.dirname(__file__), "resources", "translations", language)
			if not os.path.isdir(language_path):
				continue  # Not a translation folder.
			for root, _, files in os.walk(language_path):
				for filename in files:
					base_name, extension = os.path.splitext(filename)
					if extension != ".md":
						continue  # Only interested in article files.
					if base_name not in result:
						continue  # Translation for an article that doesn't exist in English?
					result[base_name][language] = os.path.join(root, filename)

		return result

	def load_window(self):
		"""
		Create the GUI window for the guide.

		The window's QML element is stored in a field. There can only be one
		instance at a time.
		"""
		self.load_definitions()

		if self._dialog:  # Dialogue already open.
			self._dialog.requestActivate()  # Bring focus to dialogue.
			return
		Logger.log("d", "Creating Settings Guide window.")
		plugin_path = PluginRegistry.getInstance().getPluginPath(self.getPluginId())
		if plugin_path is None:
			plugin_path = os.path.dirname(__file__)
		application = CuraApplication.getInstance()
		version = Version(application.getVersion())
		if application.getVersion() != "source" and version.getMajor() <= 4:
			path = os.path.join(plugin_path, "resources", "qml_cura4", "SettingsGuide.qml")
		else:  # In Cura 5+ the QML interface changed significantly, and the settings layout too. We use a different set of QML files to use the new interface and to mimic the new look.
			path = os.path.join(plugin_path, "resources", "qml", "SettingsGuide.qml")
		self._dialog = application.createQmlComponent(path, {"manager": self})
		if not self._dialog:
			Logger.log("e", "Unable to create settings guide dialogue.")

	def startWelcomeGuide(self) -> None:
		"""
		Opens the guide in the welcome page.
		"""
		self.load_window()
		if not self._dialog:
			return
		self.setSelectedArticleId("")  # Display welcome page.
		self._dialog.show()

	def startWelcomeGuideAndSelectArticle(self, article_key: str) -> None:
		"""
		Opens the guide and immediately selects a certain article.
		:param article_key: The key of the article to show the guide of.
		"""
		self.load_window()
		if not self._dialog:
			return
		self.currentArticleReset.emit()
		self.setSelectedArticleId(article_key)
		self._dialog.show()

	currentArticleReset = pyqtSignal() #Signal to indicate that the article list should reset its current index.

	def _getArticle(self, article_id, language="en_US") -> List[List[str]]:
		"""
		Gets the rich text of a specified article.

		This function lazily loads an article from a file. If it's never been
		loaded before the article gets parsed and stored. Otherwise it'll get
		taken from the cache.
		:param article_id: The ID of the article to get.
		:param language: The language to get the article in.
		:return: A list of article "parts". Each article part is a list, where
		the first element indicates the type of part and the rest contains the
		content. Possible types of parts are "rich_text", "images" or
		"checkbox".
		"""
		if article_id in self.articles and language in self.articles[article_id]:
			return self.articles[article_id][language]

		images_path = os.path.join(os.path.dirname(__file__), "resources", "articles", "images")
		try:
			if language not in self.article_locations[article_id]:
				language = "en_US"  # Fall back to English if the preferred language is not available.
			markdown_file = self.article_locations[article_id][language]
			with open(markdown_file, encoding="utf-8") as f:
				markdown_str = f.read()
			images_path = os.path.dirname(markdown_file)
		except (OSError, KeyError):  # File doesn't exist or is otherwise not readable.
			if self.definition_container and article_id in self.definition_container.getAllKeys():
				markdown_str = self.definition_container.getProperty(article_id, "label") + "\n====\n"
				markdown_str += "*" + self.definition_container.getProperty(article_id, "description") + "*"  # Use the setting description as fallback.
			else:
				markdown_str = "There is no article on this topic."

		# Store this unparsed for later.
		if language not in self.articles_source:
			self.articles_source[language] = {}
		self.articles_source[language][article_id] = markdown_str

		if images_path not in self._markdown_per_folder:
			renderer = QtMarkdownRenderer.QtMarkdownRenderer(images_path)
			self._markdown_per_folder[images_path] = mistune.Markdown(renderer=renderer)  # Renders the Markdown articles into the subset of HTML supported by Qt.

		# Pre-process so that comments and conditionals don't influence the business.
		markdown_str = QtMarkdownRenderer.QtMarkdownRenderer.preprocess_conditionals(markdown_str)
		markdown_str = QtMarkdownRenderer.QtMarkdownRenderer.preprocess_comments(markdown_str)

		find_images = re.compile(r"!\[(.*)\]\(([^\)]+)\)")
		find_checkboxes = re.compile(r"\[ \]\s*([^\n]+)")
		image_description = None
		parts = []  # type: List[List[str]]  # List of items in the article. Each item starts with a type ID, and then a variable number of data items.
		for index, part_between_images in enumerate(find_images.split(markdown_str)):
			# The parts of the regex split alternate between text, image description and image URL.
			if index % 3 == 0:
				part_between_images = part_between_images.strip()
				if part_between_images or index == 0:
					parts_between_checkboxes = find_checkboxes.split(part_between_images)
					for index2, part_between_checkboxes in enumerate(parts_between_checkboxes):
						part_between_checkboxes = part_between_checkboxes.strip()
						# The parts of the regex split alternate between text and checkbox description.
						if index2 % 2 == 0:
							if part_between_checkboxes:
								rich_text = self._markdown_per_folder[images_path](part_between_checkboxes)
								parts.append(["rich_text", rich_text])
						else:  # if index2 == 1:
							preference_key = "settings_guide/" + urllib.parse.quote_plus(part_between_checkboxes).lower()
							parts.append(["checkbox", preference_key, part_between_checkboxes])
			elif index % 3 == 1:
				image_description = mistune.markdown(part_between_images)
			else:  # if index % 3 == 2:
				if image_description is not None:
					if parts[-1][0] != "images":  # List of images.
						parts.append(["images"])
					image_url = os.path.join(images_path, part_between_images)
					parts[-1].append(QUrl.fromLocalFile(image_url).toString() + "|" + image_description)
					image_description = None

		if article_id not in self.articles:
			self.articles[article_id] = {}
		self.articles[article_id][language] = parts
		if article_id not in self.articles_rich_text:
			self.articles_rich_text[article_id] = {}
		self.articles_rich_text[article_id][language] = self._markdown_per_folder[images_path](markdown_str)

		return self.articles[article_id][language]

	@pyqtSlot(str, result=bool)
	def isArticleFile(self, filename: str) -> bool:
		"""
		Tests whether a file name is the file name of an existing article.

		This test is used to determine if a link should refer to a different
		article or to the internet.
		:param filename: The file name to test for.
		:return: True if the file name is the file name of an existing article,
		or False if it isn't.
		"""
		return os.path.exists(filename)

	@pyqtProperty(str, constant=True)
	def pluginVersion(self) -> str:
		"""
		Get the version number of this plug-in.

		This plug-in version is a semantic version number in three parts
		("1.2.3").
		:return: The version number of this plug-in.
		"""
		return self.getVersion()

	selectedArticleChanged = pyqtSignal()

	@pyqtSlot(str)
	def setSelectedArticleId(self, article_key: str) -> None:
		"""
		Show a certain article in the dialogue.
		:param article_key: The key of the article to display.
		"""
		if self._selected_article_id != article_key:
			self._selected_article_id = article_key
			self.selectedArticleChanged.emit()

	@pyqtProperty(str, fset=setSelectedArticleId, notify=selectedArticleChanged)
	def selectedArticleId(self) -> str:
		"""
		Returns the key of the article that is currently selected.

		If no article has been selected (the logo is being shown), an empty
		string is returned.
		:return: The key of the article that is currently selected.
		"""
		return self._selected_article_id

	@pyqtProperty("QVariantList", notify=selectedArticleChanged)
	def selectedArticle(self) -> List[List[str]]:
		"""
		Returns the currently selected article.

		This article data is a rich text document, properly formatted from the
		Markdown files in the article directory. Each article is a list of
		items, some of which are text and some of which are image lists.
		:return: The the currently selected article.
		"""
		preferences = CuraApplication.getInstance().getPreferences()
		language = preferences.getValue("settings_guide/language")
		if language == "cura_default":
			language = preferences.getValue("general/language")
		return self._getArticle(self._selected_article_id, language)

	@pyqtSlot(str, result="QVariantList")
	def language_list(self, article_key: str) -> List[str]:
		"""
		Gets a list of available languages for a certain article.
		:param article_key: The article ID to get the languages for.
		:return: A list of language codes (e.g. [nl_NL, en_US]).
		"""
		if article_key not in self.article_locations:
			return []  # We have no articles about this setting at all.
		return list(self.article_locations[article_key].keys())

	@pyqtSlot(str)
	def set_language(self, language_code: str) -> None:
		"""
		Changes the viewing language.
		:param language_code: The new language code.
		"""
		preferences = CuraApplication.getInstance().getPreferences()
		preferences.setValue("settings_guide/language", language_code)
		if preferences.getValue("settings_guide/show+articles+in+setting+tooltips+%28requires+restart%29"):
			self.set_tooltips()
		self.selectedArticleChanged.emit()

	@pyqtSlot()
	def refresh_screenshots(self) -> None:
		"""
		Refresh the screenshots on the current article.

		This starts the process outlined in the ScreenshotTool class.
		"""
		if not has_screenshot_tool:
			Logger.error("The screenshot tool is not installed in this version of the Settings Guide. Please use the version from the source repository.")
			return
		if self.selectedArticleId:  # Refresh a particular article.
			preferences = CuraApplication.getInstance().getPreferences()
			language = preferences.getValue("settings_guide/language")
			if language == "cura_default":
				language = preferences.getValue("general/language")
			refresh_job = threading.Thread(target=ScreenshotTool.refresh_screenshots, kwargs={"article_text": self.articles_source[language][self.selectedArticleId], "refreshed_set": set()})
			refresh_job.start()
		else:  # Refresh everything.
			refreshed_set = set()  # Don't refresh the same image multiple times. Share the same set among all calls.
			def refresh_everything():
				Logger.info("Refreshing ALL screenshots.")
				for article_per_language in self.articles_source.values():
					for article in article_per_language.values():
						ScreenshotTool.refresh_screenshots(article_text=article, refreshed_set=refreshed_set)
			refresh_job = threading.Thread(target=refresh_everything)
			refresh_job.start()