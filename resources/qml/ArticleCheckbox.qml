//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Controls 2.0
import UM 1.3 as UM

//Draws a checkbox that the user can check or uncheck.
//The checkbox is linked to a preference value. Clicking it will change the
//preference.

Row {
	property var article_data

	CheckBox {
		id: checkbox
		text: article_data[1]

		checked: UM.Preferences.getValue(article_data[0])
		onClicked: UM.Preferences.setValue(article_data[0], checked)

		background: Item {}
		indicator: Rectangle {
			width: UM.Theme.getSize("checkbox").width
			height: UM.Theme.getSize("checkbox").height
			color: UM.Theme.getColor(checkbox.hovered ? "checkbox_hover" : "checkbox")
			radius: UM.Theme.getSize("checkbox_radius").width
			border.width: UM.Theme.getSize("default_lining").width
			border.color: UM.Theme.getColor(checkbox.hovered ? "checkbox_border_hover" : "checkbox_border")

			UM.RecolorImage
			{
				anchors.verticalCenter: parent.verticalCenter
				anchors.horizontalCenter: parent.horizontalCenter
				width: Math.round(parent.width / 2.5)
				height: Math.round(parent.height / 2.5)
				sourceSize.height: width
				color: UM.Theme.getColor("checkbox_mark")
				source: UM.Theme.getIcon("check")
				opacity: checkbox.checked
				Behavior on opacity {
					NumberAnimation {
					duration: 100
					}
				}
			}
		}

		contentItem: Text {
			text: checkbox.text
			color: UM.Theme.getColor("checkbox_text")
			font: UM.Theme.getFont("default")
			elide: Text.ElideRight
			renderType: Text.NativeRendering
			leftPadding: checkbox.indicator.width
		}
	}
}