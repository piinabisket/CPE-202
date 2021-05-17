"""
Function tests for Lab 1.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""

import unittest
from Lab1 import *


class TestCases(unittest.TestCase):
    def test_get_max(self):
        self.assertEqual(get_max([1, 2, 3, 4, 5, 6, 7]), 7)
        self.assertEqual(get_max([40, 60, 4, 700, 67]), 700)
        self.assertEqual(get_max([]), None)

    def test_reverse(self):
        self.assertEqual(reverse("String"), "gnirtS")
        self.assertEqual(reverse("Forrest"), "tserroF")

    def test_search(self):
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7], 3), 2)
        self.assertEqual(search([40, 60, 76, 89, 100, 1000], 100), 4)

    def test_fib(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(20), 6765)

    def test_factorial_rec(self):
        self.assertEqual(factorial_rec(10), 3628800)
        self.assertEqual(factorial_rec(4), 24)

    def test_factorial_iter(self):
        self.assertEqual(factorial_iter(10), 3628800)
        self.assertEqual(factorial_iter(4), 24)


if __name__ == '__main__':
    unittest.main()
