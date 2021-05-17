import unittest
from project4 import *
import os
import sys

class MyTestCase(unittest.TestCase):
    def test_initializers(self):
        h = SearchEngine(sys.path[0], import_stopwords('stop_words.txt', HashTableLinear()))
        self.assertEqual(h.read_file('test.txt'), ['computer', 'science'])
        self.assertEqual(h.parse_words(h.read_file('test.txt')), ['computer', 'science'])
        self.assertEqual(h.parse_words(h.read_file('test_2.txt')), ['cpe', 'computer', 'science'])
        self.assertIsNotNone(h)


if __name__ == '__main__':
    unittest.main()
