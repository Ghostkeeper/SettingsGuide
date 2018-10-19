import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.2

import UM 1.2 as UM
import Cura 1.0 as Cura

import CuraSettingsGuide 1.0 as CuraSettingsGuideNS
import GuideTheme 1.0 as GuideThemeNS

Rectangle
{
    id: rightSideItem
    width: UM.Theme.getSize("sidebar").width;

    property var listViewLastSelectedItem: undefined // keeps reference to the last item in the list. After item change
                                                     // in the list, the previous selection should be removed
    property var first_start: true
    property var temp_setting_id: ""

    // The function hides highlighted area from previous item and highlights a new selected item
    function setSelectedItemInSettingListView(setting_id)
    {
        if (listViewLastSelectedItem != undefined)
        {
            listViewLastSelectedItem.hideHighlightArea()
        }

        var temp_index = contents.model.getIndex(setting_id)

        // If returned value is -1, then ListView with settings is not yet ready, call one more time same function with small delay
        if (temp_index == -1 && first_start == true)
        {
            first_start = false
            temp_setting_id = setting_id
            checkSelectedItemForInitialStartTimer.restart()
            return
        }

        contents.currentIndex = temp_index
        listViewLastSelectedItem = contents.currentItem.item

        // Need to check because at first the items in Listview might be not initialized,
        // for this reason is used timer
        checkSelectedSettingItemStatus()
    }

    function resetSelectedItemInSettingListView()
    {
        if (listViewLastSelectedItem != undefined)
        {
            listViewLastSelectedItem.hideHighlightArea()
            listViewLastSelectedItem = undefined
        }
    }

    property var last_setting_id: ""

    // After collapsing and expanding the selected item needs to be highilghted again.
    // This is a tricky of assigning because of Loader asynchronous, we need perform check only after the Item is onCompleted:
    property var onCompleteItemCallBack: function(setting_item)
    {
        // Can e selected only one item
        if (setting_item.setting_item_key == last_setting_id && setting_item.isSelected == false)
        {
            //we need keep track of selected item to able unselect it
            listViewLastSelectedItem = setting_item
            setting_item.showHighlightArea()
        }
    }

    property int checkCounter: 0
    function checkSelectedSettingItemStatus ()
    {
        // Check maximum 10 times
        if (listViewLastSelectedItem == null && checkCounter < 10)
        {
             checkSelectedSettingItemStatusTimer.restart()
             checkCounter++
        }
        else
        {
            listViewLastSelectedItem.showHighlightArea()
        }
    }

    function checkSelectedItemForInitialStart()
    {
        setSelectedItemInSettingListView(temp_setting_id)
    }

    Timer
    {
        id: checkSelectedSettingItemStatusTimer
        onTriggered: checkSelectedSettingItemStatus()
        interval: 500
        running: false
        repeat: false
    }

    Timer
    {
        id: checkSelectedItemForInitialStartTimer
        onTriggered: checkSelectedItemForInitialStart()
        interval: 1000
        running: false
        repeat: false
    }

    property bool findingSettings

    Rectangle
    {
        id: filterContainer

        border.width: Math.round(UM.Theme.getSize("default_lining").width)
        border.color:
        {
            if (hoverMouseArea.containsMouse || clearFilterButton.containsMouse)
            {
                return GuideThemeNS.Colors.getColor("setting_control_border_highlight");
            }
            else
            {
                return GuideThemeNS.Colors.getColor("setting_control_border");
            }
        }

        color: GuideThemeNS.Colors.getColor("setting_control")

        anchors
        {
            top: parent.top
            topMargin: UM.Theme.getSize("sidebar_margin").height
            left: parent.left
            leftMargin: UM.Theme.getSize("sidebar_margin").width
            right: parent.right
            rightMargin: Math.floor(UM.Theme.getSize("default_margin").width / 2)
        }
        height: UM.Theme.getSize("setting_control").height
        width: rightSideItem.width
        Behavior on height { NumberAnimation { duration: 100 } }

        Timer
        {
            id: settingsSearchTimer
            onTriggered: filter.editingFinished()
            interval: 500
            running: false
            repeat: false
        }

        TextField
        {
            id: filter;
            height: parent.height
            anchors.left: filterContainer.left
            anchors.right: filterContainer.right
            anchors.rightMargin: Math.round(UM.Theme.getSize("sidebar_margin").width)

            placeholderText: catalog.i18nc("@label:textbox", "Search...")

            style: TextFieldStyle
            {
                textColor: GuideThemeNS.Colors.getColor("setting_control_text");
                placeholderTextColor: GuideThemeNS.Colors.getColor("setting_control_text")
                font: UM.Theme.getFont("default");
                background: Item {}
            }

            property var expandedCategories
            property bool lastFindingSettings: false

            onTextChanged:
            {
                settingsSearchTimer.restart()
            }

            property var temp_model: ""
            onEditingFinished:
            {

                if (text.toLowerCase() == "createdby")
                {
                    temp_model = contents.model
                    contents.model = createdBy
                    return
                }
                if (temp_model != "")
                {
                    contents.model = temp_model
                    temp_model = ""
                }

                definitionsModel.filter = {"i18n_label": "*" + text};

                findingSettings = (text.length > 0);
                if (findingSettings != lastFindingSettings)
                {
                    updateDefinitionModel();
                    lastFindingSettings = findingSettings;
                }
            }

            Keys.onEscapePressed:
            {
                filter.text = "";
            }

            function updateDefinitionModel()
            {
                if (findingSettings)
                {
                    expandedCategories = definitionsModel.expanded.slice();
                    definitionsModel.expanded = [""]; // keep categories closed while to prevent render while making settings visible one by one
                    definitionsModel.showAncestors = true;
                    definitionsModel.showAll = true;
                    definitionsModel.expanded = ["*"];
                }
                else
                {
                    if (expandedCategories)
                    {
                        definitionsModel.expanded = expandedCategories;
                    }
                    definitionsModel.showAncestors = false;
                    definitionsModel.showAll = true;
                }
            }
        }

        // Custom Item which is used only for createdBy setting
        ListModel {id: createdBy; ListElement {type: "createdBy"; key: "createdBy"; label: "Created By"; depth: 2}}

        MouseArea
        {
            id: hoverMouseArea
            anchors.fill: parent
            hoverEnabled: true
            acceptedButtons: Qt.NoButton
            cursorShape: Qt.IBeamCursor
        }

        UM.SimpleButton
        {
            id: clearFilterButton
            iconSource: UM.Theme.getIcon("cross1")
            visible: findingSettings

            height: Math.round(parent.height * 0.4)
            width: visible ? height : 0

            anchors.verticalCenter: parent.verticalCenter
            anchors.right: parent.right
            anchors.rightMargin: UM.Theme.getSize("default_margin").width

            color: GuideThemeNS.Colors.getColor("setting_control_button")
            hoverColor: GuideThemeNS.Colors.getColor("setting_control_button_hover")

            onClicked:
            {
                filter.text = "";
                filter.forceActiveFocus();
            }
        }
    }

    ScrollView
    {
        id: scrollView

        anchors.top: filterContainer.bottom;
        anchors.bottom: parent.bottom;
        anchors.right: parent.right;
        anchors.left: parent.left;
        anchors.topMargin: filterContainer.visible ? UM.Theme.getSize("sidebar_margin").height : 0
        Behavior on anchors.topMargin { NumberAnimation { duration: 100 } }
        style: scrollview_settings_guide
        flickableItem.flickableDirection: Flickable.VerticalFlick;
        __wheelAreaScrollSpeed: 75; // Scroll three lines in one scroll event

        ListView
        {
            id: contents
            spacing: Math.round(UM.Theme.getSize("default_lining").height);
            cacheBuffer: 1000000;   // Set a large cache to effectively just cache every list item.

            height: parent.height
            currentIndex: -1

            model: CuraSettingsGuideNS.SettingsModel
            {
                id: definitionsModel;
                containerId: Cura.MachineManager.activeDefinitionId
                showAll: true
                exclude: ["machine_settings", "command_line_settings", "infill_mesh", "infill_mesh_order", "cutting_mesh", "support_mesh", "anti_overhang_mesh"] // TODO: infill_mesh settigns are excluded hardcoded, but should be based on the fact that settable_globally, settable_per_meshgroup and settable_per_extruder are false.
                expanded: CuraApplication.expandedCategories
            }

            delegate:Loader
            {
                id: settingLoader

                width: parent.width
                height: model.type != undefined ? UM.Theme.getSize("section").height : 0;

                property var definition: model
                property var settingDefinitionsModel: definitionsModel
                property var propertyProvider: provider
                property var globalPropertyProvider: inheritStackProvider
                property var externalResetHandler: false

                //Qt5.4.2 and earlier has a bug where this causes a crash: https://bugreports.qt.io/browse/QTBUG-35989
                //In addition, while it works for 5.5 and higher, the ordering of the actual combo box drop down changes,
                //causing nasty issues when selecting different options. So disable asynchronous loading of enum type completely.
                asynchronous: model.type != "enum" && model.type != "extruder" && model.type != "optional_extruder"
                active: model.type != undefined

                source:
                {
                    switch (model.type)
                    {
                        case "int":
                            return Qt.resolvedUrl("SidebarSettings/SettingTextField.qml")
                        case "[int]":
                            return Qt.resolvedUrl("SidebarSettings/SettingTextField.qml")
                        case "float":
                            return Qt.resolvedUrl("SidebarSettings/SettingTextField.qml")
                        case "enum":
                            return Qt.resolvedUrl("SidebarSettings/SettingComboBox.qml")
                        case "extruder":
                            return Qt.resolvedUrl("SidebarSettings/SettingExtruder.qml")
                        case "bool":
                            return Qt.resolvedUrl("SidebarSettings/SettingCheckBox.qml")
                        case "str":
                            return Qt.resolvedUrl("SidebarSettings/SettingTextField.qml")
                        case "category":
                            return Qt.resolvedUrl("SidebarSettings/SettingCategory.qml")
                        case "optional_extruder":
                            return Qt.resolvedUrl("SidebarSettings/SettingOptionalExtruder.qml")
                        default:
                            return Qt.resolvedUrl("SidebarSettings/SettingUnknown.qml")
                    }
                }

                MouseArea
                {
                    id: mouse_area1
                    anchors.fill: parent
                    propagateComposedEvents: true
                    hoverEnabled: true
                    onClicked:
                    {
                        rightSideItem.last_setting_id = model.key
                        CuraSettingsGuide.setSelectedSetting(model.key)
                    }
                }
            }
            UM.SettingPropertyProvider
            {
                id: inheritStackProvider
                containerStackId: Cura.MachineManager.activeMachineId
            }

            UM.SettingPropertyProvider
            {
                id: provider
                containerStackId: Cura.MachineManager.activeMachineId
            }
        }
    }

    property Component scrollview_settings_guide: Component
    {
        ScrollViewStyle {
            decrementControl: Item { }
            incrementControl: Item { }

            transientScrollBars: false

            scrollBarBackground: Rectangle {
                implicitWidth: UM.Theme.getSize("scrollbar").width
                radius: Math.round(implicitWidth / 2)
                color: GuideThemeNS.Colors.getColor("scrollbar_background");
            }

            handle: Rectangle {
                id: scrollViewHandle
                implicitWidth: UM.Theme.getSize("scrollbar").width;
                radius: Math.round(implicitWidth / 2)

                color: styleData.pressed ? GuideThemeNS.Colors.getColor("scrollbar_handle_down") : styleData.hovered ? GuideThemeNS.Colors.getColor("scrollbar_handle_hover") : GuideThemeNS.Colors.getColor("scrollbar_handle");
                Behavior on color { ColorAnimation { duration: 50; } }
            }
        }
    }
}
