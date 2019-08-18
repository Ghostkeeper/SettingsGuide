//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import UM 1.3 as UM

Text {
	property var article_data
	text: article_data[0]
	wrapMode: Text.Wrap
	renderType: Text.NativeRendering
	font: UM.Theme.getFont("default")
	color: UM.Theme.getColor("text")

	onLinkActivated: {
		if(link in manager.allArticleIds) {
			manager.setSelectedArticleId(link);
		} else {
			Qt.openUrlExternally(link);
		}
	}

	//Use a different cursor when hovering over a link.
	MouseArea {
		anchors.fill: parent
		cursorShape: parent.hoveredLink ? Qt.PointingHandCursor : Qt.ArrowCursor
		acceptedButtons: Qt.NoButton //Don't capture button clicks. We want the link to do that.
	}
}