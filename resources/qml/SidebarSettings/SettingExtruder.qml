//Copyright (C) 2016 Ultimaker B.V.
//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Controls 2.0

import UM 1.1 as UM
import Cura 1.0 as Cura
import GuideTheme 1.0 as GuideThemeNS

SettingItem {
	id: base
	property var focusItem: control

	contents: ComboBox {
		id: control
		anchors.fill: parent

		indicator: UM.RecolorImage {
			id: downArrow
			x: control.width - width - control.rightPadding
			y: control.topPadding + Math.round((control.availableHeight - height) / 2)

			source: UM.Theme.getIcon("arrow_bottom")
			width: GuideThemeNS.Theme.getSize("standard_arrow").width
			height: GuideThemeNS.Theme.getSize("standard_arrow").height
			sourceSize.width: width + 5 * screenScaleFactor
			sourceSize.height: width + 5 * screenScaleFactor

			color: GuideThemeNS.Theme.getColor("setting_control_text")
		}

		property string color: "#fff"

		background: Rectangle {
			color: {
				if (!enabled) {
					return GuideThemeNS.Theme.getColor("setting_control_disabled");
				}
				if (control.hovered || base.activeFocus) {
					return GuideThemeNS.Theme.getColor("setting_control_highlight");
				}
				return GuideThemeNS.Theme.getColor("setting_control");
			}
			border.width: GuideThemeNS.Theme.getSize("default_lining").width
			border.color: {
				if (!enabled) {
					return GuideThemeNS.Theme.getColor("setting_control_disabled_border");
				}
				if (control.hovered || control.activeFocus) {
					return GuideThemeNS.Theme.getColor("setting_control_border_highlight");
				}
				return GuideThemeNS.Theme.getColor("setting_control_border");
			}
		}

		contentItem: Label {
			anchors.verticalCenter: parent.verticalCenter
			anchors.left: parent.left
			anchors.leftMargin: GuideThemeNS.Theme.getSize("setting_unit_margin").width
			anchors.right: downArrow.left
			rightPadding: swatch.width + GuideThemeNS.Theme.getSize("setting_unit_margin").width

			text: control.currentText
			renderType: Text.NativeRendering
			font: GuideThemeNS.Theme.getFont("default")
			color: enabled ? GuideThemeNS.Theme.getColor("setting_control_text") : GuideThemeNS.Theme.getColor("setting_control_disabled_text")

			elide: Text.ElideLeft
			verticalAlignment: Text.AlignVCenter

			background: Rectangle {
				id: swatch
				height: Math.round(GuideThemeNS.Theme.getSize("setting_control").height / 2)
				width: height

				anchors.right: parent.right
				anchors.verticalCenter: parent.verticalCenter
				anchors.margins: Math.round(GuideThemeNS.Theme.getSize("default_margin").width / 4)

				border.width: GuideThemeNS.Theme.getSize("default_lining").width
				border.color: enabled ? GuideThemeNS.Theme.getColor("setting_control_border") : GuideThemeNS.Theme.getColor("setting_control_disabled_border")
				radius: Math.round(width / 2)

				color: control.color
			}
		}

		popup: Popup {
			y: control.height - GuideThemeNS.Theme.getSize("default_lining").height
			width: control.width
			implicitHeight: contentItem.implicitHeight
			padding: GuideThemeNS.Theme.getSize("default_lining").width

			contentItem: ListView {
				clip: true
				implicitHeight: contentHeight
				model: control.popup.visible ? control.delegateModel : null
				currentIndex: control.highlightedIndex

				ScrollIndicator.vertical: ScrollIndicator {}
			}

			background: Rectangle {
				color: GuideThemeNS.Theme.getColor("setting_control")
				border.color: GuideThemeNS.Theme.getColor("setting_control_border")
			}
		}

		delegate: ItemDelegate {
			width: control.width - 2 * GuideThemeNS.Theme.getSize("default_lining").width
			height: control.height
			highlighted: control.highlightedIndex == index

			contentItem: Label {
				text: model.name
				renderType: Text.NativeRendering
				color: {
					if (model.enabled) {
						GuideThemeNS.Theme.getColor("setting_control_text");
					} else {
						GuideThemeNS.Theme.getColor("action_button_disabled_text");
					}
				}
				font: GuideThemeNS.Theme.getFont("default")
				elide: Text.ElideRight
				verticalAlignment: Text.AlignVCenter
				rightPadding: swatch.width + GuideThemeNS.Theme.getSize("setting_unit_margin").width

				background: Rectangle {
					id: swatch
					height: Math.round(GuideThemeNS.Theme.getSize("setting_control").height / 2)
					width: height

					anchors.right: parent.right
					anchors.verticalCenter: parent.verticalCenter
					anchors.margins: Math.round(GuideThemeNS.Theme.getSize("default_margin").width / 4)

					border.width: GuideThemeNS.Theme.getSize("default_lining").width
					border.color: enabled ? GuideThemeNS.Theme.getColor("setting_control_border") : GuideThemeNS.Theme.getColor("setting_control_disabled_border")
					radius: Math.round(width / 2)

					color: control.model.getItem(index).color
				}
			}

			background: Rectangle {
				color: parent.highlighted ? GuideThemeNS.Theme.getColor("setting_control_highlight") : "transparent"
				border.color: parent.highlighted ? GuideThemeNS.Theme.getColor("setting_control_border_highlight") : "transparent"
			}
		}
	}
}
