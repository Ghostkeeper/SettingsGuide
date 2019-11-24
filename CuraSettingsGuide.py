#Copyright (C) 2018 Aleksei Sasin
#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import os.path #To find the path of the resources.
import re #To get images from the descriptions.
from PyQt5.QtCore import pyqtSlot, pyqtProperty, pyqtSignal, QObject, QUrl #To expose data to the GUI.
from typing import Dict, List, Optional

from cura.API import CuraAPI #To register the context menu item in the settings list.
from cura.CuraApplication import CuraApplication #To get the setting version to load the correct definition file, and to create QML components.
from UM.Extension import Extension #We're implementing a Cura extension.
from UM.Logger import Logger
from UM.Job import Job  # To load articles as a background task.
from UM.JobQueue import JobQueue  # To load articles as a background task.
from UM.PluginRegistry import PluginRegistry #To find the path of the resources.
from UM.Settings.ContainerRegistry import ContainerRegistry #To register the non-setting entries.
from UM.Settings.ContainerStack import ContainerStack #To get the names of non-setting entries.
from UM.Settings.DefinitionContainer import DefinitionContainer #To register the non-setting entries.

from . import MenuItemHandler #To register the context menu item in the settings list.
from . import QtMarkdownRenderer #To match Mistune's output to Qt's supported HTML subset.
from .Mistune import mistune #To parse the Markdown files.

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

		self.addMenuItem("Settings Guide", self.startWelcomeGuide)
		self._dialog = None #Cached instance of the dialogue window.
		self._container_stack = None #Stack that provides not only the normal settings but also the extra articles added by this guide.

		renderer = QtMarkdownRenderer.QtMarkdownRenderer()
		self._markdown = mistune.Markdown(renderer=renderer) #Renders the Markdown articles into the subset of HTML supported by Qt.

		self.articles = {} #type: Dict[str, List[List[str]]] #All of the articles by key. Key: article ID, value: Lists of items in each article.
		self._selected_article_id = "" #Which article is currently shown for the user. Empty string indicates it's the welcome screen.

		#Add context menu item to the settings list to open the guide for that setting.
		CuraAPI().interface.settings.addContextMenuItem({
			"name": "Settings Guide",
			"icon_name": "help-contents",
			"actions": ["sidebarMenuItemOnClickHandler"],
			"menu_item": MenuItemHandler.MenuItemHandler(self)
		})

		CuraApplication.getInstance().initializationFinished.connect(self.load_all_in_background)

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
		self.load_definitions()  # Ensure that we have a list of articles.
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

	def load_window(self):
		"""
		Do all the things necessary to start using the guide.
		"""
		self.load_definitions()

		if not self._dialog:
			self._dialog = self._createDialog("SettingsGuide.qml")
			if not self._dialog:
				Logger.log("e", "Unable to create settings guide dialogue.")

	def startWelcomeGuide(self) -> None:
		"""
		Opens the guide in the welcome page.
		"""
		self.load_window()
		if not self._dialog:
			return
		self.setSelectedArticleId("") #Display welcome page.
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

	def _createDialog(self, qml_name: str) -> Optional["QObject"]:
		"""
		Creates an instance of the QML item for the dialogue window of the
		guide.
		:param qml_name: The filename of the QML to create.
		:return: The QML instance.
		"""
		Logger.log("d", "Settings Guide: Create dialog from QML [%s]", qml_name)
		plugin_path = PluginRegistry.getInstance().getPluginPath(self.getPluginId())
		if plugin_path is None:
			plugin_path = os.path.dirname(__file__)
		path = os.path.join(plugin_path, "resources", "qml", qml_name)
		dialog = CuraApplication.getInstance().createQmlComponent(path, {"manager": self})
		return dialog

	currentArticleReset = pyqtSignal() #Signal to indicate that the article list should reset its current index.

	def _getArticle(self, article_id) -> List[List[str]]:
		"""
		Gets the rich text of a specified article.

		This function lazily loads an article from a file. If it's never been
		loaded before the article gets parsed and stored. Otherwise it'll get
		taken from the cache.
		:param article_id: The ID of the article to get.
		"""
		if article_id not in self.articles:
			markdown_file = os.path.join(os.path.dirname(__file__), "resources", "articles", article_id + ".md")
			try:
				with open(markdown_file, encoding="utf-8") as f:
					markdown_str = f.read()
			except OSError: #File doesn't exist or is otherwise not readable.
				if self._container_stack and article_id in self._container_stack.getAllKeys():
					markdown_str = "*" + self._container_stack.getProperty(article_id, "description") + "*" #Use the setting description as fallback.
				else:
					markdown_str = "There is no article on this topic."

			images_path = os.path.join(os.path.dirname(__file__), "resources", "articles")
			find_images = re.compile(r"!\[(.*)\]\((.+)\)")
			text_parts = find_images.split(markdown_str)
			image_description = None
			parts = [] #type: List[List[str]] #List of items in the article. Each item starts with a type ID, and then a variable number of data items.
			for index, part in enumerate(text_parts):
				#The parts of the regex split alternate between text, image description and image URL.
				if index % 3 == 0:
					part = part.strip()
					if part or index == 0:
						rich_text = self._markdown(part)
						parts.append(["rich_text", rich_text])
				elif index % 3 == 1:
					image_description = mistune.markdown(part)
				else: #if index % 3 == 2:
					if image_description is not None:
						if parts[-1][0] != "images": #List of images.
							parts.append(["images"])
						image_url = os.path.join(images_path, part)
						parts[-1].append(QUrl.fromLocalFile(image_url).toString() + "|" + image_description)
						image_description = None

			self.articles[article_id] = parts

			#Load the article into the actual setting description as well.
			global_stack = CuraApplication.getInstance().getGlobalContainerStack()
			if global_stack and article_id in global_stack.getAllKeys():
				complete_article = self._markdown(markdown_str)
				definition = global_stack.definition.findDefinitions(key=article_id)[0]
				definition._SettingDefinition__property_values["description"] = complete_article

		return self.articles[article_id]

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
		return os.path.exists(os.path.join(os.path.dirname(__file__), "resources", "articles", filename))

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
		return self._getArticle(self._selected_article_id)