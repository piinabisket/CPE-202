"""
Array based Stack for Lab 3.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


class StackArray:
    """
    an Array based stack
    Attributes:
        arr(any): the data stored in the list
    """
    def __init__(self):
        self.arr = [None] * 2
        self.capacity = 2
        self.num_items = 0

    def __eq__(self, other):
        return self.arr == other.arr

    def __repr__(self):
        return '%s' % self.arr

    def is_empty(self):
        return self.num_items == 0

    def push(self, item):
        if self.capacity == self.num_items:
            self.enlarge()
        self.arr[self.num_items] = item
        self.num_items += 1

    def pop(self):
        if self.num_items == 0:
            raise IndexError
        if self.capacity / self.num_items >= 4:
            self.shrink()
        x = self.arr[self.num_items - 1]
        self.num_items -= 1
        return x

    def peek(self):
        if self.num_items == 0:
            raise IndexError
        return self.arr[self.num_items - 1]

    def size(self):
        return self.num_items

    def enlarge(self):
        """
        Doubles the size of the stack
        Arguments:
            N/a
        Returns:
             N/a
        """
        arr2 = [None] * self.capacity * 2
        for i in range(self.num_items):
            arr2[i] = self.arr[i]
        self.arr = arr2

    def shrink(self):
        """
        Shrinks the size of the stack by half
        Arguments:
            N/a
        Returns:
            N/a
        """
        arr2 = [None] * (self.capacity // 2)
        for i in range(self.num_items):
            arr2[i] = self.arr[i]
        self.arr = arr2
