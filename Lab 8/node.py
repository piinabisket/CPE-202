"""
Node for Lab 8
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


class Node:
    """
    A Linked List is one of
        - None, or
        - Node(key, val, next) : A Linked List
    Attributes:
        key (str): key in key-val pair.
        val (any) : the payload of any type, in this case 0.
        next (Node) : a Linked List.
    """
    def __init__(self, key, val=0, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt

    def __eq__(self, other):
        return self.val == other.val, self.key == other.key

    def __repr__(self):
        return "Key: %s, Val: %s" % (self.key, self.val)
