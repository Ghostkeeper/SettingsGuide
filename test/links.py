#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

"""
These are tests to check whether there are any broken links in any articles.
"""

import os  # To find all articles.
import re  # To find the links in the Markdown articles.
import unittest  # Run the automated tests.

class TestLinks(unittest.TestCase):
	"""
	These are tests to check whether there are any broken links in any articles.
	"""

	def all_articles(self):
		"""
		Get all article file paths.
		:return: A sequence of all article file paths.
		"""
		for root, _, files in os.walk(os.path.join(os.path.dirname(__file__), "..", "resources", "articles")):
			for filename in files:
				_, extension = os.path.splitext(filename)
				if extension != ".md":
					continue  # Not an article. Ignore this.
				yield os.path.join(root, filename)

	def test_images(self):
		"""
		Test if the links to images are correct.
		"""
		find_images = re.compile(r"!\[.*\]\(([^\)]*)\)")
		for filename in self.all_articles():
			with self.subTest():
				with open(filename) as f:
					contents = f.read()
				for image_link in find_images.findall(contents):
					image_path = os.path.join(os.path.dirname(filename), image_link)
					assert os.path.exists(image_path), "Article {article_path} refers to image {image_path}, which doesn't exist.".format(article_path=filename, image_path=image_link)

	def test_articles(self):
		"""
		Test if the links to other articles are correct.
		"""
		find_links = re.compile(r"\[.*\]\(([^\)]*)\)")
		for filename in self.all_articles():
			with self.subTest():
				with open(filename) as f:
					contents = f.read()
				for link in find_links.findall(contents):
					if not link.endswith(".md"):
						continue  # Only find articles.
					if link.startswith("https://"):
						continue  # Don't find articles on the internet either.
					article_path = os.path.join(os.path.dirname(filename), link)
					assert os.path.exists(article_path), "Article {article_path} refers to article {path}, which doesn't exist.".format(article_path=filename, path=article_path)

if __name__ == "__main__":
	unittest.main()