//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.2

import UM 1.2 as UM
import Cura 1.0 as Cura

Item {
	id: rightSideItem
	width: UM.Theme.getSize("print_setup_widget").width

	Rectangle {
		id: filterContainer

		border.width: Math.round(UM.Theme.getSize("default_lining").width)
		border.color: {
			if(hoverMouseArea.containsMouse || clearFilterButton.containsMouse) {
				return UM.Theme.getColor("setting_control_border_highlight");
			}
			else {
				return UM.Theme.getColor("setting_control_border");
			}
		}

		color: UM.Theme.getColor("setting_control")

		anchors {
			top: parent.top
			topMargin: UM.Theme.getSize("default_margin").height
			left: parent.left
			leftMargin: UM.Theme.getSize("default_margin").width
			right: parent.right
			rightMargin: Math.floor(UM.Theme.getSize("default_margin").width / 2)
		}
		height: UM.Theme.getSize("setting_control").height
		width: rightSideItem.width

		TextField {
			id: filter
			height: parent.height
			anchors.left: filterContainer.left
			anchors.right: filterContainer.right
			anchors.rightMargin: Math.round(UM.Theme.getSize("default_margin").width)

			placeholderText: "Search..."

			style: TextFieldStyle {
				textColor: UM.Theme.getColor("setting_control_text")
				placeholderTextColor: UM.Theme.getColor("setting_control_text")
				font: UM.Theme.getFont("default");
				background: Item {}
			}

			onTextChanged: {
				definitionsModel.filter = {"i18n_label": "*" + text};
			}

			Keys.onEscapePressed: {
				filter.text = "";
			}
		}

		MouseArea {
			id: hoverMouseArea
			anchors.fill: parent
			hoverEnabled: true
			acceptedButtons: Qt.NoButton
			cursorShape: Qt.IBeamCursor
		}

		UM.SimpleButton {
			id: clearFilterButton
			iconSource: UM.Theme.getIcon("cross1")
			visible: filter.text.length > 0

			height: Math.round(parent.height * 0.4)
			width: visible ? height : 0

			anchors.verticalCenter: parent.verticalCenter
			anchors.right: parent.right
			anchors.rightMargin: UM.Theme.getSize("default_margin").width

			color: UM.Theme.getColor("setting_control_button")
			hoverColor: UM.Theme.getColor("setting_control_button_hover")

			onClicked: {
				filter.text = "";
				filter.forceActiveFocus();
			}
		}
	}

	ScrollView {
		id: scrollView

		anchors.top: filterContainer.bottom
		anchors.bottom: parent.bottom
		anchors.right: parent.right
		anchors.left: parent.left
		anchors.topMargin: filterContainer.visible ? UM.Theme.getSize("default_margin").height : 0
		style: scrollview_settings_guide
		flickableItem.flickableDirection: Flickable.VerticalFlick
		__wheelAreaScrollSpeed: 75 // Scroll three lines in one scroll event

		ListView {
			id: contents
			spacing: Math.round(UM.Theme.getSize("default_lining").height)
			cacheBuffer: 1000000 //Set a large cache to effectively just cache every list item.

			height: parent.height
			currentIndex: -1

			model: UM.SettingDefinitionsModel {
				id: definitionsModel
				containerId: "settings_guide_definitions"
				showAll: true
				showAncestors: true
				exclude: ["machine_settings", "command_line_settings", "infill_mesh", "infill_mesh_order", "cutting_mesh", "support_mesh", "anti_overhang_mesh"] // TODO: infill_mesh settigns are excluded hardcoded, but should be based on the fact that settable_globally, settable_per_meshgroup and settable_per_extruder are false.
				expanded: filter.text === "" ? CuraApplication.expandedCategories : ["*"]
			}

			delegate: Loader {
				id: settingLoader

				width: parent.width
				height: model.type != undefined ? UM.Theme.getSize("section").height : 0

				property var definition: model
				property var settingDefinitionsModel: definitionsModel

				asynchronous: true
				active: model.type != undefined

				source: {
					switch (model.type) {
						case "int":
							return Qt.resolvedUrl("SidebarSettings/SettingTextField.qml");
						case "[int]":
							return Qt.resolvedUrl("SidebarSettings/SettingTextField.qml");
						case "float":
							return Qt.resolvedUrl("SidebarSettings/SettingTextField.qml");
						case "enum":
							return Qt.resolvedUrl("SidebarSettings/SettingComboBox.qml");
						case "extruder":
							return Qt.resolvedUrl("SidebarSettings/SettingExtruder.qml");
						case "bool":
							return Qt.resolvedUrl("SidebarSettings/SettingCheckBox.qml");
						case "str":
							return Qt.resolvedUrl("SidebarSettings/SettingTextField.qml");
						case "category":
							return Qt.resolvedUrl("SidebarSettings/SettingCategory.qml");
						case "optional_extruder":
							return Qt.resolvedUrl("SidebarSettings/SettingExtruder.qml");
						default:
							return Qt.resolvedUrl("SidebarSettings/SettingTextField.qml");
					}
				}
			}
			UM.SettingPropertyProvider {
				id: inheritStackProvider
				containerStackId: Cura.MachineManager.activeMachineId
			}

			UM.SettingPropertyProvider {
				id: provider
				containerStackId: Cura.MachineManager.activeMachineId
			}
		}
	}

	property Component scrollview_settings_guide: Component {
		ScrollViewStyle {
			decrementControl: Item {}
			incrementControl: Item {}

			transientScrollBars: false

			scrollBarBackground: Rectangle {
				implicitWidth: UM.Theme.getSize("scrollbar").width
				radius: Math.round(implicitWidth / 2)
				color: UM.Theme.getColor("scrollbar_background")
			}

			handle: Rectangle {
				id: scrollViewHandle
				implicitWidth: UM.Theme.getSize("scrollbar").width
				radius: Math.round(implicitWidth / 2)

				color: styleData.pressed ? UM.Theme.getColor("scrollbar_handle_down") : styleData.hovered ? UM.Theme.getColor("scrollbar_handle_hover") : UM.Theme.getColor("scrollbar_handle");
			}
		}
	}

	UM.I18nCatalog {
		id: catalog
		name: "cura"
	}
}
