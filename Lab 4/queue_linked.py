"""
link based queue.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""
from node import *


class QueueLinked:
    """
    a linked-list based queue
    Attributes:
        front(Node): The value at the front of the queue
        rear(Node): The value at the rear of the queue
        num_items(int): Number of items in the queue
        capacity(int): Number of items possible in queue
    """
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.num_items = 0
        self.front = None
        self.rear = None

    def dequeue(self):
        """
        removes an item from the front of the queue
        Returns:
            int: the value from the front of the queue
        """
        if self.is_empty():
            raise IndexError
        temp_val = self.front.val
        if self.num_items == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
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
        temp_node = Node(item)
        if self.num_items == 0:
            self.front = temp_node
            self.rear = temp_node
        else:
            self.rear.next = temp_node
            self.rear = self.rear.next
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
