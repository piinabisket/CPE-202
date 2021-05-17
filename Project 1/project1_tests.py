import unittest
from perm_gen_lex import *
from base_convert import *
from bear_picnic import *


class TestCases(unittest.TestCase):
    def test_perm_gen_lex(self):
        self.assertEqual(perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(perm_gen_lex(''), [])
        self.assertEqual(perm_gen_lex('xy'), ['xy', 'yx'])
        self.assertEqual(perm_gen_lex('x'), ['x'])

    def test_convert(self):
        self.assertEqual(convert(15, 2), '1111')
        self.assertEqual(convert(67, 2), '1000011')
        self.assertEqual(convert(316, 16), '13C')
        self.assertEqual(convert(1000, 12), '6B4')

    def test_bears(self):
        self.assertEqual(bears(42), True)
        self.assertEqual(bears(41), False)
        self.assertEqual(bears(0), False)
        self.assertEqual(bears(250), True)
        self.assertEqual(bears(53), False)
        self.assertEqual(bears(210), True)


if __name__ == "__main__":
    unittest.main()