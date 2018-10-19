import QtQuick 2.7
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

import UM 1.2 as UM
import GuideTheme 1.0 as GuideThemeNS

Rectangle
{
    id: emptyTemplate
    color: GuideThemeNS.Colors.getColor("viewport_background")

    Image
    {
        id: author
        width:
        {
            var ratio = Math.max( sourceSize.width / 700, sourceSize.height / 400)
            var new_value = sourceSize.width
            if(ratio > 1)
                new_value =  sourceSize.width / ratio

            return new_value * screenScaleFactor

        }
        height:
        {
            var ratio = Math.max( sourceSize.width / 700, sourceSize.height / 400)
            var new_value = sourceSize.height
            if(ratio > 1)
                new_value =  sourceSize.height / ratio

            return new_value * screenScaleFactor
        }
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        source: "data:image/png;base64," + CuraSettingsGuide.getCreatedByImage()
    }

    Text
    {
        text: "Created By: Terri-Ann dela Cruz and Aleksei Sasin"
        color: "black"
        font.pixelSize: 20
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: author.bottom
        anchors.topMargin: 20
        opacity: 0.7
    }
}
