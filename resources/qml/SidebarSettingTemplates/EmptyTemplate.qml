import QtQuick 2.7
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

import UM 1.2 as UM


Rectangle
{
    id: empty_template
    color: UM.Theme.getColor("viewport_background")

    Text
    {
        text: "EMPTY"
        color: "black"
        font.pixelSize: 80
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        //rotation: -45
        opacity: 0.3
    }
}
