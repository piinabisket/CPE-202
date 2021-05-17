"""
Linked-list Stack for Project 2.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


from node import *


class StackLinked:
    """
    a linked-list based stack
    Attributes:
        top(Node): node at the top of the stack
        num_items(int): number of items in the stack
    """
    def __init__(self):
        self.top = None
        self.num_items = 0

    def __eq__(self, other):
        return self.top == other.top and self.num_items == other.num_items

    def __repr__(self):
        return '%s' % self.top

    def is_empty(self):
        return self.num_items == 0

    def peek(self):
        if self.num_items == 0:
            raise IndexError
        return self.top.val

    def size(self):
        return self.num_items

    def pop(self):
        if self.num_items == 0:
            raise IndexError
        self.num_items -= 1
        x = self.top.val
        self.top = self.top.next
        return x

    def push(self, item):
        self.top = Node(item, self.top)
        self.num_items += 1
