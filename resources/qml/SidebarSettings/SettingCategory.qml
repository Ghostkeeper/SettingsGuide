//Copyright (C) 2018 Ultimaker B.V.
//Copyright (C) 2019 Ghostkeeper
//This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
//This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
//You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import QtQuick 2.7
import QtQuick.Controls 2.0

import UM 1.1 as UM
import Cura 1.0 as Cura

Button {
	id: base
	anchors.left: parent.left
	anchors.right: parent.right
	anchors.leftMargin: UM.Theme.getSize("default_margin").width
	anchors.rightMargin: UM.Theme.getSize("default_margin").width
	background: Rectangle {
		implicitHeight: UM.Theme.getSize("section").height
		color: {
			if (base.color) {
				return base.color;
			} else if (!base.enabled) {
				return UM.Theme.getColor("setting_category_disabled");
			} else if (base.hovered && base.checkable && base.checked) {
				return UM.Theme.getColor("setting_category_active_hover");
			} else if (base.pressed || (base.checkable && base.checked)) {
				return UM.Theme.getColor("setting_category_active");
			} else if (base.hovered) {
				return UM.Theme.getColor("setting_category_hover");
			} else {
				return UM.Theme.getColor("setting_category");
			}
		}
		Behavior on color {
			ColorAnimation {
				duration: 50
			}
		}
		Rectangle {
			height: UM.Theme.getSize("default_lining").height
			width: parent.width
			anchors.bottom: parent.bottom
			color: {
				if (!base.enabled) {
					return UM.Theme.getColor("setting_category_disabled_border");
				} else if ((base.hovered || base.activeFocus) && base.checkable && base.checked) {
					return UM.Theme.getColor("setting_category_active_hover_border");
				} else if (base.pressed || (base.checkable && base.checked)) {
					return UM.Theme.getColor("setting_category_active_border");
				} else if (base.hovered || base.activeFocus) {
					return UM.Theme.getColor("setting_category_hover_border");
				} else {
					return UM.Theme.getColor("setting_category_border");
				}
			}
		}
	}

	signal showTooltip(string text)
	signal hideTooltip()
	signal contextMenuRequested()
	signal showAllHiddenInheritedSettings(string category_id)
	signal focusReceived()
	signal setActiveFocusToNextSetting(bool forward)

	property var focusItem: base

	contentItem: Item {
		anchors.fill: parent
		anchors.left: parent.left

		Label {
			anchors {
				left: parent.left
				leftMargin: 2 * UM.Theme.getSize("default_margin").width + UM.Theme.getSize("section_icon").width
				right: parent.right
				verticalCenter: parent.verticalCenter
			}
			text: definition.label
			renderType: Text.NativeRendering
			font: UM.Theme.getFont("default_bold")
			color: {
				if (!base.enabled) {
					return UM.Theme.getColor("setting_category_disabled_text");
				} else if ((base.hovered || base.activeFocus) && base.checkable && base.checked) {
					return UM.Theme.getColor("setting_category_active_hover_text");
				} else if (base.pressed || (base.checkable && base.checked)) {
					return UM.Theme.getColor("setting_category_active_text");
				} else if (base.hovered || base.activeFocus) {
					return UM.Theme.getColor("setting_category_hover_text");
				} else {
					return UM.Theme.getColor("setting_category_text");
				}
			}
			fontSizeMode: Text.HorizontalFit
			minimumPointSize: 8
		}
		UM.RecolorImage {
			id: category_arrow
			anchors.verticalCenter: parent.verticalCenter
			anchors.right: parent.right
			anchors.rightMargin: UM.Theme.getSize("default_margin").width
			width: UM.Theme.getSize("standard_arrow").width
			height: UM.Theme.getSize("standard_arrow").height
			sourceSize.width: width
			sourceSize.height: width
			color: {
				if (!base.enabled) {
					return UM.Theme.getColor("setting_category_disabled_text");
				} else if ((base.hovered || base.activeFocus) && base.checkable && base.checked) {
					return UM.Theme.getColor("setting_category_active_hover_text");
				} else if (base.pressed || (base.checkable && base.checked)) {
					return UM.Theme.getColor("setting_category_active_text");
				} else if (base.hovered || base.activeFocus) {
					return UM.Theme.getColor("setting_category_hover_text");
				} else {
					return UM.Theme.getColor("setting_category_text");
				}
			}
			source: base.checked ? UM.Theme.getIcon("arrow_bottom") : UM.Theme.getIcon("arrow_left")
		}
	}

	UM.RecolorImage {
		id: icon
		anchors.verticalCenter: parent.verticalCenter
		anchors.left: parent.left
		anchors.leftMargin: UM.Theme.getSize("default_margin").width
		color: {
			if (!base.enabled) {
				return UM.Theme.getColor("setting_category_disabled_text");
			} else if((base.hovered || base.activeFocus) && base.checkable && base.checked) {
				return UM.Theme.getColor("setting_category_active_hover_text");
			} else if(base.pressed || (base.checkable && base.checked)) {
				return UM.Theme.getColor("setting_category_active_text");
			} else if(base.hovered || base.activeFocus) {
				return UM.Theme.getColor("setting_category_hover_text");
			} else {
				return UM.Theme.getColor("setting_category_text");
			}
		}
		source: UM.Theme.getIcon(definition.icon)
		width: UM.Theme.getSize("section_icon").width
		height: UM.Theme.getSize("section_icon").height
		sourceSize.width: width + 15 * screenScaleFactor
		sourceSize.height: width + 15 * screenScaleFactor
	}

	checkable: true
	checked: definition.expanded

	onClicked: {
		if (definition.expanded) {
			settingDefinitionsModel.collapse(definition.key);
		} else {
			settingDefinitionsModel.expandRecursive(definition.key);
		}
		//Set focus so that tab navigation continues from this point on.
		//NB: This must be set AFTER collapsing/expanding the category so that the scroll position is correct.
		forceActiveFocus();
	}
	onActiveFocusChanged: {
		if(activeFocus) {
			base.focusReceived();
		}
	}

	Keys.onTabPressed: {
		base.setActiveFocusToNextSetting(true);
	}
	Keys.onBacktabPressed: {
		base.setActiveFocusToNextSetting(false);
	}
}
