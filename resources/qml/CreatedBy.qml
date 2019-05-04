//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

import UM 1.2 as UM

Item {
	Item {
		anchors.centerIn: parent
		width: childrenRect.width
		height: childrenRect.height
		Image {
			id: author
			width: 500 * screenScaleFactor
			fillMode: Image.PreserveAspectFit
			source: "../icons/created_by.jpg"
		}

		Text {
			text: "Created By: Terri-Ann dela Cruz, Aleksei Sasin and Ghostkeeper"
			color: UM.Theme.getColor("text")
			font.pixelSize: 20
			anchors.horizontalCenter: author.horizontalCenter
			anchors.top: author.bottom
			anchors.topMargin: 20
		}
	}
}