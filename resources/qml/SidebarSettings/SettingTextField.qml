// Copyright (c) 2017 Ultimaker B.V.
// Cura is released under the terms of the LGPLv3 or higher.

import QtQuick 2.7
import QtQuick.Controls 2.0

import UM 1.1 as UM
import GuideTheme 1.0 as GuideThemeNS

SettingItem
{
    id: base

    contents: Rectangle
    {
        id: control

        anchors.fill: parent

        border.width: Math.round(UM.Theme.getSize("default_lining").width)
        border.color:
        {
            return GuideThemeNS.Colors.getColor("setting_control_disabled_border")
        }

        color:
        {
            return GuideThemeNS.Colors.getColor("setting_control_disabled")
        }

        Label
        {
            anchors.right: parent.right
            anchors.rightMargin: Math.round(UM.Theme.getSize("setting_unit_margin").width)
            anchors.verticalCenter: parent.verticalCenter

            text: definition.unit
            renderType: Text.NativeRendering
            color: GuideThemeNS.Colors.getColor("setting_unit")
            font: UM.Theme.getFont("default")
        }
    }
}
