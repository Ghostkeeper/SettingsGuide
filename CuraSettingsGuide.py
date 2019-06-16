#Copyright (C) 2018 Aleksei Sasin
#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import json
import os
from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal
import re
from typing import Dict, List, Optional, Union

from cura.API import CuraAPI
from UM.Extension import Extension
from UM.Application import Application
from UM.Logger import Logger
from UM.PluginRegistry import PluginRegistry
from UM.i18n import i18nCatalog

from . import MenuItemHandler

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

		self._settings_data = {} #type: Dict[str, Dict[str, Union[List[str], Dict[str, str]]]] #The data loaded from the JSON files containing descriptions about settings.
		self._selected_setting_id = "" #Which setting is currently shown for the user. Empty string indicates it's the welcome screen.

		self._loadDescriptionAndImages()

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

	def startWelcomeGuide(self) -> None:
		"""
		Opens the guide in the welcome page.
		"""
		if not self._dialog:
			self._dialog = self._createDialog("SettingsGuide.qml")
			if not self._dialog:
				Logger.log("e", "Unable to create settings guide dialogue.")
				return

		self.setSelectedSettingId("") #Display welcome page.
		self._dialog.show()


	def startWelcomeGuideAndSelectSetting(self, setting_key: str) -> None:
		"""
		Opens the guide and immediately selects a certain setting.
		:param setting_key: The key of the setting to show the guide of.
		"""
		if not self._dialog:
			self._dialog = self._createDialog("SettingsGuide.qml")
			if not self._dialog:
				Logger.log("e", "Unable to create settings guide dialogue.")
				return

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

	def _loadDescriptionAndImages(self) -> None:
		"""
		Load all descriptions and image paths.
		"""
		plugin_path = os.path.dirname(__file__)
		images_path = os.path.join(plugin_path, "resources", "images")
		descriptions_path = os.path.join(plugin_path, "resources", "descriptions")

		#Load images paths and add its IDs to the dictionary.
		self._populateImagesPaths(images_path)

		#Load settings descriptions.
		self._populateSettingsDetails(descriptions_path, images_path)

	def _populateImagesPaths(self, images_path: str) -> None:
		"""
		Load all image paths from a directory, and convert them to QURLs.
		:param images_path: Directory to load all images from.
		"""
		images_files = os.listdir(images_path)
		images_files = sorted(images_files)

		custom_path = "file:///" + images_path

		for file in images_files:
			file_name_parts = file.split("_")
			file_id = file_name_parts[:-1]
			file_id = "_".join(file_id)
			if file_id not in self._settings_data.keys():
				self._settings_data[file_id] = {}
				self._settings_data[file_id]["images"] = []

			image_path = os.path.join(custom_path, file)
			self._settings_data[file_id]["images"].append(image_path)

	def _populateSettingsDetails(self, descriptions_path: str, images_path: str) -> None:
		"""
		Load all setting descriptions and store them in memory.
		:param descriptions_path: The path of the directory to find the setting
		descriptions.
		:param images_path: The path of the directory to find the images.
		"""
		description_files = os.listdir(descriptions_path)
		for file in description_files:
			file_path = os.path.join(descriptions_path, file)

			file_name_parts = os.path.splitext(file)
			file_base_name = file_name_parts[0]  # base name which is also the setting id
			file_extension = file_name_parts[-1]

			if not file_extension == ".json":
				continue

			try:
				with open(file_path, "r", encoding="utf-8") as f:
					json_data = json.load(f)
					general = json_data.get("general", {})

				file_id = file_base_name
				
				#The key is not yet added, no images for this setting.
				if file_id not in self._settings_data.keys():
					self._settings_data[file_id] = {}
					self._settings_data[file_id]["details"] = json_data

				#Images already added to the list.
				if "details" not in self._settings_data[file_id]:
					self._settings_data[file_id]["details"] = json_data

				#Overwrite images.
				if "images" in general:
					custom_path = "file:///" + images_path
					self._settings_data[file_id]["images"] = []
					sorted_images = sorted(general["images"].items())
					for key, image_name in sorted_images:
						image_path = os.path.join(custom_path, image_name)
						self._settings_data[file_id]["images"].append(image_path)

			except Exception:
				Logger.logException("w", "Error while reading file: %s" % file)
				continue

	settingItemChanged = pyqtSignal()

	@pyqtProperty(str, constant=True)
	def pluginVersion(self) -> str:
		"""
		Get the version number of this plug-in.

		This setting version is a semantic version number in three parts
		("1.2.3").
		:return: The version number of this plug-in.
		"""
		return self._version

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

	@pyqtProperty("QVariantMap", notify=settingItemChanged)
	def selectedSettingData(self) -> Dict[str, Dict[str, Union[List[str], Dict[str, str]]]]:
		"""
		Returns the setting data of the currently selected setting.

		This setting data is a dictionary with the data to show in the guide. It
		is a dictionary containing the following fields:
		* general/id: The ID of the currently selected setting.
		* general/template: The template file to display for this setting. If
		  this is missing, the general template is assumed.
		* general/images: A list of images to display for this setting.
		* data/description: An extensive description of the current setting.
		* data/img_description: An underscript under the images.
		* data/hints: Hints on how to use the setting better.
		* data/notes: Extra points of attention to beware of when using the
		  setting.
		:return: The setting data of the currently selected setting.
		"""
		return self._settings_data.get(self._selected_setting_id, {
			"details": {
				"general": {
					"id": self._selected_setting_id,
					"template": "EmptyTemplate.qml"
				}
			}
		})

	replacement_patterns = {
		re.compile(r"^-\s+(.*)"): "<li>\\1</li>\n",
	}

	@pyqtSlot(str, result=str)
	def parseStylingList(self, check_text: str) -> str:
		"""
		Transform the mark-up in the setting description to the HTML subset that
		Qt supports.
		:param check_text: The original text.
		:return: A transformed text that Qt can display.
		"""
		contents = ""
		block_open = ""

		for line in check_text.split("\n"):
			if not block_open:
				if line.startswith("-"):
					block_open = "ul"
					contents += "<{}>".format(block_open)

			if line == "" and block_open:
				contents += "</{}>\n".format(block_open)

			for search, replace in self.replacement_patterns.items():
				line = search.sub(replace, line)

			contents += line

		if block_open:
			contents += "</{}>\n".format(block_open)
		else:
			contents = check_text

		return contents