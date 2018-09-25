# Copyright (c) 2018 Ultimaker B.V.
# Cura is released under the terms of the LGPLv3 or higher.

from .src import CuraSettingsGuide

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("cura")


def getMetaData():
    return {
        "view": {
            "name": i18n_catalog.i18nc("@item:inmenu", "Cura Settings Guide"),
            "weight": 0
        }
    }


def register(app):
    return {"extension": CuraSettingsGuide.CuraSettingsGuide()}
