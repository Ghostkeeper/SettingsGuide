//Copyright (C) 2018 Ultimaker B.V.
//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4

import UM 1.2 as UM
import Cura 1.0 as Cura

Window {
	id: settingsGuideBase
	title: catalog.i18nc("@title", "Cura Settings Guide") + " (" + manager.getPluginpluginVersion() + ")"
	modality: Qt.ApplicationModal
	flags: Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint

	width: 1200 * screenScaleFactor
	height: 640 * screenScaleFactor
	minimumWidth: width
	maximumWidth: minimumWidth
	minimumHeight: height
	maximumHeight: minimumHeight

	color: UM.Theme.getColor("main_background")

	UM.I18nCatalog {
		id: catalog
		name: "cura"
	}

	property alias selectedSettingId: settingsSidebar.selectedSettingId

	//Display icon in the middle of the window
	Item {
		id: icon_item
		width: parent.width - rightSideItem.width
		height: parent.height

		anchors {
			leftMargin: 20
			rightMargin: 20
		}

		Image {
			id: welcome_icon
			source: Qt.resolvedUrl("../icons/icon.png")
			width: 300
			height: 300

			anchors.horizontalCenter: icon_item.horizontalCenter
			anchors.verticalCenter: parent.verticalCenter
			opacity: 0.5
		}

		Label {
			id: versionLabel
			anchors.top : welcome_icon.bottom
			anchors.topMargin: -60
			anchors.left: welcome_icon.right
			font.pixelSize: 22
			font.italic: true
			color: "#959596"

			text: "v" + manager.getPluginpluginVersion()
		}
	}

	Item {
		id: globalItem
		anchors.fill: parent

		focus: true
		//Handle escape button press here because in loader they will be not accepted.
		Keys.onEscapePressed: {
			if (typeof pageLoader.loaderEscpaPressHandler === "function") {
				pageLoader.loaderEscpaPressHandler();
			}
		}

		Rectangle {
			id: rightSideItem
			width: UM.Theme.getSize("print_setup_widget").width
			border.color: UM.Theme.getColor("lining")
			border.width: 1
			color: "transparent"

			anchors {
				top: globalItem.top
				right: parent.right
				bottom: globalItem.bottom
				topMargin: 0
				bottomMargin: 0
				rightMargin: 0
				leftMargin: 0
			}

			SettingsSidebar {
				id: settingsSidebar
				anchors.fill: parent
				anchors.leftMargin: 1
			}
		}


		// Here we show our help images with hints and descriptions, and etc..
		Loader {
			id: pageLoader

			// Every template might subscribe for this property which will be triggered for after "Escape" button click
			property var loaderEscpaPressHandler: ""

			property var loaderData: undefined // The object which is holds all information for the Loader Item
			property var loaderCallBack: undefined // The function cann be triggered for performating actions in Loader Item
			anchors {
				left: parent.left
				right: rightSideItem.left
				top: parent.top
				bottom: parent.bottom
			}
		}

		// This timer is only for calling 'CallBack' function with delay because Loader source element might be
		// loaded also with delay
		Timer {
			id: loaderSourceChangeTimer
			interval: 100
			repeat: false
			onTriggered: {
				if (typeof pageLoader.loaderCallBack === "function") {
					pageLoader.loaderCallBack();
				}
			}
		}
	}

	function callSettingItemChanged() {
		var data = manager.selectedSettingData;
		var template = "";

		var setting_template = undefined;
		if(data["details"] != undefined && data["details"]["general"] != undefined) {
			var setting_template = data["details"]["general"]["template"];
		}

		var isCreatedBy = false
		if (settingsSidebar.selectedSettingId != "" && settingsSidebar.selectedSettingId.toLowerCase() == "createdby") {
			isCreatedBy = true;
		}

		// Selected setting uses general template
		if (settingsSidebar.selectedSettingId != "" && setting_template == undefined) {
			template = 1;
		}
		// Selected setting has a different template
		else if (settingsSidebar.selectedSettingId != "" && !isCreatedBy && setting_template != undefined) {
			template = 2;
		}
		// Special view which shows created by Template
		else if (isCreatedBy == true) {
			template = 99;
		}
		// Show welcome page
		else {
			template = -1;
		}

		var template_path = "";
		switch (template) {
			case 1:
				template_path = Qt.resolvedUrl("SidebarSettingTemplates/GeneralTemplate.qml");
				break;
			case 2:
				template_path = Qt.resolvedUrl("SidebarSettingTemplates/" + setting_template);
				break;
			case 99:
				template_path = Qt.resolvedUrl("CreatedBy.qml");
				break;
		}

		if (template_path != "") {
			pageLoader.loaderData = data;
			icon_item.visible = false;
			pageLoader.source = ""; // for some reason if don't do this then QT will not unload the previous source properly
			pageLoader.source = template_path;
		}
		else {
			icon_item.visible = true;
			pageLoader.source = "";
			settingsSidebar.selectedSettingId = "";
		}

		// Call Timer to trigger call back function
		loaderSourceChangeTimer.restart();

	}

	// After selecting the setting show proper template of the setting's guide
	Connections {
		target: manager
		onSettingItemChanged: {
			callSettingItemChanged();
		}
	}
}
