//Copyright (C) 2022 Ghostkeeper
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
	anchors.left: parent.left
	anchors.right: parent.right
	height: UM.Theme.getSize("section").height + UM.Theme.getSize("narrow_margin").height

	property alias contents: controlContainer.children

	Connections {
		target: manager
		function onSelectedArticleChanged() {
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
			anchors.fill: parent
		}

		Label {
			anchors {
				left: parent.left
				leftMargin: Math.round(UM.Theme.getSize("thin_margin").width + ((definition.depth - 1) * UM.Theme.getSize("default_margin").width))
				right: controlContainer.left
				verticalCenter: parent.verticalCenter
			}

			text: definition.label
			elide: Text.ElideMiddle
			renderType: Text.NativeRendering
			textFormat: Text.PlainText
			font: UM.Theme.getFont("default")
			color: UM.Theme.getColor("setting_control_text")
		}

		Item {
			id: controlContainer

			anchors.right: parent.right
			anchors.verticalCenter: parent.verticalCenter
			width: UM.Theme.getSize("setting_control").width
			height: UM.Theme.getSize("setting_control").height
		}
	}
}
