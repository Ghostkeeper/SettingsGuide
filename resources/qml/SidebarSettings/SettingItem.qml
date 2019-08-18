//Copyright (C) 2018 Ultimaker B.V.
//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Layouts 1.2
import QtQuick.Controls 2.0

import UM 1.1 as UM
import Cura 1.0 as Cura

Item {
	id: base

	height: UM.Theme.getSize("section").height

	property alias contents: controlContainer.children

	Connections {
		target: manager
		onSelectedArticleChanged: {
			if(manager.selectedArticleId == definition.key) {
				articleList.currentIndex = index;
			}
		}
	}
	Component.onCompleted: {
		//If the selected article was changed before loading was complete, make sure the index is updated.
		//This happens when you open the settings guide for the first time by right-clicking on a setting.
		if(manager.selectedArticleId == definition.key) {
			articleList.currentIndex = index;
		}
	}

	MouseArea {
		id: mouse
		anchors.fill: parent
		acceptedButtons: Qt.LeftButton
		hoverEnabled: true
		onClicked: {
			manager.selectedArticleId = definition.key;
			articleList.forceActiveFocus(); //After clicking on any article, pressing up or down allows keyboard navigation through the list.
		}

		Rectangle {
			visible: mouse.containsMouse
			color: UM.Theme.getColor("primary")
			opacity: 0.1
			anchors {
				left: parent.left
				leftMargin: parent.height //Leave room for the marker icon.
				right: parent.right
				rightMargin: UM.Theme.getSize("default_margin").width
				top: parent.top
				bottom: parent.bottom
			}
		}

		Label {
			id: label

			anchors.left: parent.left
			anchors.leftMargin: Math.round((UM.Theme.getSize("section_icon_column").width + 5) + ((definition.depth - 1) * UM.Theme.getSize("setting_control_depth_margin").width))
			anchors.verticalCenter: parent.verticalCenter

			text: definition.label
			elide: Text.ElideMiddle
			renderType: Text.NativeRendering

			color: UM.Theme.getColor("setting_control_text")
			opacity: (definition.visible) ? 1 : 0.5
			font: UM.Theme.getFont("default")
		}

		Item {
			id: controlContainer

			enabled: propertyProvider.isValueUsed

			anchors.right: parent.right
			anchors.rightMargin: UM.Theme.getSize("default_margin").width
			anchors.verticalCenter: parent.verticalCenter
			width: UM.Theme.getSize("setting_control").width
			height: UM.Theme.getSize("setting_control").height
		}
	}
}
