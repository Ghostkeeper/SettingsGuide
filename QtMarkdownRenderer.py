#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

from .Mistune import mistune

class QtMarkdownRenderer(mistune.Renderer):
	"""
	Specialises the Mistune renderer in order to be better compatible with Qt's
	rich text.

	Mistune converts Markdown into HTML. However its choice for the HTML
	elements to use is not always supported by the limited HTML subset that Qt
	can display with its "rich text" rendering. This class makes sure that the
	supported subset of HTML is used.
	"""

	def emphasis(self, text: str) -> str:
		"""
		Rendering *emphasis* text.

		By default, Mistune emphasises text using the <em> tag. Even though the
		QML documentation claims that <em> behaves the same as <i>,
		experimentally it seems that <em> doesn't work while <i> does.
		:param text: The emphasised text.
		:return: That text in italics.
		"""
		return "<i>{text}</i>".format(text=text)