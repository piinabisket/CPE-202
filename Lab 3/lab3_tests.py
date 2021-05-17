"""
Function tests for Lab 3.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""
import unittest
from stack_array import *
from node import *
from stack_linked import *


class TestCases(unittest.TestCase):
    def test_push_and_peek(self):
        linked = StackLinked()
        array = StackArray()
        linked.push(2)
        array.push(2)
        self.assertEqual(linked.peek(), 2)
        self.assertEqual(array.peek(), 2)

    def test_size(self):
        linked = StackLinked()
        array = StackArray()
        linked.push(2)
        array.push(2)
        linked.push(50)
        array.push(50)
        self.assertEqual(linked.size(), 2)
        self.assertEqual(array.size(), 2)

    def test_is_empty(self):
        linked = StackLinked()
        array = StackArray()
        linked.push(2)
        array.push(2)
        linked.push(60)
        array.push(60)
        linked.push(3)
        array.push(3)
        self.assertEqual(linked.is_empty(), False)
        self.assertEqual(array.is_empty(), False)

    def test_pop_resize(self):
        linked = StackLinked()
        array = StackArray()
        linked.push(2)
        array.push(2)
        linked.push(60)
        array.push(60)
        linked.push(3)
        array.push(3)
        self.assertEqual(linked.pop(), 3)
        self.assertEqual(array.pop(), 3)


if __name__ == '__main__':
    unittest.main()
