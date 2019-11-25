//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Controls 1.2
import UM 1.3 as UM

//Draws a checkbox that the user can check or uncheck.
//The checkbox is linked to a preference value. Clicking it will change the
//preference.

Row {
	property var article_data

	CheckBox {
		text: article_data[1]
		style: UM.Theme.styles.checkbox

		checked: UM.Preferences.getValue(article_data[0])
		onClicked: UM.Preferences.setValue(article_data[0], checked)
	}
}