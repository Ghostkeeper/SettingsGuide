//Copyright (C) 2018 Ultimaker B.V.
//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

import UM 1.3 as UM
import Cura 1.0 as Cura

Item {
	id: general_template

	property var setting_data: loaderData
	property string zoomed_image: ""

	// Check for undefined, because after switching loader object the qml still tries to read this data
	property var setting_description: {
		return setting_data["details"]["data"] != undefined ? setting_data["details"]["data"]["description"]: "";
	}
	property var setting_img_description: {
		return setting_data["details"]["data"] != undefined ? setting_data["details"]["data"]["img_description"]: "";
	}
	property var setting_hints: {
		return setting_data["details"]["data"] != undefined ? setting_data["details"]["data"]["hints"]: "";
	}
	property var setting_notes: {
		return setting_data["details"]["data"] != undefined ? setting_data["details"]["data"]["notes"] != undefined ? setting_data["details"]["data"]["notes"] : "" : "";
	}	
	property var setting_images: {
		return setting_data["images"] != undefined ? setting_data["images"] : "";
	}

	ScrollView {
		id: page_scroll_view
		anchors.fill: parent

		Column {
			spacing: UM.Theme.getSize("default_margin").height
			padding: UM.Theme.getSize("wide_margin").width
			id: rect_scroll

			width: general_template.width //Can't use parent.width since it is a ScrollView of infinite dimensions.

			Label {
				id: title

				text: selectedSettingName.properties.label
				font: UM.Theme.getFont("large")
				color: UM.Theme.getColor("text")
				renderType: Text.NativeRendering
			}

			Label {
				id: description

				text: general_template.setting_description
				width: parent.width - parent.padding * 2
				wrapMode: Text.WordWrap
				font: UM.Theme.getFont("default")
				color: UM.Theme.getColor("text")
				renderType: Text.NativeRendering
			}

			GridLayout {
				id: images_grid
				columns: 6
				columnSpacing: UM.Theme.getSize("default_margin").width
				rowSpacing: UM.Theme.getSize("default_margin").height
				visible: setting_images.length > 0
				width: parent.width - parent.padding * 2
				height: 200 * screenScaleFactor + Math.floor((setting_images.length - 1) / 3) * 200 * screenScaleFactor + Math.max(Math.floor((setting_images.length - 1) / 3), 0) * rowSpacing

				Repeater {
					model: setting_images
					Image {
						source: modelData
						fillMode: Image.PreserveAspectFit

						Layout.preferredWidth: (parent.width - parent.columnSpacing * 2) / 3
						Layout.fillWidth: true
						Layout.preferredHeight: 200
						Layout.columnSpan: {
							if(index == setting_images.length - 1) {
								return 6 / ((index % 3) + 1); //2 columns if it's the 3rd item, 3 if it's the 2nd item or 6 if it's the 1st item on the row.
							} else if(index == setting_images.length - 2 && index % 3 == 0) { //If the second-to-last item is 1st on the row, both last items get 3 columns.
								return 3;
							} else {
								return 2;
							}
						}

						//Border.
						Rectangle {
							anchors {
								fill: parent
								margins: -UM.Theme.getSize("thick_lining").width
							}
							color: "transparent"
							border.width: image_mouse_area.containsMouse ? UM.Theme.getSize("thick_lining").width : 0
							border.color: UM.Theme.getColor("primary_hover")

							//Clickable area.
							MouseArea {
								id: image_mouse_area
								anchors.fill: parent
								hoverEnabled: true
								cursorShape: Qt.PointingHandCursor
								onClicked: general_template.zoomed_image = modelData;
							}
						}

						Image {
							source: Qt.resolvedUrl("../../icons/play.svg")
							anchors.centerIn: parent
							opacity: 0.7
							width: 50 * screenScaleFactor
							height: 50 * screenScaleFactor
							visible: modelData.split('.').pop() === "gif" //Only show this for GIF images.
						}
					}
				}
			}

			Label {
				id: img_description

				width: parent.width - parent.padding * 2
				text: general_template.setting_img_description
				font: UM.Theme.getFont("default_italic")
				color: UM.Theme.getColor("text")
				renderType: Text.NativeRendering
				wrapMode: Text.WordWrap
			}

			Label {
				id: hints

				text: manager.parseStylingList(general_template.setting_hints)
				width: parent.width - parent.padding * 2
				font: UM.Theme.getFont("default")
				color: UM.Theme.getColor("text")
				renderType: Text.NativeRendering
				wrapMode: Text.WordWrap
				textFormat: Text.RichText
			}

			Label {
				id: notes

				text: general_template.setting_notes
				width: parent.width - parent.padding * 2
				font: UM.Theme.getFont("default_bold")
				color: UM.Theme.getColor("text")
				renderType: Text.NativeRendering
				wrapMode: Text.WordWrap
			}
		}
	}

	//Zoomed in version of an image, shown only when you click an image.
	Item {
		id: zoom_layer
		anchors.fill: parent
		visible: general_template.zoomed_image !== ""
		z: 1 //On top of the general description.

		Rectangle {
			anchors.fill: parent
			color: UM.Theme.getColor("viewport_background")
			opacity: 0.9
		}

		//Allow reverting zoom level.
		MouseArea {
			anchors.fill: parent
			onClicked: general_template.zoomed_image = ""
			hoverEnabled: true //Catch hover events so that hovering over images behind the overlay doesn't have an effect.
		}

		Rectangle {
			width: zoom_image.paintedWidth
			height: zoom_image.paintedHeight
			color: "white" //Always white regardless of theme, to serve as background to the image.
			anchors.centerIn: parent

			AnimatedImage {
				id: zoom_image
				source: general_template.zoomed_image
				anchors.centerIn: parent
				width: zoom_layer.width * 2 / 3
				height: zoom_layer.height * 2 / 3
				fillMode: Image.PreserveAspectFit
				onStatusChanged: playing = (status == AnimatedImage.Ready)
			}
		}
	}

	UM.SettingPropertyProvider {
		id: selectedSettingName
		containerStack: Cura.MachineManager.activeMachine
		key: manager.selectedSettingId
		watchedProperties: [ "label" ]
	}

	//When switching settings, unzoom the image.
	Connections {
		target: manager
		onSettingItemChanged: general_template.zoomed_image = ""
	}
}