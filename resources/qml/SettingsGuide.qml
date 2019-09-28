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

	property string zoomed_image

	UM.I18nCatalog {
		id: catalog
		name: "cura"
	}

	//Display icon in the middle of the window
	Item {
		id: icon_item
		width: parent.width - rightSideItem.width
		height: parent.height
		visible: manager.selectedArticleId === ""

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
			id: article_scroll
			anchors {
				left: parent.left
				right: rightSideItem.left
				top: parent.top
				bottom: parent.bottom
			}
			visible: manager.selectedArticleId !== ""

			Column {
				id: content_column
				anchors {
					left: parent.left
					leftMargin: UM.Theme.getSize("wide_margin").width
					top: parent.top
					topMargin: UM.Theme.getSize("wide_margin").height
				}
				width: article_scroll.width - UM.Theme.getSize("wide_margin").width * 2
				spacing: UM.Theme.getSize("wide_margin").height

				Text {
					text: selectedArticleName.properties.label ? "<h1>" + selectedArticleName.properties.label + "</h1>" : ""
					width: parent.width
					wrapMode: Text.Wrap
					renderType: Text.NativeRendering
					font: UM.Theme.getFont("medium")
					color: UM.Theme.getColor("text")
				}

				Repeater {
					model: manager.selectedArticle
					delegate: Component {
						Loader {
							source: switch(modelData[0]) {
								case "rich_text": return "ArticleText.qml";
								case "images": return "ArticleImages.qml";
							}
							width: content_column.width
							onLoaded: {
								item.article_data = modelData.slice(1);
							}
						}
					}
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

		//Zoomed in version of an image, shown only when you click an image.
		Item {
			id: zoom_layer
			anchors {
				left: parent.left
				right: rightSideItem.left
				top: parent.top
				bottom: parent.bottom
			}
			visible: settingsGuideBase.zoomed_image !== ""
			z: 1 //On top of the general article.

			Rectangle {
				anchors.fill: parent
				color: UM.Theme.getColor("viewport_background")
				opacity: 0.9
			}

			//Allow reverting zoom level.
			MouseArea {
				anchors.fill: parent
				onClicked: settingsGuideBase.zoomed_image = ""
				hoverEnabled: true //Catch hover events so that hovering over images behind the overlay doesn't have an effect.
			}

			Connections {
				target: manager
				onSelectedArticleChanged: settingsGuideBase.zoomed_image = ""
			}

			Rectangle {
				width: zoom_image.visible ? zoom_image.paintedWidth : zoom_image_svg.paintedWidth
				height: zoom_image.visible ? zoom_image.paintedHeight : zoom_image_svg.paintedWidth
				color: "white" //Always white regardless of theme, to serve as background to the image.
				anchors.centerIn: parent

				AnimatedImage {
					id: zoom_image
					source: visible ? settingsGuideBase.zoomed_image : "" //Don't even try to render for SVG.
					anchors.centerIn: parent
					width: zoom_layer.width * 2 / 3
					height: zoom_layer.height * 2 / 3
					fillMode: Image.PreserveAspectFit
					mipmap: true
					onStatusChanged: playing = (status == AnimatedImage.Ready)
					visible: settingsGuideBase.zoomed_image.split('.').pop() !== "svg" //Only for non-SVG.
				}

				Image { //Special one for SVG that automatically adjusts sourceSize. sourceSize is not supported for AnimatedImage, and AnimatedImage doesn't support animated SVG anyway.
					id: zoom_image_svg
					source: visible ? settingsGuideBase.zoomed_image : "" //Don't even try to render for non-SVG.
					anchors.centerIn: parent
					width: zoom_image.width
					height: zoom_image.height
					fillMode: Image.PreserveAspectFit
					sourceSize.width: width
					sourceSize.height: height
					visible: !zoom_image.visible //Only for SVG.
				}
			}
		}
	}

	UM.SettingPropertyProvider {
		id: selectedArticleName
		containerStack: manager.containerStack
		key: manager.selectedArticleId
		watchedProperties: ["label"]
	}
}
