#Copyright (C) 2018 Aleksei Sasin
#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import base64
import json
import os
import platform
import re
from typing import Dict, Optional

from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal
from PyQt5.QtQml import qmlRegisterType, qmlRegisterSingletonType

from UM.Extension import Extension
from UM.Application import Application
from UM.Logger import Logger
from UM.PluginRegistry import PluginRegistry
from UM.i18n import i18nCatalog

from cura.API import CuraAPI

from . import MenuItemHandler
from . import SettingsModel
from . import GuideTheme

i18n_catalog = i18nCatalog("cura")


## The class is entry point for the Cura Settings Guide, it sets all required resources and has manager role.
class CuraSettingsGuide(Extension, QObject):

    def __init__(self, parent = None) -> None:
        QObject.__init__(self, parent)
        Extension.__init__(self)

        self.addMenuItem("Settings Guide", self.startWelcomeGuide)

        self._dialog = None
        self._settings_data = {}  # type: Dict[str, dict]
        self._selected_setting_data = {}  #
        self._os_platform = platform.system()  # type: str

        plugin_path = os.path.dirname(__file__)
        self._images_path = os.path.join(plugin_path, os.path.join("resources", "images"))
        self._descriptions_path = os.path.join(plugin_path, os.path.join("resources", "i18n", "en_US"))

        qmlRegisterType(SettingsModel.SettingsModel, "CuraSettingsGuide", 1, 0, "SettingsModel")
        qmlRegisterSingletonType(GuideTheme.GuideTheme, "GuideTheme", 1, 0, "Theme", GuideTheme.createTheme)

        self._loadDescriptionAndImages()

        self.initializeHelpSidebarHelpButton()

    def initializeHelpSidebarHelpButton(self) -> None:
        menu_actions = ["sidebarMenuItemOnClickHander"]

        data = {
            "name": "Setting Guide",
            "icon_name": "help-contents",
            "actions": menu_actions,
            "menu_item": MenuItemHandler.MenuItemHandler(self)
        }
        api = CuraAPI()
        api.interface.settings.addContextMenuItem(data)

    def startWelcomeGuide(self) -> None:
        if not self._dialog:
            self._dialog = self._createDialog("SettingsGuide.qml")

        self._selected_setting_data = {}  # Display welcome page
        self.settingItemChanged.emit()
        self._dialog.show()


    def startWelcomeGuideAndSelectSetting(self, setting_key: str) -> None:
        if not self._dialog:
            self._dialog = self._createDialog("SettingsGuide.qml")

        self._dialog.show()
        self.setSelectedSetting(setting_key)

    def _createDialog(self, qml_name: str) -> Optional["QObject"]:
        Logger.log("d", "Settings Guide: Create dialog from QML [%s]", qml_name)
        path = os.path.join(PluginRegistry.getInstance().getPluginPath(self.getPluginId()), "resources", "qml", qml_name)
        dialog = Application.getInstance().createQmlComponent(path, {"CuraSettingsGuide": self})
        return dialog

    def _loadDescriptionAndImages(self) -> None:
        # Load images paths and add it's ids to the dictionary
        self._populateImagesPaths(self._images_path)

        # Load settings descriptions
        self._populateSettingsDetails(self._descriptions_path, self._images_path)

    def _populateImagesPaths(self, images_path: str) -> None:
        # Load images paths
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
        description_files = os.listdir(descriptions_path)
        for file in description_files:
            file_path = os.path.join(descriptions_path, file)

            file_name_parts = os.path.splitext(file)
            file_base_name = file_name_parts[0]  # base name which is also the setting id
            file_extension = file_name_parts[-1]

            if not file_extension == ".json":
                continue

            try:
                with open(file_path, "r", encoding = "utf-8") as f:
                    json_data = json.load(f)
                    general = json_data["general"]

                if general["id"] != file_base_name:
                    Logger.log("d", "Setting's filename [%s] does not match to its id [%s]",
                               file_base_name, general["id"])
                    continue

                file_id = file_base_name
                
                #The key is not yet added, no images for this setting
                if file_id not in self._settings_data.keys():
                    self._settings_data[file_id] = {}
                    self._settings_data[file_id]["details"] = json_data

                #Images already added to the list
                if "details" not in self._settings_data[file_id]:
                    self._settings_data[file_id]["details"] = json_data

                # Overwrite images
                if "images" in general:
                    #Logger.log("d", "Overwrite images for setting: %s", file_base_name) # TODO this message only for developing
                    custom_path = "file:///" + images_path
                    self._settings_data[file_id]["images"] = []
                    sorted_images = sorted(general["images"].items())
                    for key, image_name in sorted_images:
                        image_path = os.path.join(custom_path, image_name)
                        self._settings_data[file_id]["images"].append(image_path)

            except Exception as e:
                Logger.logException("w", "Error while reading file: %s" % file)
                continue

    @pyqtSlot(str)
    def setSelectedSetting(self, setting_key: str)-> None:
        # self._settings_data = {}
        # self._loadDescriptionAndImages() Only for developing the plugin

        return_value = {"details": {"general": {"id": setting_key,
                                                "template": "EmptyTemplate.qml"}
                                    }
                        }
        if setting_key != "":
            for key, value in self._settings_data.items():
                if key == setting_key:
                    return_value = value
                    break

        self._selected_setting_data = return_value
        self.settingItemChanged.emit()

    settingItemChanged = pyqtSignal()

    @pyqtSlot(result = str)
    def getPluginpluginVersion(self) -> str:
        return self._version

    @pyqtProperty("QVariantMap", notify = settingItemChanged)
    def selectedSettingData(self) -> Optional["QVariantMap"]:
        return self._selected_setting_data

    @pyqtSlot(result = "QByteArray")
    def getCreatedByImage(self) -> Optional["QByteArray"]:
        plugin_path = PluginRegistry.getInstance().getPluginPath(self.getPluginId())
        images_path = os.path.join(plugin_path, os.path.join("resources", "icons", "createdBy.data"))

        with open(images_path, "rb") as f:
            data = f.read()
            image_64_decoded = base64.b64decode(data)
            image_64_encoded = base64.b64encode(image_64_decoded)

        return image_64_encoded

    replacement_patterns = {
        re.compile(r"^-\s+(.*)"): "<li>\\1</li>\n",
    }

    @pyqtSlot(str, result = str)
    def parseStylingList(self, check_text: str)-> str:
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
