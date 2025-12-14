import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# Hello World")
        self.assertEqual(title, "Hello World")

    def test_extract_title_with_whitespace(self):
        title = extract_title("#    Hello World    ")
        self.assertEqual(title, "Hello World")

    def test_extract_title_exception(self):
        with self.assertRaises(Exception):
            extract_title("## Hello World")

if __name__ == "__main__":
    unittest.main()
