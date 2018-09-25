# Copyright (c) 2018 Aleksei Sasin
# The plugin is released under the terms of the LGPLv3 or higher.

from UM.Settings.Models.SettingDefinitionsModel import SettingDefinitionsModel


class SettingsModel(SettingDefinitionsModel):

    def __init__(self, parent = None, *args, **kwargs) -> None:
        super().__init__(parent = parent, *args, **kwargs)
