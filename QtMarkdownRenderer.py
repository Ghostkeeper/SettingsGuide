#Copyright (C) 2020 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

from .Mistune import mistune  # Extending from this library's renderer.
import os.path  # To fix the source paths for images.
import PyQt5.QtCore  # To fix the source paths for images using QUrl.
import re  # To find parts of the conditional syntax.
import UM.Application  # To get the application version.
import UM.Logger  # To log warnings if parsing went wrong.
import UM.Qt.Bindings.Theme  # To get the correct hyperlink colour from the theme.
import UM.Version  # To compare version numbers for conditional content.

class QtMarkdownRenderer(mistune.Renderer):
	"""
	Specialises the Mistune renderer in order to be better compatible with Qt's
	rich text while degrading gracefully with Github's renderer.

	Mistune converts Markdown into HTML. However its choice for the HTML
	elements to use is not always supported by the limited HTML subset that Qt
	can display with its "rich text" rendering. This class makes sure that the
	supported subset of HTML is used.

	This renderer makes sure that the Markdown that gets interpreted by the
	renderer displays correctly on a conventional Markdown parser such as that
	of Github.
	"""

	def __init__(self, images_path):
		"""
		Creates a renderer with a certain relative path for resources.
		:param images_path: The path to which relative paths should be
		dereferenced.
		"""
		super().__init__()
		self._images_path = images_path

	def link(self, link, title, text):
		"""
		Renders a given link with content and title.

		This gives the link the correct colour, since Qt's linkColor property
		seems to be completely broken. This wraps the link text with a <font>
		tag that adjusts its colour.
		:param link: The URL to link towards.
		:param title: The description text for the link. This is not shown by Qt
		though, so in the end the argument will not be used.
		:param text: The text to display (in the correct colour).
		:return: HTML for Qt's Rich Text to display the link.
		"""
		link = mistune.escape_link(link)
		link_colour = UM.Qt.Bindings.Theme.Theme.getInstance().getColor("text_link").name()

		if "://" not in link and link.endswith(".md"):  # Link to a different article.
			link = os.path.join(self._images_path, link)

		if not title:
			return "<a href=\"{link}\"><font color=\"{colour}\">{text}</font></a>".format(colour=link_colour, link=link, text=text)
		title = mistune.escape(title, quote=True)
		return "<a href=\"{link}\" title=\"{title}\"><font color=\"{colour}\">{text}</font></a>".format(colour=link_colour, title=title, link=link, text=text)

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

	def image(self, src, title, alt_text):
		"""
		Renders an image with a title (normally displayed on hover) and an alt-
		text that gets displayed if the image is not available.
		:param src: The path to the image, relative to the "articles" directory.
		:param title: A text to display with the image. This gets ignored
		because Qt's Rich Text doesn't support it.
		:param alt_text: A text to display in case the image can't get loaded.
		This gets ignored because Qt's Rich Text doesn't support it.
		:return: HTML for Qt's Rich Text to display the image.
		"""
		image_full_path = os.path.join(self._images_path, src)
		image_url = PyQt5.QtCore.QUrl.fromLocalFile(image_full_path).url()
		margin = UM.Qt.Bindings.Theme.Theme.getInstance().getSize("default_margin").width()
		width = UM.Qt.Bindings.Theme.Theme.getInstance().getSize("tooltip").width() / 3 - margin * 2  # Fit 3 images in the width.
		return "<img src=\"{image_url}\" width=\"{width}\" />".format(image_url=image_url, width=width)

	def inline_html(self, html):
		"""
		This renders a piece of inline HTML.

		HTML is not really supported here. However we're using this syntax to
		implement our own conditional Markdown syntax, which renders only if a
		certain condition is met. This conditional syntax is designed to degrade
		 gracefully when rendered in a conventional Markdown renderer such as
		 the one on github.com.

		There are two possible syntax variations for conditional content. Both
		will look exactly the same in this plug-in, but look differently when
		rendered with a conventional renderer.
		* Content that gets hidden with a conventional renderer looks like this:
		`<!--if variable == value:conditional content-->`
		* Content that gets shown in a conventional renderer looks like this:
		`<!--if variable == value -->conditional content<!--endif-->`

		This syntax contains a condition, in the above example:
		`variable == true`. This condition consists of a variable, a comparator
		and a value. The conditional content is shown only if the condition is
		met. For instance, you could have a condition such as:
		`cura_version < 4.4` which would cause the conditional content to draw
		only if the user is using a Cura version earlier than 4.4.
		:param html: The HTML tag that was found in the article.
		:return: What should be shown in the article.
		"""
		return self.any_html(html)

	def block_html(self, html):
		"""
		This renders a piece of HTML on a separate block.

		HTML is not really supported here. However we're using this syntax to
		implement our own conditional Markdown syntax, which renders only if a
		certain condition is met. This conditional syntax is designed to degrade
		 gracefully when rendered in a conventional Markdown renderer such as
		 the one on github.com.

		There are two possible syntax variations for conditional content. Both
		will look exactly the same in this plug-in, but look differently when
		rendered with a conventional renderer.
		* Content that gets hidden with a conventional renderer looks like this:
		`<!--if variable == value:conditional content-->`
		* Content that gets shown in a conventional renderer looks like this:
		`<!--if variable == value -->conditional content<!--endif-->`

		This syntax contains a condition, in the above example:
		`variable == true`. This condition consists of a variable, a comparator
		and a value. The conditional content is shown only if the condition is
		met. For instance, you could have a condition such as:
		`cura_version < 4.4` which would cause the conditional content to draw
		only if the user is using a Cura version earlier than 4.4.
		:param html: The HTML tag that was found in the article.
		:return: What should be shown in the article.
		"""
		return self.any_html(html)

	def any_html(self, html):
		"""
		Helper function to parse HTML.

		In most cases this will do nothing to the text. However if a conditional
		tag is found we'll remove the text or replace it, depending on whether
		the condition is met.
		:param html: The HTML content found in the article.
		:return: The rich text to draw instead of the HTML tag.
		"""
		result = ""

		# First try finding the conditional content that gets hidden by conventional renderers.
		hidden_pattern = r"<!--if\s+([A-Za-z0-9_]+\s*(<=|==|!=|>=|<|>)\s*[^-^:]+?(\s+and\s+[A-Za-z0-9_]+\s*(<=|==|!=|>=|<|>)\s*[^-^:]+?)*)\s*:(.*?)-->"
		for match in re.finditer(hidden_pattern, html, flags=re.DOTALL):
			condition = match.group(1)
			content = match.group(5)
			if self.condition_met(condition):
				result += content
			else:
				pass

		return result

	def condition_met(self, condition):
		"""
		Checks if a piece of conditional Markdown should be shown or not.
		:param condition: The condition under which the content gets shown, as a
		string. This needs to be formatted as a series of variable checks of the
		form `variable <= value` (with any comparative operator). If there are
		multiple of these checks (separated with `and`) then all of them must
		hold for the condition to be met.
		:return: `True` if the condition is met, or `False` if it is not met.
		"""
		check_pattern = r"([A-Za-z09_]+)\s*(<=|==|!=|>=|<|>)\s*([^-^:]+?)\s*(?=(\s*and\s*|$))"
		for match in re.finditer(check_pattern, condition):
			variable = match.group(1)
			operator = match.group(2)
			value = match.group(3)

			if variable == "cura_version":
				variable_value = UM.Application.Application.getInstance().getVersion()
			else:
				UM.Logger.Logger.log("w", "Unknown variable in condition: {variable}".format(variable=variable))
				return False

			# Depending on the variable, we may need to convert the type for proper comparison.
			if variable == "cura_version":
				variable_value = UM.Version.Version(variable_value)
				value = UM.Version.Version(value)

			if operator == "==":
				if variable_value != value:
					return False
			elif operator == "!=":
				if variable_value == value:
					return False
			elif operator == "<":
				if variable_value >= value:
					return False
			elif operator == "<=":
				if variable_value > value:
					return False
			elif operator == ">":
				if variable_value <= value:
					return False
			elif operator == ">=":
				if variable_value < value:
					return False
			else:
				UM.Logger.Logger.log("w", "Unknown condition operator: {operator}".format(operator=operator))
				return False

		return True

	@classmethod
	def preprocess_exposed_conditionals(cls, markdown):
		"""
		Preprocesses a piece of Markdown so that exposed conditional texts get
		properly parsed.

		This is necessary because Mistune provides two methods to customise text
		parsing, which are both insufficient as far as I could find.
		* A renderer can only process existing syntax and then only processes
		the content of the syntax at hand. Exposed conditional syntax would
		display the content *between* two inline HTML or block HTML bits, which
		are not part of any syntax, so the rendering is not powerful enough to
		choose to render this bit or not.
		* A lexer (or in Mistune v2.0 a plug-in) can define new syntax elements,
		including stuff wrapped by delimiters. However since the HTML comments
		that we are using are already existing syntax elements, this causes a
		clash which makes the lexer or plug-in not function. These elements get
		parsed as HTML.

		This function turns all of the exposed conditional elements into hidden
		conditional elements, which then get properly rendered by the
		`inline_html` and `block_html` functions.
		:param markdown: A piece of Markdown that needs to get pre-processed.
		:return: The same Markdown, except that exposed conditionals are changed
		into hidden conditionals.
		"""
		exposed_pattern = r"<!--if\s+([A-Za-z0-9_]+\s*(<=|==|!=|>=|<|>)\s*[^-^:]+?(\s+and\s+[A-Za-z0-9_]+\s*(<=|==|!=|>=|<|>)\s*[^-^:]+?)*)\s*-->(.*?)<!--endif-->"
		replacement = r"<!--if \1:\5-->"
		return re.sub(exposed_pattern, replacement, markdown, flags=re.DOTALL)