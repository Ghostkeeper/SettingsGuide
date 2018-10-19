// Copyright (c) 2015 Ultimaker B.V.
// Uranium is released under the terms of the LGPLv3 or higher.

import QtQuick 2.7
import QtQuick.Controls 2.0

import UM 1.2 as UM
import GuideTheme 1.0 as GuideThemeNS

SettingItem
{
    contents: Label
    {
        anchors.fill: parent
        text: propertyProvider.properties.value + " " + unit
        renderType: Text.NativeRendering
        font: UM.Theme.getFont("default")
        color: GuideThemeNS.Colors.getColor("text")
        verticalAlignment: Text.AlignVCenter
    }
}
