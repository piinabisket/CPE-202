"""
Functions for tree_map for Lab 5
Course: CPE202
Quarter: Spring 2020
Author: Forrest Dudley
"""
import random
import csv
import bst
from classmate import classmate_factory 


class TreeMap:
    """ A map tree class
    Attributes:
        tree (BSTNode): binary search tree
        num_items (int): number of items in tree
    """

    def __init__(self):
        self.tree = None
        self.num_items = 0

    def __eq__(self, other):
        return self.tree == other.tree \
           and self.num_items == other.num_items

    def __repr__(self):
        return '%s' % self.tree

    def __getitem__(self, key):
        """Gets an item with [] notation
        This function calls your get method.
        Arguments:
            key (any): a key which is comparable by <,>,==
        Returns:
            any: the value associated with the key
        Raises:
            KeyError: it raises KeyError because the get function in bst.py raises the error.
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """Sets a key value pair with [] notation
        This function calls your put method.
        Arguments:
            key (any): a key which is comparable by <,>,==
            val (any): the value associated with the key
        """
        self.put(key, val)

    def __contains__(self, key):
        """Checks if a key exists with in notation
        Arguments:
            key (any): a key which is comparable by <,>,==
        Returns:
            boolean: True is the key exists, otherwise False
        """
        return self.contains(key)

    def get(self, key):
        """Put a key value pair into the map
        Calls get function in bst.py
        Arguments:
            key (any): a key which is comparable by <,>,==
        Returns:
            any: the value associated with th key
        Raises:
            KeyError: if the key does not exist
        """
        return bst.get(self.tree, key)

    def put(self, key, val):
        """Puts a key value pair into the map
        Calls insert function in bst.py and increments num_items by 1
        Arguments:
            key (any) : a key which is comparable by <,>,==
            val (any): the value associated with the key
        """
        self.tree = bst.insert(self.tree, key, val)
        self.num_items += 1

    def contains(self, key):
        """Finds if key is in binary search tree
        Args:
            key (any): a key which is comparable by <,>,==
        Returns:
            boolean: True is the key exists, otherwise False
        """
        return bst.contains(self.tree, key)

    def delete(self, key):
        """Deletes a key in the binary search tree
        Args:
            key (any): a key which is comparable by <,>,==
        Raises:
            KeyError: if the key does not exist
        """
        self.tree = bst.delete(self.tree, key)
        self.num_items -= 1

    def size(self):
        """Returns the number of items in the map
        Returns:
            int: the number of items in the map
        """
        return self.num_items

    def find_min(self) -> (any, any):
        """ Finds the minimum key in the tree
        Returns:
            tuple: minimum key and associated value
        """
        return bst.find_min(self.tree)

    def find_max(self) -> (any, any):
        """ Finds the maximum key in the tree
        Returns:
            tuple: maximum key and associated value
        """
        return bst.find_max(self.tree)

    def inorder_list(self) -> list:
        """ Returns list of keys in inorder
        Returns:
            list: a list of keys in inorder
        """
        return bst.inorder_list(self.tree, [])

    def preorder_list(self) -> list:
        """ Returns list of keys in preorder
        Returns:
            list: a list of keys in preorder
        """
        return bst.preorder_list(self.tree, [])

    def tree_height(self) -> int:
        """ Gives the height of the tree
        Returns:
            int: height of tree
        """
        return bst.tree_height(self.tree)

    def range_search(self, lo, hi) -> list:
        """ Returns list of values in a range
        Arguments:
            lo (int): inclusive low value
            hi (int): exclusive high value
        Return:
            (list): list of values in range
        """
        return bst.range_search(self.tree, lo, hi)


def import_classmates(filename):
    """
    Imports classmates from a tsv file
    Args:
        filename (str) : the file name of a tsv file containing classmates
    Returns:
        TreeMap : return an object of TreeMap containing classmates.
    """
    tree_map = TreeMap()
    classmates = []
    file = open(filename, "r")
    lines = csv.reader(file, delimiter="\t")
    for line in lines:
        tokens = line
        classmate = classmate_factory(tokens)
        classmates.append(classmate)
    random.seed(2)
    random.shuffle(classmates)
    for classmate in classmates:
        tree_map.put(classmate.sid, classmate)
    file.close()
    return tree_map


def search_classmate(tmap, sid):
    """
    Searches a classmate in a TreeMap using the sid as a key
    Args:
        tmap (TreeMap): an object of TreeMap
        sid (int): the id of a classmate
    Returns:
        Classmate: a Classmate object
    """
    tester = tmap.contains(sid)
    if tester is not True:
        raise KeyError("Student ID doesn't exist")
    return tmap.get(sid)
