import unittest
import sys
import os
# To solve import issues https://stackoverflow.com/questions/64849971/cant-create-python-project-tests-via-hitchhikers-guide-to-python-method
from extract.doc_scraper import (
	scrape_docs)

from extract.extracted_data_analyzer import (
	read_doc_links)

# Run tests with python -m unittest test_scraper from root directory
# Reference: https://geekflare.com/unit-testing-with-python-unittest/#:~:text=The%20command%20to%20run%20the,%2Dm%20unittest%20test_utils.py%20.

class ScraperTest(unittest.TestCase):
	def test_scrape_docs(self):
		#TODO: this is testing two functions, break these apart.
		my_path = os.path.abspath(os.path.dirname(__file__))
		path = os.path.join(my_path, "../extract/extracted_data/trial_docs_test.json")
		
		try:
			os.remove(path)
		except:
			pass

		self.assertEqual(scrape_docs(['NCT03386513','NCT03520959','NCT03490747'], path), len(read_doc_links(path)))


if __name__ == '__main__':
    unittest.main()