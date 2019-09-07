#Copyright (C) 2018 Aleksei Sasin
#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

class MenuItemHandler:
	"""
	This class handles clicks when the user clicks on the context menu item in
	the settings list.

	An instance of this class is passed to the list model in QML's context menu.
	"""

	def __init__(self, plugin_controller) -> None:
		"""
		Constructs the menu item handler.
		:param plugin_controller: The main Settings Guide class so that we can
		open the guide.
		"""
		self._plugin_controller = plugin_controller

	def sidebarMenuItemOnClickHandler(self, kwargs) -> None:
		"""
		Triggered when the user clicks the menu item in the context menu in the
		settings list.
		:param kwargs: Keyword arguments that the QML menu provided. This
		function looks for the `key` keyword, which indicates the setting key
		that the user clicked on.
		"""
		if "key" in kwargs:
			article_key = kwargs["key"]
			self._plugin_controller.startWelcomeGuideAndSelectArticle(article_key)