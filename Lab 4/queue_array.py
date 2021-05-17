"""
array based queue.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


class QueueArray:
    """
    an array based queue
    Attributes:
        write(int): The index of the back of the queue
        read(int): The index of the front of the queue
        num_items(int): Number of items in queue
        capacity(int): Number of items possible in queue
        self.arr(array): List of values in queue
    """
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.arr = [None] * (self.capacity + 1)
        self.num_items = 0
        self.write = None
        self.read = None

    def dequeue(self):
        """
        removes an item from the front of the queue
        Returns:
            int: the value from the front of the queue
        """
        if self.num_items == 0:
            raise IndexError
        if self.read == self.capacity:
            self.read = 0
        temp_val = self.arr[self.read]
        self.arr[self.read] = None
        self.read += 1
        self.num_items -= 1
        return temp_val

    def enqueue(self, item):
        """
        adds an item to the back of the queue
        Attributes:
            item(int): item to be added to the queue
        """
        if self.is_full():
            raise IndexError
        if self.is_empty():
            self.write = 0
            self.read = 0
        if self.write == self.capacity:
            self.write = 0
        self.arr[self.write] = item
        self.write += 1
        self.num_items += 1

    def is_empty(self):
        """
        checks in the queue is empty
        Returns:
            bool: True if empty
        """
        return self.num_items == 0

    def is_full(self):
        """
        checks if the queue is full
        Returns:
            bool: True if full
        """
        return self.num_items == self.capacity

    def size(self):
        """
        returns number of items in the queue
        Returns:
            int: number of items in array
        """
        return self.num_items
