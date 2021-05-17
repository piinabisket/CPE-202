"""
Node for the Linked-List for Lab 3.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


class Node:
    """
    A Linked List is one of
        - None, or
        - Node(val, next) : A Linked List
    Attributes:
        val (any) : the payload of any type
        next (Node) : a Linked List
    """

    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __eq__(self, other):
        return self.val == other.val

    def __repr__(self):
        return "%s" % self.val
