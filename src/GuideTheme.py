# Copyright (c) 2018 Aleksei Sasin
# The plugin is released under the terms of the LGPLv3 or higher.

from PyQt5.QtCore import pyqtSlot, QObject, QSizeF, QCoreApplication
from PyQt5.QtGui import QColor, QFontMetrics, QFont

class GuideTheme(QObject):

    sizes_json = {
        "sidebar_margin": [1.71, 1.43],
        "sidebar": [35.0, 10.0],
        "setting_control": [10.0, 2.0],
        "scrollbar": [0.75, 0.5],
        "section": [0.0, 2.2],
        "standard_arrow": [0.8, 0.8],
        "setting_unit_margin": [0.5, 0.5],
        "section_icon_column": [2.8, 0.0],
        "setting_control_depth_margin": [1.4, 0.0],
        "default_lining": [0.08, 0.08],
        "default_margin": [1.0, 1.0],
        "section_icon": [1.6, 1.6],
    }

    fonts_json = {
        "setting_category": {
            "size": 1.15,
            "weight": 63,
        },
        "default": {
            "size": 1.0,
            "weight": 50,
            "family": "Noto Sans"
        },
        "default_bold": {
            "size": 1.0,
            "weight": 63,
            "family": "Noto Sans"
        },
        "default_italic": {
            "size": 1.15,
            "weight": 50,
            "italic": "true",
            "family": "Noto Sans"
        },
        "large": {
            "size": 1.35,
            "weight": 63,
            "family": "Noto Sans"
        }
    }

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

    sizes_dict = {}

    fonts_dict = {}

    def __init__(self, engine, parent = None) -> None:
        super().__init__(parent)

        self._em_height = int(QFontMetrics(QCoreApplication.instance().font()).ascent())
        self._em_width = self._em_height

        self._initSizes()
        self._initFonts()


    def _initSizes(self) -> None:
        for key, value in self.sizes_json.items():
            new_size = QSizeF()
            new_size.setWidth(round(value[0] * self._em_width))
            new_size.setHeight(round(value[1] * self._em_height))
            self.sizes_dict[key] = new_size

    def _initFonts(self) -> None:
        system_font_size = QCoreApplication.instance().font().pointSize()
        for name, font in self.fonts_json.items():
            f = QFont()
            f.setFamily(font.get("family", QCoreApplication.instance().font().family()))

            if font.get("bold"):
                f.setBold(font.get("bold", False))
            else:
                f.setWeight(font.get("weight", 50))

            f.setLetterSpacing(QFont.AbsoluteSpacing, font.get("letterSpacing", 0))
            f.setItalic(bool(font.get("italic", False)))
            f.setPointSize(int(font.get("size", 1) * system_font_size))
            f.setCapitalization(QFont.AllUppercase if font.get("capitalize", False) else QFont.MixedCase)

            self.fonts_dict[name] = f

    @pyqtSlot(str, result = "QColor")
    def getColor(self, color):
        if color in self.colors_dict:
            return self.colors_dict[color]

        print("NO COLOR: {0}".format(color))
        return QColor()

    @pyqtSlot(str, result="QSizeF")
    def getSize(self, size):
        if size in self.sizes_dict:
            return self.sizes_dict[size]

        print("NO SIZE: {0}".format(size))
        return QSizeF()

    @pyqtSlot(str, result="QFont")
    def getFont(self, font_name):
        if font_name in self.fonts_dict:
            return self.fonts_dict[font_name]

        print("NO FONT: {0}".format(font_name))
        return QFont()

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

