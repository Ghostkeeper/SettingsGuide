//Copyright (C) 2016 Ultimaker B.V.
//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Controls 2.0

import UM 1.1 as UM
import Cura 1.0 as Cura

SettingItem {
	id: base

	contents: Rectangle {
		anchors.fill: parent
		color: UM.Theme.getColor("setting_control_disabled")
		border.width: UM.Theme.getSize("default_lining").width
		border.color: UM.Theme.getColor("setting_control_disabled_border")

		UM.RecolorImage
        {
			id: downArrow
			anchors {
	            right: parent.right
                rightMargin: UM.Theme.getSize("default_margin").width
				verticalCenter: parent.verticalCenter
			}

			source: UM.Theme.getIcon("arrow_bottom")
			width: UM.Theme.getSize("standard_arrow").width
			height: UM.Theme.getSize("standard_arrow").height
			sourceSize.width: width + 5 * screenScaleFactor
			sourceSize.height: width + 5 * screenScaleFactor

			color: UM.Theme.getColor("setting_control_button")
		}
		Rectangle {
			id: swatch
			height: Math.round(UM.Theme.getSize("setting_control").height / 2)
			width: height

			anchors {
				right: downArrow.left
				verticalCenter: parent.verticalCenter
				margins: Math.round(UM.Theme.getSize("default_margin").width / 4)
			}

			border.width: UM.Theme.getSize("default_lining").width
			border.color: UM.Theme.getColor("setting_control_disabled_border")
			radius: Math.round(width / 2)

			color: "white" //Always white because there is no extruder.
		}
	}
}