// Copyright (c) 2018 Ultimaker B.V.
// Cura is released under the terms of the LGPLv3 or higher.

import QtQuick 2.7
import QtQuick.Layouts 1.2
import QtQuick.Controls 2.0

import UM 1.1 as UM
import Cura 1.0 as Cura
import GuideTheme 1.0 as GuideThemeNS

//import "."

Rectangle {
    id: base;

    height: GuideThemeNS.Theme.getSize("section").height

    property alias contents: controlContainer.children
    property alias hovered: mouse.containsMouse
    property var doDepthIndentation: true
    property var doQualityUserSettingEmphasis: true


    // Create properties to put property provider stuff in (bindings break in qt 5.5.1 otherwise)
    //property var state: propertyProvider.properties.state
    // There is no resolve property if there is only one stack.
    //property var resolve: Cura.MachineManager.activeStackId != Cura.MachineManager.activeMachineId ? propertyProvider.properties.resolve : "None"
    property var stackLevels: propertyProvider.stackLevels
    property var stackLevel: stackLevels[0]


    property bool isSelected: false
    property string setting_item_key: definition.key

    function showHighlightArea()
    {
        isSelected = true
        highlightRectangle.opacity = 0.1
        selectRectangle.visible = true
        selectImage.visible = true
    }

    function hideHighlightArea()
    {
        isSelected = false
        highlightRectangle.opacity = 0.0
        selectRectangle.visible = false
        selectImage.visible = false
    }


    MouseArea
    {
        id: mouse;
        anchors.fill: parent;
        acceptedButtons: Qt.RightButton;
        hoverEnabled: true;

        Image {
            id: selectImage
            height: 20
            width: 20
            visible: false
            anchors.verticalCenter: parent.verticalCenter
            source: Qt.resolvedUrl("../../icons/arrow.png")
        }

        Rectangle
        {
            id: selectRectangle
            z: 1
            color: "transparent"
            visible: false
            anchors.fill: parent;
            anchors.leftMargin : 22
            anchors.rightMargin : 22
            border.color: GuideThemeNS.Theme.getColor("action_button_active_border")
            border.width: 1
        }

        Rectangle
        {
            id: highlightRectangle
            z: 1
            anchors.fill: parent;
            anchors.leftMargin : 22
            anchors.rightMargin : 22
            opacity: 0.0
            color: GuideThemeNS.Theme.getColor("primary")
        }

        Label
        {
            id: label;

            anchors.left: parent.left;
            anchors.leftMargin: doDepthIndentation ? Math.round((GuideThemeNS.Theme.getSize("section_icon_column").width + 5) + ((definition.depth - 1) * GuideThemeNS.Theme.getSize("setting_control_depth_margin").width)) : 0
            anchors.verticalCenter: parent.verticalCenter

            text: definition.label
            elide: Text.ElideMiddle;
            renderType: Text.NativeRendering

            color: GuideThemeNS.Theme.getColor("setting_control_text");
            opacity: (definition.visible) ? 1 : 0.5
            // emphasize the setting if it has a value in the user or quality profile
            font: base.doQualityUserSettingEmphasis && base.stackLevel != undefined && base.stackLevel <= 1 ? GuideThemeNS.Theme.getFont("default_italic") : GuideThemeNS.Theme.getFont("default")
        }

        Item
        {
            id: controlContainer;

            enabled: propertyProvider.isValueUsed

            anchors.right: parent.right;
            anchors.rightMargin: GuideThemeNS.Theme.getSize("sidebar_margin").width
            anchors.verticalCenter: parent.verticalCenter;
            width: GuideThemeNS.Theme.getSize("setting_control").width;
            height: GuideThemeNS.Theme.getSize("setting_control").height
        }

        onEntered:
        {
            if(!isSelected)
                highlightRectangle.opacity = 0.1
        }
        onExited:
        {
            if(!isSelected)
                highlightRectangle.opacity = 0.0
        }
    }

    UM.I18nCatalog { id: catalog; name: "cura" }

    Component.onCompleted:
    {
        onCompleteItemCallBack(base)
    }
}
