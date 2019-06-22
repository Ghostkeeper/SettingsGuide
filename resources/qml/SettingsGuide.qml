//Copyright (C) 2018 Ultimaker B.V.
//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 2.3

import UM 1.2 as UM
import Cura 1.0 as Cura

Window {
	id: settingsGuideBase
	title: catalog.i18nc("@title", "Cura Settings Guide") + " (" + manager.pluginVersion + ")"
	modality: Qt.NonModal

	width: 1200 * screenScaleFactor
	height: 640 * screenScaleFactor
	minimumWidth: 800 * screenScaleFactor
	minimumHeight: 400 * screenScaleFactor

	color: UM.Theme.getColor("main_background")

	UM.I18nCatalog {
		id: catalog
		name: "cura"
	}

	//Display icon in the middle of the window
	Item {
		id: icon_item
		width: parent.width - rightSideItem.width
		height: parent.height
		visible: manager.selectedSettingId === ""

		anchors {
			leftMargin: UM.Theme.getSize("wide_margin").width
			rightMargin: UM.Theme.getSize("wide_margin").width
		}

		Image {
			id: welcome_icon
			source: Qt.resolvedUrl("../icons/icon.svg")
			width: 300 * screenScaleFactor
			height: 300 * screenScaleFactor

			anchors.centerIn: parent
		}

		Label {
			id: versionLabel
			anchors.bottom: welcome_icon.bottom
			anchors.left: welcome_icon.right
			font.pixelSize: 22 * screenScaleFactor
			font.italic: true
			color: UM.Theme.getColor("text")

			text: "v" + manager.pluginVersion
		}
	}

	Item {
		id: globalItem
		anchors.fill: parent
		focus: true

		Rectangle {
			id: rightSideItem
			width: UM.Theme.getSize("print_setup_widget").width
			border.color: UM.Theme.getColor("lining")
			border.width: UM.Theme.getSize("default_lining").width
			color: "transparent"

			anchors {
				top: globalItem.top
				right: parent.right
				bottom: globalItem.bottom
			}

			SettingsSidebar {
				id: settingsSidebar
				anchors.fill: parent
			}
		}

		ScrollView {
			id: description_scroll
			anchors {
				left: parent.left
				right: rightSideItem.left
				top: parent.top
				bottom: parent.bottom
			}
			Column {
				anchors {
					left: parent.left
					leftMargin: UM.Theme.getSize("wide_margin").width
					top: parent.top
					topMargin: UM.Theme.getSize("wide_margin").height
				}
				width: description_scroll.width - UM.Theme.getSize("wide_margin").width * 2
				spacing: UM.Theme.getSize("wide_margin").height

				Text {
					text: selectedSettingName.properties.label
					width: parent.width
					wrapMode: Text.Wrap
					renderType: Text.NativeRendering
					font: UM.Theme.getFont("large")
				}
				Text {
					text: manager.selectedSettingDescription
					width: parent.width
					wrapMode: Text.Wrap
					renderType: Text.NativeRendering
					font: UM.Theme.getFont("default")
				}
				Item {
					/* The scrollview's dimensions depend on the content height,
					but since we move the contents down with a margin, the
					bottom part of the column is not visible. So we add some
					content at the bottom to adjust the total height of the
					column and all the actual content is still visible. */
					width: parent.width
					height: UM.Theme.getSize("wide_margin").height
				}
			}
		}
	}

	UM.SettingPropertyProvider {
		id: selectedSettingName
		containerStack: Cura.MachineManager.activeMachine
		key: manager.selectedSettingId
		watchedProperties: ["label"]
	}
}
