//Copyright (C) 2018 Ultimaker B.V.
//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Layouts 1.2
import QtQuick.Controls 2.0

import UM 1.2 as UM
import GuideTheme 1.0 as GuideThemeNS

SettingItem
{
	id: base
	//property var focusItem: control

	contents: MouseArea
	{
		id: control
		anchors.fill: parent
		hoverEnabled: true

		property bool checked: false

		Rectangle
		{
			anchors
			{
				top: parent.top
				bottom: parent.bottom
				left: parent.left
			}
			width: height

			color:
			{
				if(!enabled)
				{
					return GuideThemeNS.Theme.getColor("setting_control_disabled")
				}
				if(control.containsMouse || control.activeFocus)
				{
					return GuideThemeNS.Theme.getColor("setting_control_highlight")
				}
				return GuideThemeNS.Theme.getColor("setting_control")
			}

			border.width: GuideThemeNS.Theme.getSize("default_lining").width
			border.color:
			{
				if(!enabled)
				{
					return GuideThemeNS.Theme.getColor("setting_control_disabled_border")
				}
				if(control.containsMouse || control.activeFocus)
				{
					return GuideThemeNS.Theme.getColor("setting_control_border_highlight")
				}
				return GuideThemeNS.Theme.getColor("setting_control_border")
			}
		}
	}
}
