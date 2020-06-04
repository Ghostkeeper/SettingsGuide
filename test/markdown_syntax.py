#Copyright (C) 2020 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

"""
These are tests to check for common mistakes in the Markdown syntax.
"""

import os  # To find all articles.
import re  # To find broken Markdown syntax in those articles.
import unittest  # Run the automated tests.

class TestMarkdownSyntax(unittest.TestCase):
	"""
	These are tests to check for common mistakes in the Markdown syntax.
	"""

	def all_articles(self):
		"""
		Get all article file paths.
		:return: A sequence of all article file paths.
		"""
		article_directories = {"articles", "translations"}
		for article_directory in article_directories:
			for root, _, files in os.walk(os.path.join(os.path.dirname(__file__), "..", "resources", article_directory)):
				for filename in files:
					_, extension = os.path.splitext(filename)
					if extension != ".md":
						continue  # Not an article. Ignore this.
					yield os.path.join(root, filename)

	def test_space_within_link(self):
		"""
		Search for broken links due to a space in the middle of the link
		syntax.

		Example:

		```
		This is a [hyperlink] (some_article.md).
		```

		Most likely, the author intended that to be a hyper link, like this:

		```
		This is a [hyperlink](some_article.md).
		```
		"""
		find_space_within_link = re.compile(r"\[.*\]\s+\(.*\)")
		for filename in self.all_articles():
			with self.subTest(filename=filename):
				with open(filename) as f:
					contents = f.read()
				for broken_link in find_space_within_link.findall(contents):
					assert False, "Article {filename} contains a space within a link: {broken_link}".format(filename=filename, broken_link=broken_link)

	def test_simplest_link(self):
		"""
		Tests if all links are in their simplest form.

		Examples of incorrect links are:
		`folder/../folder/file.md` (can be simplified to `folder/file.md`)
		`folder/./folder/file.md` (can be simplified to `folder/folder/file.md`)
		`./file.md` (can be simplified to `file.md`)
		"""
		find_link = re.compile(r"\[.*?\]\((.*?)\)")
		for filename in self.all_articles():
			with self.subTest(filename=filename):
				with open(filename) as f:
					contents = f.read()
				for link_path in find_link.findall(contents):
					if link_path.startswith("http://") or link_path.startswith("https://"):
						continue  # Ignore web links for now, since os.path doesn't deal with them.
					self.assertEqual(link_path, os.path.normpath(link_path))

if __name__ == "__main__":
	unittest.main()