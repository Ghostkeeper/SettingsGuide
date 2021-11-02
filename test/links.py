#Copyright (C) 2020 Ghostkeeper
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

	"""
	Regex to find hyperlinks in articles.

	The capture group is the URL in the link. The text itself is ignored.
	"""
	find_links = re.compile(r"\[.*?\]\(([^\)]*)\)")

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
					self.assertTrue(os.path.exists(image_path), "Article {article_path} refers to image {image_path}, which doesn't exist.".format(article_path=filename, image_path=image_link))

	def test_articles(self):
		"""
		Test if the links to other articles are correct.
		"""
		for filename in self.all_articles():
			with self.subTest():
				with open(filename) as f:
					contents = f.read()
				for link in self.find_links.findall(contents):
					if link.startswith("https://") or link.startswith("http://"):
						continue  # Don't find articles on the internet either.
					article_path = os.path.join(os.path.dirname(filename), link)
					self.assertTrue(os.path.exists(article_path), "Article {article_path} refers to article {path}, which doesn't exist.".format(article_path=filename, path=article_path))

	def test_links_within_translations(self):
		"""
		Tests that translations of articles link to translated articles of the same language if a translation is
		available.
		"""
		# First gather which articles are translated in each language.
		all_articles = list(self.all_articles())
		translated_articles = {}
		for filename in all_articles:
			rel_filename = os.path.relpath(filename, os.path.join(os.path.dirname(__file__), "..", "resources"))  # Make relative to the resources folder.
			path = rel_filename.split(os.sep)
			if len(path) <= 2:
				continue  # Ignore files not in the translations/<language> folders.
			if path[0] != "translations":
				continue

			language = path[1]
			if language not in translated_articles:
				translated_articles[language] = {}
			translated_articles[language][os.path.basename(filename)] = filename

		for filename in all_articles:
			rel_filename = os.path.relpath(filename, os.path.join(os.path.dirname(__file__), "..", "resources"))  # Make relative to the resources folder.
			path = rel_filename.split(os.sep)
			if len(path) <= 2:
				continue  # Ignore files not in the translations/<language> folders.
			if path[0] != "translations":
				continue
			language = path[1]

			with self.subTest():
				with open(filename) as f:
					contents = f.read()
				for link in self.find_links.findall(contents):
					if link.startswith("https://") or link.startswith("http://"):
						continue  # Don't find articles on the internet either.
					absolute_link = os.path.join(os.path.dirname(filename), link)
					linked_file = os.path.basename(link)
					if linked_file in translated_articles[language]:
						self.assertEqual(os.path.abspath(absolute_link), os.path.abspath(translated_articles[language][linked_file]), "There is a translation of {linked_file} in {language}, but {article} is not linking to the translation.".format(linked_file=linked_file, language=language, article=os.path.basename(filename)))

if __name__ == "__main__":
	unittest.main()
