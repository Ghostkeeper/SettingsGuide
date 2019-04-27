//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

import UM 1.2 as UM
import GuideTheme 1.0 as GuideThemeNS

Rectangle {
	id: emptyTemplate
	color: GuideThemeNS.Theme.getColor("viewport_background")

	Image {
		id: author
		width: {
			var ratio = Math.max( sourceSize.width / 700, sourceSize.height / 400)
			var new_value = sourceSize.width
			if(ratio > 1) {
				new_value = sourceSize.width / ratio
			}

			return new_value * screenScaleFactor
		}
		height: {
			var ratio = Math.max( sourceSize.width / 700, sourceSize.height / 400)
			var new_value = sourceSize.height
			if(ratio > 1) {
				new_value = sourceSize.height / ratio
			}

			return new_value * screenScaleFactor
		}
		anchors.horizontalCenter: parent.horizontalCenter
		anchors.verticalCenter: parent.verticalCenter
		source: "data:image/png;base64," + CuraSettingsGuide.getCreatedByImage()
	}

	Text {
		text: "Created By: Terri-Ann dela Cruz and Aleksei Sasin"
		color: "black"
		font.pixelSize: 20
		anchors.horizontalCenter: parent.horizontalCenter
		anchors.top: author.bottom
		anchors.topMargin: 20
		opacity: 0.7
	}
}
