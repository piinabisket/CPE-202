import unittest


class MyTestCase(unittest.TestCase):
    def test_email_domain(self):
        self.assertEqual(email_domain('example@gmail.com'), 'gmail.com')
        self.assertRaises(ValueError, email_domain(), 'example@geocities')
        list = Node(1, Node(2, Node(3, None)))
        self.assertEqual(split_list(list, 2), (1, 3))
        list = Node(0, Node(5, Node(2, Node(9, None))))
        self.assertEqual(split_list(list, 3), ((0, 2), (5, 9)))
        self.assertEqual(maxval(FloatBinTree(7.98, FloatBinTree(2.67, None, None), FloatBinTree(2.22, None, None))), MaybeFloat(7.98))
        self.assertEqual(maxval(FloatBinTree(None)), MaybeFloat(None))


def split_list(int_list, int):
    """
    Splits a linked list of integers into two lists, one of values
    higher than the passed in value, and one of values lower.
    Arguments:
        int_list (IntList): A linked based list object of integers.
        int(int): value to compare the list against.
    Returns:
        tuple: Two IntLists of values greater than or less than the passed in value.
    """
    list_smaller = None
    list_greater = None
    return split_list_helper(int_list, int, list_smaller, list_greater)


def split_list_helper(int_list, int, list_smaller, list_greater):
    """
    Helper function for split_list().
    Arguments:
        int_list (Node): A linked based list object of integers.
        int(int): value to compare the list against.
        list_smaller (Node): list of smaller than integers.
        list_greater (Node): list of greater than integers.
    Returns:
        tuple: final output of the greater than or less than lists.
        split_list_helper: recursive function call.
    """
    if int_list.val > int:
        list_greater = Node(int_list.val, list_greater)
    if int_list.val < int:
        list_smaller = Node(int_list.val, list_smaller)
    if int_list.next is None:
        return list_smaller, list_greater
    return split_list_helper(int_list, int, list_smaller, list_greater)


class FloatBinTree:
    """
    A binary tree of floats.
    Attributes:
        key(float): key of the key-value pair.
        float(float): value of the key-value pair.
        left(FloatBinTree): left branch.
        right(FloatBinTree): right branch.
    """

    def __init__(self, key, float, left, right):
        self.key = key
        self.float = float
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.float == other.float, self.key == other.key

    def __repr__(self):
        return '%s' % self.float


def maxval(tree):
    """
    Takes a FloatBinTree object and returns a MaybeFloat object, which can either be a float or None,
    if the tree is empty.
    Arguments:
        tree(FloatBinTree): tree to be searched
    Returns:
        MaybeFloat: either a float or none
    """
    if tree is None:
        return MaybeFloat(None)
    return maxval_helper(tree, 0)


def maxval_helper(tree, float):
    """
    Helper function for maxval.
    Arguments:
        tree(FloatBinTree): tree to be searched.
        float(MaybeFloat): MaybeFloat object to be returned.
        last_float(MaybeFloat): value to compare new value to.
    Returns:
        MaybeFloat: either a float or none.
    """
    if tree.left is None and tree.right is None:
        return float
    if tree.left.float > float:
        float = MaybeFloat(tree.left.float)
    elif tree.right.float > float:
        float = MaybeFloat(tree.right.float)
    maxval_helper(tree.left, float)
    maxval_helper(tree.right, float)


self.assertEqual(maxval(FloatBinTree(7.98, FloatBinTree(2.67, None, None), FloatBinTree(2.22, None, None))), MaybeFloat(7.98))
self.assertEqual(maxval(FloatBinTree(None)), MaybeFloat(None))


