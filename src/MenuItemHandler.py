# Copyright (c) 2018 Aleksei Sasin
# The plugin is released under the terms of the LGPLv3 or higher.


class MenuItemHandler:

    def __init__(self, plugin_controller) -> None:
        self._plugin_controller = plugin_controller

    def sidebarMenuItemOnClickHander(self, kwargs) -> None:
        if "key" in kwargs:
            setting_key = kwargs["key"]
            self._plugin_controller.startWelcomeGuideAndSelectSetting(setting_key)
