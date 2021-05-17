"""
tests for lab  4.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""

import unittest

from node import *
from queue_array import *
from queue_linked import *


class TestCases(unittest.TestCase):
    def test_array(self):
        q = QueueArray()
        self.assertEqual(q.is_empty(), True)
        q.enqueue(3)
        self.assertEqual(q.is_empty(), False)
        self.assertEqual(q.is_full(), False)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.arr, [3, None, None])
        self.assertEqual(q.dequeue(), 3)
        q.enqueue(7)
        q.enqueue(8)
        self.assertEqual(q.is_full(), True)
        self.assertRaises(IndexError, q.enqueue, 3)
        q.dequeue()
        q.dequeue()
        self.assertRaises(IndexError, q.dequeue)

    def test_linked(self):
        q = QueueLinked()
        self.assertEqual(q.is_empty(), True)
        q.enqueue(3)
        self.assertEqual(q.is_empty(), False)
        self.assertEqual(q.is_full(), False)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 3)
        q.enqueue(7)
        q.enqueue(8)
        self.assertEqual(q.is_full(), True)
        self.assertRaises(IndexError, q.enqueue, 3)
        q.dequeue()
        q.dequeue()
        self.assertRaises(IndexError, q.dequeue)

    def test_node(self):
        node = Node(1, 2)
        node_1 = Node(1, 3)
        self.assertTrue(node == node_1)


if __name__ == '__main__':
    unittest.main()
