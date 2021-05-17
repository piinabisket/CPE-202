"""
Functions for vst for Lab 5
Course: CPE202
Quarter: Spring 2020
Author: Forrest Dudley
"""


class BSTNode:
    """ Binary Search Tree is one of
    - None
    - BSTNode

    Attributes:
        key (int): key
        val (any): value associated with the key
        left (BSTNode): left subtree of Binary Search Tree
        right (BSTNode): right subtree of Binary Search Tree
    """
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.val == other.val \
           and self.key == other.key \
           and self.left == other.left \
           and self.right == other.right

    def __repr__(self):
        return 'Value: %s Key: %s' % (self.val, self.key)


def get(tree, key)->any:
    """
    Arguments:
        tree (BSTNode): binary search tree
        key (any): key
    Returns:
        any: value stored in the map
    """
    if tree is None:
        return None
    if tree.key == key:
        return tree.val
    if key < tree.key:
        return get(tree.left, key)
    return get(tree.right, key)


def contains(tree, key)->bool:
    """
    Checks if a given item exists
    Arguments:
        tree (BSTNode): binary search tree
        key (any): key
    Returns:
        boolean: true if key in tree, false otherwise
    """
    if tree is None:
        return False
    if tree.key == key:
        return True
    if key < tree.key:
        return contains(tree.left, key)
    return contains(tree.right, key)


def insert(tree, key, val)->BSTNode:
    """
    Inserts an item with a key into the tree
    Arguments:
        tree (BSTNode): binary search tree
        key (any): key
        val (val): value associated with key
    Returns:
        BSTNode: a tree node
    """
    if tree is None:
        return BSTNode(key, val, None, None)
    if key < tree.key:
        tree.left = insert(tree.left, key, val)
    if key > tree.key:
        tree.right = insert(tree.right, key, val)
    return tree


def delete(tree, key) -> BSTNode:
    """
    Deletes a node from the tree
    Arguments:
         tree (BSTNode): binary search tree
         key (any): key
    Returns:
        BSTNode: node deleted
    """
    if tree is None:
        raise KeyError("Branch doesn't exist")
    if tree.key == key:
        if tree.left and tree.right:
            replacement = get_replacement(tree.right)
            tree = delete(tree, replacement.key)
            tree.key = replacement.key
            tree.val = replacement.val
            return tree
        if tree.left:
            return tree.left
        return tree.right
    if tree.key > key:
        tree.left = delete(tree.left, key)
    else:
        tree.right = delete(tree.right, key)
    return tree


def find_min(tree)->(any, any):
    """
    Finds the minimum value in the tree
    Arguments:
        tree (BSTNode): a binary search tree
    Returns:
        tuple: key and minimum associated value
    """
    if tree is None:
        raise ValueError("Tree is empty")
    if tree.left is None:
        return tree.key, tree.val
    return find_min(tree.left)


def find_max(tree)->(any, any):
    """
    Finds the maximum value in the tree
    Arguments:
        tree (BSTNode): a binary search tree
    Returns:
        tuple: key and maximum associated value
    """
    if tree is None:
        raise ValueError("Tree is empty")
    if tree.right is None:
        return tree.key, tree.val
    return find_max(tree.right)


def inorder_list(tree, accum):
    """
    Returns list of keys in inorder
    Arguments:
        tree (BTSNode): a binary search tree
        accum (list): a list
    Returns:
        list: a list of keys in inorder
    """
    if accum is None:
        accum = []
    if tree is None:
        return accum
    if tree is not None:
        inorder_list(tree.left, accum)
        accum.append(tree.key)
        inorder_list(tree.right, accum)
    return accum

def preorder_list(tree, accum):
    """
    Returns list of values in preorder
    Arguments:
        tree (BTSNode): a binary search tree
        accum (list): a list
    Returns:
        list: a list of values in preorder
    """
    if accum is None:
        accum = []
    if tree is None:
        return accum
    if tree is not None:
        accum.append(tree.key)
        preorder_list(tree.left, accum)
        preorder_list(tree.right, accum)
    return accum


def tree_height(tree)->int:
    """
    Finds the height of the given tree
    Arguments:
        tree (BSTNode): a binary search tree
    Returns:
        int: height of tree
    """
    if tree is None:
        return -1
    return 1 + max(tree_height(tree.left), tree_height(tree.right))


def range_search(tree, lo, hi, accum=None):
    """
    Returns list of values in a range
    Arguments:
        tree (BSTNode): a binary search tree
        lo (int): inclusive low value
        hi (int): exclusive high value
        accum (list): empty list
    Return:
        (list): list of values in range
    """
    if accum is None:
        accum = []
    if tree is None:
        return accum
    if hi <= tree.key:
        return range_search(tree.left, lo, hi, accum)
    if tree.key < lo:
        return range_search(tree.right, lo, hi, accum)
    if tree is not None:
        range_search(tree.left, lo, hi, accum)
        if tree.key >= lo and tree.key < hi:
            accum.append((tree.key, tree.val))
        range_search(tree.right, lo, hi, accum)
    return accum


def get_replacement(tree):
    """
    Helper function for delete
    Arguments:
        tree (BSTNode): a binary search tree
    Returns:
        BSTNode: a replacement node
    """
    if tree is None:
        raise ValueError('Tree is empty.')
    if tree.left is None:
        return tree
    return get_replacement(tree.left)

