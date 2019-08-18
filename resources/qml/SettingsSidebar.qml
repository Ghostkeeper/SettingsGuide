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

	Label {
		id: debug
		text: articleList.currentIndex
	}

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
			id: articleList
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

			focus: true
			keyNavigationEnabled: true
			highlight: Item { //Needs a surrounding item that adapts to the full width/height of the current item. ListView does that.
				Image {
					id: highlightArrow
					height: parent.height
					width: parent.height
					source: Qt.resolvedUrl("../icons/arrow.svg")
				}
				Rectangle {
					color: UM.Theme.getColor("primary")
					opacity: 0.1
					anchors {
						left: highlightArrow.right
						top: parent.top
						bottom: parent.bottom
						right: parent.right
						rightMargin: UM.Theme.getSize("scrollbar").width
					}
				}
				Rectangle {
					color: "transparent"
					border.color: UM.Theme.getColor("action_button_active_border")
					border.width: 1
					anchors {
						left: highlightArrow.right
						top: parent.top
						bottom: parent.bottom
						right: parent.right
						rightMargin: UM.Theme.getSize("scrollbar").width
					}
				}
			}
			highlightMoveDuration: 100
			highlightMoveVelocity: -1
			onCurrentIndexChanged: { //If index changed due to keyboard navigation.
				manager.selectedSettingId = currentItem.definition.key;
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

			Keys.onDownPressed: {
				var originalIndex = articleList.currentIndex; //In case we need to revert because everything below us is a category; we can only know that by going there (until Qt 5.13).
				if(articleList.currentIndex + 1 < articleList.count - 1) {
					articleList.currentIndex++;
				}
				while(articleList.currentItem.definition.type == "category" && articleList.currentIndex + 1 < articleList.count - 1) {
					articleList.currentIndex++;
				}
				if(articleList.currentItem.definition.type == "category") { //Every item below us is a category.
					articleList.currentIndex = originalIndex;
				}
			}
			Keys.onUpPressed: {
				var originalIndex = articleList.currentIndex; //In case we need to revert because everything above us is a category; we can only know that by going there (until Qt 5.13).
				if(articleList.currentIndex - 1 >= 0) {
					articleList.currentIndex--;
				}
				while(articleList.currentItem.definition.type == "category" && articleList.currentIndex - 1 >= 0) {
					articleList.currentIndex--;
				}
				if(articleList.currentItem.definition.type == "category") { //Every item above us is a category.
					articleList.currentIndex = originalIndex;
				}
			}
			onCountChanged: { //When we collapse categories, make sure that the selected item doesn't rest on a category.
				while(articleList.currentItem.definition.type == "category" && articleList.currentIndex + 1 < articleList.count - 1) {
					articleList.currentIndex++;
				}
				while(articleList.currentItem.definition.type == "category" && articleList.currentIndex - 1 >= 0) {
					articleList.currentIndex--;
				}
				if(articleList.currentItem.definition.type == "category") { //All categories are collapsed.
					articleList.currentIndex = -1;
				}
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
