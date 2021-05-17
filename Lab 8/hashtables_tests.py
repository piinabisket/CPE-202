import unittest
from hashtables import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        linear_test = import_stopwords('stop_words.txt', HashTableLinear())
        quadratic_test = import_stopwords('stop_words.txt', HashTableQuadratic())
        #  sep_test = import_stopwords('stop_words.txt', HashTableSepchain())
        self.assertEqual(hash_string('dog', 10), 4)
        self.assertEqual(hash_string('god', 3), 2)
        self.assertEqual(quadratic_test.get('between'), 0)
        #self.assertEqual(sep_test.get('between'), 0)
        quadratic_test.remove('between')
        #sep_test.remove('between')
        self.assertRaises(KeyError, quadratic_test.get, 'between')
        self.assertRaises(KeyError, linear_test.get, 'unless')
        #self.assertRaises(KeyError, sep_test.get, 'unless')
        self.assertEqual(quadratic_test.size(), 304)
        self.assertEqual(quadratic_test.contains('the'), True)
        self.assertEqual(linear_test.contains('Forrest'), False)
        # self.assertEqual(sep_test.contains('the'), True)


if __name__ == '__main__':
    unittest.main()
