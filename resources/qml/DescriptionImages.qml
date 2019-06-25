//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Layouts 1.3
import UM 1.3 as UM

GridLayout {
	id: images_grid
	columns: 6
	columnSpacing: UM.Theme.getSize("default_margin").width
	rowSpacing: UM.Theme.getSize("default_margin").height
	height: 200 * screenScaleFactor + Math.floor((description_data.length - 1) / 3) * 200 * screenScaleFactor + Math.max(Math.floor((description_data.length - 1) / 3), 0) * rowSpacing

	property var description_data

	Repeater {
		model: images_grid.description_data

		Item {
			Layout.preferredWidth: (parent.width - parent.columnSpacing * 2) / 3
			Layout.fillWidth: true
			Layout.preferredHeight: 200
			Layout.columnSpan: {
				if(index == images_grid.description_data.length - 1) {
					return 6 / ((index % 3) + 1); //2 columns if it's the 3rd item, 3 if it's the 2nd item or 6 if it's the 1st item on the row.
				} else if(index == images_grid.description_data.length - 2 && index % 3 == 0) {
					return 3; //If the second-to-last item is 1st on the row, both last items get 3 columns.
				} else {
					return 2; //Normal image width.
				}
			}

			Text {
				id: image_description
				text: modelData.substring(modelData.indexOf("|") + 1)
				wrapMode: Text.Wrap
				font: UM.Theme.getFont("default_italic")
				color: UM.Theme.getColor("text")
				renderType: Text.NativeRendering
				horizontalAlignment: Text.AlignHCenter
				anchors {
					left: parent.left
					right: parent.right
					bottom: parent.bottom
				}
			}

			Item {
				anchors {
					left: parent.left
					right: parent.right
					top: parent.top
					bottom: parent.bottom
					bottomMargin: image_description.contentHeight
				}
				//Border and background.
				Rectangle {
					anchors.centerIn: parent
					width: thumbnail.paintedWidth + border.width * 2
					height: thumbnail.paintedHeight + border.width * 2
					color: "white" //Always white regardless of theme in order to provide a fixed background for the image.
					border.width: image_mouse_area.containsMouse ? UM.Theme.getSize("thick_lining").width : 0
					border.color: UM.Theme.getColor("primary_hover")

					//Clickable area.
					MouseArea {
						id: image_mouse_area
						anchors.fill: parent
						hoverEnabled: true
						cursorShape: Qt.PointingHandCursor
						onClicked: settingsGuideBase.zoomed_image = modelData.substring(0, modelData.indexOf("|"));
					}
				}

				Image {
					id: thumbnail
					source: modelData.substring(0, modelData.indexOf("|"))
					fillMode: Image.PreserveAspectFit
					mipmap: true
					anchors.fill: parent
				}

				Image {
					source: Qt.resolvedUrl("../icons/play.svg")
					anchors.centerIn: parent
					opacity: 0.7
					width: 50 * screenScaleFactor
					height: 50 * screenScaleFactor
					visible: modelData.substring(0, modelData.indexOf("|")).split('.').pop() === "gif" //Only show this for animations.
				}
			}
		}
	}
}