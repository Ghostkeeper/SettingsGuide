#Copyright (C) 2018 Ultimaker B.V.
#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

from . import CuraSettingsGuide

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
