#Copyright (C) 2020 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

from .Mistune import mistune  # Extending from this library's renderer.
import os.path  # To fix the source paths for images.
import PyQt5.QtCore  # To fix the source paths for images using QUrl.
import UM.Application  # To get the application version.
import UM.Logger  # To log warnings if parsing went wrong.
import UM.Qt.Bindings.Theme  # To get the correct hyperlink colour from the theme.
import UM.Version  # To compare version numbers for conditional content.

CONDITIONAL_PATTERN = r"<!--if\s+([A-Za-z0-9_]+)\s*(<|<=|==|>=|>)\s*([^-^:]+)\s*(:(.*)-->|-->(.*)<!--endif-->)"
"""
This is a pattern that matches content that is shown only if a certain condition
is met.

The regex matches two types of syntax at the same time:
* There is a syntax that is completely enclosed in one HTML comment. The content
then does not get shown in Github. The syntax has the form:
`<!--if variable < value :conditional text-->`
Note that the conditional text includes all whitespace around it, so if the
conditional text should not get spaces around it there should be no whitespace
between the : and the text or between the --> and the text.
* There is also a syntax that leaves the content exposed outside of the HTML
comment. This content then also gets shown in Github. The syntax has the form:
`<!--if variable == value -->conditional text<!--endif-->
Again, the conditional text includes all whitespace between the two HTML
comments.

Note that there may be no whitespace before the "if" keyword or around the
"endif" keyword. This is to reduce false positives.

The pattern matches on six groups:
# The "variable" which is checked against.
# The comparator to compare the variable to the value with. This is one of the
following: < <= == >= >
# The "value" to which to compare the variable.
# This group is used for prioritising the order of operations in the regex
itself and shouldn't be used.
# The conditional text to show when using the "hidden" syntax (the first one as
documented above).
# The conditional text to show when using the "exposed" syntax (the second one
as documented above).
"""

def parse_conditional(parser, match, state):
	"""
	Parse conditional content.

	This is part of an implementation of a Mistune plug-in. These parameters are
	provided to the function by Mistune itself:
	:param parser: The parser to add this syntax rule to.
	:param match: A regex match that matches with the CONDITIONAL_PATTERN.
	:param state: A memory of state variables provided by earlier parsings.
	:return: A tuple containing the render function to call on the parser to
	render this conditional, as well as the parameters to call it with.
	"""
	variable = match.group(1)
	operator = match.group(2)
	value = match.group(3)
	if match.group(4) is not None:
		content = match.group(4)
	else:
		content = match.group(5)
	return "conditional", variable, operator, value, content

def render_conditional(variable, operator, value, content):
	"""
	Render conditional content. Or don't render it, maybe.
	:param variable: A variable to check against whether to render the content
	or not. These are the possible variables that can be checked against:
	* cura_version: The version of Cura that the user is running this plug-in
	in.
	:param operator: The operator to check the variable against the value. This
	is one of: < <= == >= >
	:param value: The value to compare the variable to. This is a string,
	stripped of whitespace.
	:param content: The content to show if the condition is met.
	:return: The text to add to the RichText document shown in Qt. If the
	condition is not met, this will be an empty string.
	"""
	if variable == "cura_version":
		variable_value = UM.Application.Application.getInstance().getVersion()
	else:
		UM.Logger.Logger.log("w", "Unknown conditional variable: {variable}".format(variable=variable))
		return ""

	# Some type conversion so that we can properly compare, which may depend on the type in the variable.
	if variable == "cura_version":
		variable_value = UM.Version.Version(variable_value)
		value = UM.Version.Version(value)

	if operator == "<":
		condition_met = variable_value < value
	elif operator == "<=":
		condition_met = variable_value <= value
	elif operator == "==":
		condition_met = variable_value == value
	elif operator == ">=":
		condition_met = variable_value >= value
	elif operator == ">":
		condition_met = variable_value > value
	else:
		UM.Logger.Logger.log("w", "Unknown operator: {operator}".format(operator=operator))  # Should never happen because the regex doesn't match then.
		return ""

	if condition_met:
		return content
	else:
		return ""

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