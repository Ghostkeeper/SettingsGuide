#Copyright (C) 2018 Aleksei Sasin
#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import os
from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal
from typing import Dict, Optional

from cura.API import CuraAPI
from UM.Extension import Extension
from UM.Application import Application
from UM.Logger import Logger
from UM.PluginRegistry import PluginRegistry
from UM.i18n import i18nCatalog

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

		self.descriptions = {} #type: Dict[str, str] #The descriptions for each setting. Key: setting ID, value: QML rich text being displayed for that setting.
		self._settings_data = {} #TEMP! Just to not crash.
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

	def _loadDescriptions(self) -> None:
		"""
		Load all the descriptions for all settings.
		"""
		descriptions_path = os.path.join(os.path.dirname(__file__), "resources", "descriptions")
		for file_name in os.listdir(descriptions_path):
			file_path = os.path.join(descriptions_path, file_name)
			setting_id, extension = os.path.splitext(file_name)
			if extension != ".md":
				continue
			with open(file_path, encoding="utf-8") as f:
				markdown_str = f.read()
			rich_text = mistune.markdown(markdown_str)
			self.descriptions[setting_id] = rich_text
			Logger.log("d", "----------------------loaded description for {setting_id}: {rich_text}".format(setting_id=setting_id, rich_text=rich_text))

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

	@pyqtProperty(str, notify=settingItemChanged)
	def selectedSettingDescription(self) -> str:
		"""
		Returns the description of the currently selected setting.

		This setting data is a rich text document, properly formatted from the
		Markdown files in the setting description files.
		:return: The description of the currently selected setting.
		"""
		return self.descriptions.get(self._selected_setting_id, "There is no description for this setting.")