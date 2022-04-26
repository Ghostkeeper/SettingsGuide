//Copyright (C) 2022 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Controls 2.0

import UM 1.5 as UM

SettingItem {
	contents: UM.UnderlineBackground {
		anchors.fill: parent

		liningColor: UM.Theme.getColor("text_field_border_disabled")
		color: UM.Theme.getColor("text_field")

		UM.Label {
			anchors {
				left: parent.left
				leftMargin: UM.Theme.getSize("setting_unit_margin").width
				right: parent.right
				rightMargin: UM.Theme.getSize("setting_unit_margin").width
				verticalCenter: parent.verticalCenter
			}

			text: definition.unit
			horizontalAlignment: Text.AlignRight //TODO: Not consistent with real layout with right-to-left languages. We don't have a TextInput to take the correct alignment from.
			textFormat: Text.PlainText
			color: UM.Theme.getColor("setting_unit")
		}
	}
}