//Copyright (C) 2022 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.2

import UM 1.5 as UM
import Cura 1.0 as Cura

Item {
	id: rightSideItem
	width: UM.Theme.getSize("print_setup_widget").width

	Item {
		id: filterContainer
		anchors {
			top: parent.top
			left: parent.left
			right: parent.right
		}
		height: UM.Theme.getSize("print_setup_big_item").height

		Cura.TextField {
			id: filter
			height: parent.height
			width: parent.width
			topPadding: height / 4
			leftPadding: searchIcon.width + UM.Theme.getSize("default_margin").width * 2
			placeholderText: catalog.i18nc("@label:textbox", "Search settings")
			font.italic: true

			UM.ColorImage {
				id: searchIcon
				anchors {
					verticalCenter: parent.verticalCenter
					left: parent.left
					leftMargin: UM.Theme.getSize("default_margin").width
				}
				height: UM.Theme.getSize("small_button_icon").height
				width: height

				source: UM.Theme.getIcon("search")
				color: UM.Theme.getColor("text")
			}

			onTextChanged: {
				definitionsModel.filter = {"i18n_label": "*" + text};
			}
			Keys.onEscapePressed: {
				text = "";
			}
		}

		UM.SimpleButton {
			id: clearFilterButton
			iconSource: UM.Theme.getIcon("Cancel")
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

	ListView {
		id: articleList
		anchors {
			top: filterContainer.bottom
			topMargin: UM.Theme.getSize("default_margin").height
			bottom: parent.bottom
			right: parent.right
			left: parent.left
		}

		clip: true
		cacheBuffer: 1000000 //Set a large cache to effectively just cache every list item.
		maximumFlickVelocity: 1000
		ScrollBar.vertical: UM.ScrollBar {
			id: scrollBar
		}
		currentIndex: -1

		focus: true  //Focus by default to allow keyboard navigation immediately.
		keyNavigationEnabled: true
		highlightMoveDuration: 100
		highlightMoveVelocity: -1
		highlight: Item {
			UM.ColorImage {
				id: highlightArrow
				height: parent.height
				width: height
				source: Qt.resolvedUrl("../icons/arrow.svg")
				color: UM.Theme.getColor("primary")
			}
			Rectangle {
				anchors {
					left: highlightArrow.right
					top: parent.top
					bottom: parent.bottom
					right: parent.right
					rightMargin: UM.Theme.getSize("default_margin").width
				}

				color: UM.Theme.getColor("primary")
				opacity: 0.1
			}
			Rectangle { //Another rectangle without the opacity, for the border.
				anchors {
					left: highlightArrow.right
					top: parent.top
					bottom: parent.bottom
					right: parent.right
					rightMargin: UM.Theme.getSize("default_margin").width
				}

				border.color: UM.Theme.getColor("action_button_active_border")
				border.width: UM.Theme.getSize("default_lining").width
			}
		}
		onCurrentIndexChanged: { //If index changed due to keyboard navigation.
			if(currentIndex < 0 || !currentItem) {
				manager.selectedArticleId = "";
			} else {
				manager.selectedArticleId = currentItem.definition.key;
			}
		}
		Keys.onDownPressed: {
			var originalIndex = articleList.currentIndex; //In case we need to revert because everything below us is a category; we can only know that by going there (until Qt 5.13).
			if(articleList.currentIndex < articleList.count - 1) {
				articleList.currentIndex++;
			}
			while(articleList.currentItem.definition.type == "category" && articleList.currentIndex < articleList.count - 1) {
				articleList.currentIndex++;
			}
			if(articleList.currentItem.definition.type == "category") { //Every item below us is a category.
				articleList.currentIndex = originalIndex;
			}
		}
		Keys.onUpPressed: {
			var originalIndex = articleList.currentIndex; //In case we need to revert because everything above us is a category; we can only know that by going there (until Qt 5.13).
			if(articleList.currentIndex > 0) {
				articleList.currentIndex--;
			}
			while(articleList.currentItem.definition.type == "category" && articleList.currentIndex > 0) {
				articleList.currentIndex--;
			}
			if(articleList.currentItem.definition.type == "category") { //Every item above us is a category.
				articleList.currentIndex = originalIndex;
			}
		}

		onCountChanged: { //When we collapse categories, make sure that the selected item doesn't rest on a category.
			if(!articleList.currentItem) { //Just building up the list so far.
				return;
			}
			while(articleList.currentItem.definition.type == "category" && articleList.currentIndex < articleList.count - 1) {
				articleList.currentIndex++;
			}
			while(articleList.currentItem.definition.type == "category" && articleList.currentIndex > 0) {
				articleList.currentIndex--;
			}
			if(articleList.currentItem.definition.type == "category") { //All categories are collapsed.
				articleList.currentIndex = -1;
			}
		}

		Connections {
			target: manager
			onCurrentArticleReset: {
				articleList.currentIndex = -1;
			}
		}

		model: UM.SettingDefinitionsModel {
			id: definitionsModel
			containerId: "settings_guide_definitions"
			showAll: true
			showAncestors: true
			exclude: ["command_line_settings", "infill_mesh", "infill_mesh_order", "cutting_mesh", "support_mesh", "anti_overhang_mesh"] // TODO: infill_mesh settings are excluded hardcoded, but should be based on the fact that settable_globally, settable_per_meshgroup and settable_per_extruder are false.
			expanded: filter.text === "" ? CuraApplication.expandedCategories : ["*"]
		}

		delegate: Loader {
			id: articleLoader
			width: parent.width - (scrollBar.width + UM.Theme.getSize("narrow_margin").width)

			property var definition: model
			property var articleDefinitionsModel: definitionsModel

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
						return Qt.resolvedUrl("SidebarSettings/SettingComboBox.qml");
					case "bool":
						return Qt.resolvedUrl("SidebarSettings/SettingCheckBox.qml");
					case "str":
						return Qt.resolvedUrl("SidebarSettings/SettingTextField.qml");
					case "category":
						return Qt.resolvedUrl("SidebarSettings/SettingCategory.qml");
					case "optional_extruder":
						return Qt.resolvedUrl("SidebarSettings/SettingComboBox.qml");
					default:
						return Qt.resolvedUrl("SidebarSettings/SettingTextField.qml");
				}
			}
		}
	}

	UM.I18nCatalog {
		id: catalog
		name: "cura"
	}
}
