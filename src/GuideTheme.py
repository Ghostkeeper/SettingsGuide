# Copyright (c) 2018 Aleksei Sasin
# The plugin is released under the terms of the LGPLv3 or higher.

from PyQt5.QtCore import pyqtSlot, QObject
from PyQt5.QtGui import QColor

class GuideTheme(QObject):


    colors_dict = {
        "viewport_background": QColor(255, 255, 255, 255),
        "action_button_active_border": QColor(12, 169, 227, 255),

        "setting_control_border_highlight": QColor(12, 169, 227, 255),
        "setting_control_border": QColor(127, 127, 127, 255),
        "setting_control": QColor(255, 255, 255, 255),
        "setting_control_disabled": QColor(245, 245, 245, 255),
        "setting_control_text": QColor(27, 27, 27, 255),
        "setting_control_button": QColor(127, 127, 127, 255),
        "setting_control_button_hover": QColor(70, 84, 113, 255),
        "setting_control_disabled_border": QColor(127, 127, 127, 255),
        "setting_control_disabled_text": QColor(127, 127, 127, 255),
        "setting_category_text": QColor(31, 36, 39, 255),
        "setting_category_border": QColor(245, 245, 245, 255),
        "setting_category_active_hover_text": QColor(31, 36, 39, 255),
        "setting_category_active_text": QColor(31, 36, 39, 255),
        "setting_category": QColor(245, 245, 245, 255),
        "setting_category_hover_text": QColor(31, 36, 39, 255),
        "setting_category_hover_border": QColor(12, 159, 227, 255),
        "setting_category_hover": QColor(245, 245, 245, 255),
        "setting_category_active_border": QColor(245, 245, 245, 255),
        "setting_category_active_hover_border": QColor(12, 159, 227, 255),
        "setting_category_active": QColor(245, 245, 245, 255),
        "setting_category_active_hover": QColor(245, 245, 245, 255),
        "setting_unit": QColor(127, 127, 127, 255),
        "primary": QColor(12, 169, 227, 255),

        "scrollbar_background": QColor(255, 255, 255, 255),
        "scrollbar_handle": QColor(31, 36, 39, 255),
        "scrollbar_handle_hover": QColor(12, 159, 227, 255),
        "scrollbar_handle_down": QColor(12, 159, 227, 255),
    }

    def __init__(self, engine, parent = None):
        super().__init__(parent)

    @pyqtSlot(str, result = "QColor")
    def getColor(self, color):
        if color in self.colors_dict:
            return self.colors_dict[color]


        print("!!!!!!!!!!!!!!!!!!!!!  " + color)
        return QColor()

    ##  Get the singleton instance for this class.
    @classmethod
    def getInstance(cls, engine = None):
        # Note: Explicit use of class name to prevent issues with inheritance.
        if GuideTheme.__instance is None:
            GuideTheme.__instance = cls(engine)
        return GuideTheme.__instance

    __instance = None   # type: 'Theme'

def createTheme(engine, script_engine = None):
    return GuideTheme.getInstance(engine)

