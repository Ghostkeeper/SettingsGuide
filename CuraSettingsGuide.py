#Copyright (C) 2018 Aleksei Sasin
#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import os
import re #To get images from the descriptions.
from PyQt5.QtCore import pyqtSlot, pyqtProperty, pyqtSignal, QObject, QUrl
from typing import Dict, List, Optional

from cura.API import CuraAPI
from cura.CuraApplication import CuraApplication #To get the setting version to load the correct definition file.
from UM.Application import Application
from UM.Extension import Extension
from UM.Logger import Logger
from UM.PluginRegistry import PluginRegistry
from UM.i18n import i18nCatalog
from UM.Settings.ContainerRegistry import ContainerRegistry #To register the non-setting entries.
from UM.Settings.ContainerStack import ContainerStack #To get the names of non-setting entries.
from UM.Settings.DefinitionContainer import DefinitionContainer #To register the non-setting entries.

from . import MenuItemHandler
from .Mistune import mistune #To parse the Markdown files.

i18n_catalog = i18nCatalog("cura")

class CuraSettingsGuide(Extension, QObject):
	"""
	The main manager and entry point for the Cura Settings Guide.

	This adds a menu item to the extensions menu and to the context menu of
	every setting. It creates a dialogue window to display the guide in, and
	makes the menu items open said dialogue window.

	This class is also exposed to the QML code, which can use it to request the
	descriptions and metadata about the settings.
	"""

	def __init__(self, parent=None) -> None:
		"""
		Executed during registration of the plug-in.

		This adds a menu item to the extensions menu and the context menu of the
		settings. It also loads the descriptions and setting metadata from the
		resources.
		:param parent: The parent QObject this is located in. Unused by this
		particular object.
		"""
		QObject.__init__(self, parent)
		Extension.__init__(self)

		self.addMenuItem("Settings Guide", self.startWelcomeGuide)
		self._dialog = None #Cached instance of the dialogue window.
		self._container_stack = None #Stack that provides not only the normal settings but also the extra pages added by this guide.

		self.descriptions = {} #type: Dict[str, List[List[str, str]]] #The descriptions for each setting. Key: setting ID, value: Lists of items in each description.
		self._selected_setting_id = "" #Which setting is currently shown for the user. Empty string indicates it's the welcome screen.

		self._loadDescriptions()

		self.initializeHelpSidebarHelpButton()

	def initializeHelpSidebarHelpButton(self) -> None:
		"""
		Add menu item to the context menus of settings that opens the guide of
		that setting.
		"""
		menu_actions = ["sidebarMenuItemOnClickHandler"]

		data = {
			"name": "Settings Guide",
			"icon_name": "help-contents",
			"actions": menu_actions,
			"menu_item": MenuItemHandler.MenuItemHandler(self)
		}
		CuraAPI().interface.settings.addContextMenuItem(data)

	def load_window(self):
		"""
		Do all the things necessary to start using the guide.
		"""
		#Load a special definition container that also contains extra entries for the guide entries that are not settings.
		settings_guide_filename = "settings_guide_definitions_{n}.def.json".format(n=DefinitionContainer.Version * 1000000 + CuraApplication.SettingVersion)
		with open(os.path.join(os.path.dirname(__file__), "resources", settings_guide_filename)) as f:
			definitions_serialised = f.read()
		definition_container = DefinitionContainer("settings_guide_definitions")
		definition_container.deserialize(definitions_serialised)
		ContainerRegistry.getInstance().addContainer(definition_container)
		self._container_stack = ContainerStack("settings_guide_stack")
		self._container_stack.addContainer(definition_container)
		ContainerRegistry.getInstance().addContainer(self._container_stack)

		if not self._dialog:
			self._dialog = self._createDialog("SettingsGuide.qml")
			if not self._dialog:
				Logger.log("e", "Unable to create settings guide dialogue.")

	def startWelcomeGuide(self) -> None:
		"""
		Opens the guide in the welcome page.
		"""
		self.load_window()
		self.setSelectedSettingId("") #Display welcome page.
		self._dialog.show()

	def startWelcomeGuideAndSelectSetting(self, setting_key: str) -> None:
		"""
		Opens the guide and immediately selects a certain setting.
		:param setting_key: The key of the setting to show the guide of.
		"""
		self.load_window()
		self.setSelectedSettingId(setting_key)
		self._dialog.show()

	def _createDialog(self, qml_name: str) -> Optional["QObject"]:
		"""
		Creates an instance of the QML item for the dialogue window of the
		guide.
		:param qml_name: The filename of the QML to create.
		:return: The QML instance.
		"""
		Logger.log("d", "Settings Guide: Create dialog from QML [%s]", qml_name)
		path = os.path.join(PluginRegistry.getInstance().getPluginPath(self.getPluginId()), "resources", "qml", qml_name)
		dialog = Application.getInstance().createQmlComponent(path, {"manager": self})
		return dialog

	def _loadDescriptions(self) -> None:
		"""
		Load all the descriptions for all settings.
		"""
		find_images = re.compile(r"!\[(.*)\]\((.+)\)")
		descriptions_path = os.path.join(os.path.dirname(__file__), "resources", "descriptions")
		images_path = os.path.join(os.path.dirname(__file__), "resources", "images")
		for file_name in os.listdir(descriptions_path):
			file_path = os.path.join(descriptions_path, file_name)
			setting_id, extension = os.path.splitext(file_name)
			if extension != ".md":
				continue
			with open(file_path, encoding="utf-8") as f:
				markdown_str = f.read()

			text_parts = find_images.split(markdown_str)
			image_description = None
			parts = [] #type: List[List[str]] #List of items in the description. Each item starts with a type ID, and then a variable number of data items.
			for index, part in enumerate(text_parts):
				#The parts of the regex split alternate between text, image description and image URL.
				if index % 3 == 0:
					part = part.strip()
					if part or index == 0:
						rich_text = mistune.markdown(part)
						parts.append(["rich_text", rich_text])
				elif index % 3 == 1:
					image_description = mistune.markdown(part)
				else: #if index % 3 == 2:
					if image_description is not None:
						if parts[-1][0] != "images": #List of images
							parts.append(["images"])
						image_url = os.path.join(images_path, part)
						parts[-1].append(QUrl.fromLocalFile(image_url).toString() + "|" + image_description)
						image_description = None
			self.descriptions[setting_id] = parts

	@pyqtProperty(QObject, constant=True)
	def containerStack(self) -> Optional[ContainerStack]:
		return self._container_stack

	@pyqtProperty(str, constant=True)
	def pluginVersion(self) -> str:
		"""
		Get the version number of this plug-in.

		This setting version is a semantic version number in three parts
		("1.2.3").
		:return: The version number of this plug-in.
		"""
		return self._version

	settingItemChanged = pyqtSignal()

	@pyqtSlot(str)
	def setSelectedSettingId(self, setting_key: str) -> None:
		"""
		Show the description of a certain setting in the guide dialogue.
		:param setting_key: The key of the setting to display.
		"""
		self._selected_setting_id = setting_key
		self.settingItemChanged.emit()

	@pyqtProperty(str, fset=setSelectedSettingId, notify=settingItemChanged)
	def selectedSettingId(self) -> str:
		"""
		Returns the setting key of the setting that is currently selected.

		If no setting has been selected, an empty string is returned.
		:return: The setting key of the setting that is currently selected.
		"""
		return self._selected_setting_id

	@pyqtProperty("QVariantList", notify=settingItemChanged)
	def selectedSettingDescription(self) -> List[List[str]]:
		"""
		Returns the description of the currently selected setting.

		This setting data is a rich text document, properly formatted from the
		Markdown files in the setting description files.
		:return: The description of the currently selected setting.
		"""
		return self.descriptions.get(self._selected_setting_id, [["rich_text", "There is no description for this setting."]])