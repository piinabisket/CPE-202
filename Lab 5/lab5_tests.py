"""
tests for lab  5.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""

import unittest

import bst
from tree_map import *
from classmate import *


class TestCases(unittest.TestCase):
    def test_bst(self):
        tree = bst.BSTNode(10, 10)
        self.assertEqual(bst.insert(tree, 1, '+'), tree)
        self.assertEqual(bst.insert(tree, 20, 20), tree)
        self.assertEqual(bst.insert(tree, 9, 9), tree)
        self.assertEqual(bst.contains(tree, 9), True)
        self.assertEqual(bst.contains(tree, 21), False)
        self.assertEqual(bst.get(tree, 9), 9)
        self.assertEqual(bst.get(tree, 20), 20)
        self.assertEqual(bst.find_min(tree), (1, '+'))
        self.assertEqual(bst.find_max(tree), (20, 20))
        self.assertEqual(bst.inorder_list(tree, []), [1, 9, 10, 20])
        self.assertEqual(bst.preorder_list(tree, []), [10, 1, 9, 20])
        self.assertEqual(bst.tree_height(tree), 2)
        self.assertEqual(bst.range_search(tree, 1, 10, []), [(1, '+'), (9, 9)])

    def test_tree_map(self):
        '''
        maptree = TreeMap
        maptree.put(10, 10)
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        self.assertEqual()
        '''


if __name__ == '__main__':
    unittest.main()
