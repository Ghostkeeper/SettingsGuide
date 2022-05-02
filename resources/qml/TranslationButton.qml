//Copyright (C) 2020 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Controls 2.0

import UM 1.1 as UM

MouseArea {
	property string article_id

	onClicked: languagesMenu.popup()
	visible: manager.language_list(article_id).length > 1
	hoverEnabled: true
	ToolTip.visible: containsMouse
	ToolTip.delay: 500
	ToolTip.timeout: 5000
	ToolTip.text: qsTr("Translations are available.")

	UM.ColorImage {
		color: UM.Theme.getColor("text")
		source: Qt.resolvedUrl("../icons/translations.svg")
		anchors.centerIn: parent
		width: height
		height: parent.height - UM.Theme.getSize("narrow_margin").height * 2
	}

	Menu {
		id: languagesMenu
		Instantiator {
			model: manager.language_list(article_id)

			MenuItem {
				text: code_to_language(modelData.toString())
				onTriggered: manager.set_language(modelData.toString())
			}
			onObjectAdded: function(index, object) { languagesMenu.insertItem(index, object); }
			onObjectRemoved: function(index, object) { languagesMenu.removeItem(object); }
		}
	}

	function code_to_language(code) {
		var language_mapping = {
			"cs_CZ": "Čeština",
			"de_DE": "Deutsch",
			"en_7S": "Pirate",
			"en_US": "English",
			"es_ES": "Español",
			"fi_FI": "Suomi",
			"fr_FR": "Français",
			"it_IT": "Italiano",
			"ja_JP": "日本語",
			"ko_KR": "한국어",
			"nl_NL": "Nederlands",
			"pl_PL": "Polski",
			"pt_BR": "Português do Brasil",
			"pt_PT": "Português",
			"ru_RU": "Русский",
			"tr_TR": "Türkçe",
			"zh_CN": "简体中文",
			"zh_TW": "正體字"
		};
		return language_mapping[code];
	}
}