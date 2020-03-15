#Copyright (C) 2018 Aleksei Sasin
#Copyright (C) 2020 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import json  # To modify the theme file.
import os  # To find the article files and other resources.
import urllib.parse  # For unquote_plus to create preference keys for forms.
from PyQt5.QtCore import pyqtSlot, pyqtProperty, pyqtSignal, QObject, QUrl  # To expose data to the GUI.
import re  # To get images from the descriptions.
import shutil  # To copy the theme.
from typing import Dict, List, Optional

from cura.CuraApplication import CuraApplication  # To get the setting version to load the correct definition file, and to create QML components.
from UM.Extension import Extension  # We're implementing a Cura extension.
from UM.Logger import Logger
from UM.Job import Job  # To load articles as a background task.
from UM.JobQueue import JobQueue  # To load articles as a background task.
from UM.PluginRegistry import PluginRegistry  # To find the path of the resources.
from UM.Resources import Resources  # To find the themes in order to adjust them.
from UM.Settings.ContainerRegistry import ContainerRegistry  # To register the non-setting entries.
from UM.Settings.ContainerStack import ContainerStack  # To get the names of non-setting entries.
from UM.Settings.DefinitionContainer import DefinitionContainer  # To register the non-setting entries.

from . import MenuItemHandler  # To register the context menu item in the settings list.
from . import QtMarkdownRenderer  # To match Mistune's output to Qt's supported HTML subset.
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
		self._dialog = None  # Cached instance of the dialogue window.
		self._container_stack = None  # Stack that provides not only the normal settings but also the extra articles added by this guide.

		self._markdown_per_folder = {}  # For each directory containing Markdown files, create one renderer that correctly dereferences images relatively.

		self.articles = {}  # type: Dict[str, Dict[str, List[List[str]]]]  # All of the articles by key and language. Key: article ID, value: Dict with language as key and lists of items in each article as value.
		self.load_definitions()
		self.article_locations = self.find_articles()
		self._selected_article_id = ""  # Which article is currently shown for the user. Empty string indicates it's the welcome screen.

		# Add context menu item to the settings list to open the guide for that setting.
		application = CuraApplication.getInstance()
		self._selected_language = application.getPreferences().getValue("general/language")
		application.getCuraAPI().interface.settings.addContextMenuItem({
			"name": "Settings Guide",
			"icon_name": "help-contents",
			"actions": ["sidebarMenuItemOnClickHandler"],
			"menu_item": MenuItemHandler.MenuItemHandler(self)
		})

		application.getPreferences().addPreference("settings_guide/show+articles+in+setting+tooltips+%28requires+restart%29", False)

		self.adjust_theme()
		application.initializationFinished.connect(self.load_all_in_background)

	def adjust_theme(self):
		"""
		Makes the tooltips wider, if displaying articles in the tooltips.
		"""
		application = CuraApplication.getInstance()
		preferences = application.getPreferences()
		if preferences.getValue("settings_guide/show+articles+in+setting+tooltips+%28requires+restart%29"):
			preferences.addPreference("general/theme", application.default_theme)
			theme_name = preferences.getValue("general/theme")
			if theme_name.endswith("_settingsguideadjust"):
				return  # Already adjusted.
			theme_path = Resources.getPath(Resources.Themes, theme_name)

			# Create a new theme where we can adjust the tooltip.
			new_theme_name = theme_name + "_settingsguideadjust"
			new_theme_path = Resources.getStoragePath(Resources.Themes, new_theme_name)
			try:
				shutil.copytree(theme_path, new_theme_path)
			except OSError:  # Already exists. Happens when the user manually adjusted the theme back in the preferences screen.
				try:
					os.removedirs(new_theme_path)
					shutil.copytree(theme_path, new_theme_path)
				except OSError:
					pass  # Perhaps no rights?

			# Adjust the tooltip width.
			with open(os.path.join(theme_path, "theme.json")) as f:
				adjusted_theme = json.load(f)
			if "sizes" not in adjusted_theme:
				adjusted_theme["sizes"] = {}
			adjusted_theme["sizes"]["tooltip"] = [50.0, 10.0]
			with open(os.path.join(new_theme_path, "theme.json"), "w") as f:
				json.dump(adjusted_theme, f)

			# Enable the new theme.
			preferences.setValue("general/theme", new_theme_name)
			application.default_theme = new_theme_name

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
		Pre-cache all articles.

		This is meant to run as a background task. This makes sure all setting
		descriptions are loaded so that they can load faster next time the
		article is requested. It also makes sure that the setting description
		is correctly displayed (after a while).
		"""
		for article_id in self._container_stack.getAllKeys():
			self._getArticle(article_id)  # Load articles one by one.
		Logger.log("i", "Finished loading Settings Guide articles.")

	def load_definitions(self):
		"""
		Load all the setting definitions into a custom container stack.

		This container stack also contains extra entries for the articles that
		are not settings.

		The result is stored in self._container_stack.
		"""
		if self._container_stack:
			return  # Already done earlier. Don't re-load.
		with open(os.path.join(os.path.dirname(__file__), "resources", "settings_guide_definitions.def.json")) as f:
			definitions_serialised = f.read()
		definition_container = DefinitionContainer("settings_guide_definitions")
		definition_container.deserialize(definitions_serialised)
		ContainerRegistry.getInstance().addContainer(definition_container)
		self._container_stack = ContainerStack("settings_guide_stack")
		self._container_stack.addContainer(definition_container)
		ContainerRegistry.getInstance().addContainer(self._container_stack)

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

		if self._dialog:
			return  # Dialogue already open.
		Logger.log("d", "Creating Settings Guide window.")
		plugin_path = PluginRegistry.getInstance().getPluginPath(self.getPluginId())
		if plugin_path is None:
			plugin_path = os.path.dirname(__file__)
		path = os.path.join(plugin_path, "resources", "qml", "SettingsGuide.qml")
		self._dialog = CuraApplication.getInstance().createQmlComponent(path, {"manager": self})
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
			if self._container_stack and article_id in self._container_stack.getAllKeys():
				markdown_str = "*" + self._container_stack.getProperty(article_id, "description") + "*"  # Use the setting description as fallback.
			else:
				markdown_str = "There is no article on this topic."

		if images_path not in self._markdown_per_folder:
			renderer = QtMarkdownRenderer.QtMarkdownRenderer(images_path)
			self._markdown_per_folder[images_path] = mistune.Markdown(renderer=renderer)  # Renders the Markdown articles into the subset of HTML supported by Qt.

		preferences = CuraApplication.getInstance().getPreferences()
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

		if preferences.getValue("settings_guide/show+articles+in+setting+tooltips+%28requires+restart%29"):
			# Load the article into the actual setting description as well.
			global_stack = CuraApplication.getInstance().getGlobalContainerStack()
			if global_stack and article_id in global_stack.getAllKeys():
				complete_article = self._markdown_per_folder[images_path](markdown_str)
				definition = global_stack.definition.findDefinitions(key=article_id)[0]
				definition._SettingDefinition__property_values["description"] = complete_article

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

	@pyqtProperty(QObject, constant=True)
	def containerStack(self) -> Optional[ContainerStack]:
		"""
		The specialised container stack containing setting definitions for all
		of the articles in the guide.
		:return: A container stack with extra definitions for all articles in
		the guide.
		"""
		return self._container_stack

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
		return self._getArticle(self._selected_article_id, self._selected_language)

	@pyqtSlot(str, result="QVariantList")
	def language_list(self, article_key: str) -> List[str]:
		"""
		Gets a list of available languages for a certain article.
		:param article_key: The article ID to get the languages for.
		:return: A list of language codes (e.g. [nl_NL, en_US]).
		"""
		return list(self.articles[article_key].keys())