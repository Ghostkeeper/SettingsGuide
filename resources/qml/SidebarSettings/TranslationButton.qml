//Copyright (C) 2020 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import UM 1.1 as UM

Item {
	UM.RecolorImage {
		color: UM.Theme.getColor("text")
		source: Qt.resolvedUrl("../../icons/translations.svg")
		anchors.centerIn: parent
		width: height
		height: parent.height - UM.Theme.getSize("narrow_margin").height * 2
	}
}