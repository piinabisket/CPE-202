"""
Functions for Lab 7.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


class MinPQ:
    """
    Minimum Priority Queue.
    Attributes:
        capacity (int): Capacity of the queue
        num_items (int): Number of items in the queue
        arr (list): Array of items in queue
    """

    def __init__(self, arr=None):
        if arr is not None:
            self.arr = arr
            self.num_items = len(self.arr)
            self.capacity = len(self.arr)
            self.heapify()
        else:
            self.arr = [None] * 2
            self.num_items = 0
            self.capacity = 2

    def __eq__(self, other):
        return self.arr == other.arr, self.capacity == other.capacity, \
               self.num_items == other.num_items

    def __repr__(self):
        return 'arr: %s, capacity: %s, num_items: %s' % (self.arr, self.capacity, self.num_items)

    def heapify(self):
        """
        Converts an array into a heaped array.
        """
        length = self.num_items
        i = self.index_parent(length - 1)
        while i >= 0:
            self.shift_down(i)
            i -= 1
        return

    def insert(self, item):
        """
        Inserts an item into the queue.
        Args:
            item (any): Item to be inserted into the queue.
        """
        self.enlarge()
        if self.num_items == 0:
            self.arr[0] = item
        else:
            self.arr[self.size()] = item
        self.shift_up(self.num_items)
        self.num_items += 1
        return

    def del_min(self) -> any:
        """
        Deletes the minimum item in the queue.
        Returns:
            int: Smallest integer value in the min heap.
        Raises:
            IndexError: Raises IndexError when queue is empty.
        """
        if self.num_items == 0:
            raise IndexError
        min_item = self.arr[0]
        self.arr[0] = self.arr[self.num_items - 1]
        self.num_items -= 1
        self.shift_down(0)
        return min_item

    def min(self) -> any:
        """
        Returns the minimum item in the queue without deleting the item.
        Returns:
            any: Minimum item.
        Raises:
            IndexError: Raises IndexError when the queue is empty.
        """
        if self.num_items == 0:
            raise IndexError
        return self.arr[0]

    def is_empty(self):
        """
        Checks if the queue is empty.
        Returns:
            bool: True if empty.
        """
        if self.num_items == 0:
            return True
        return False

    def size(self):
        """
        Returns the number of items in queue.
        Returns:
            int: Returns the number of items in queue.
        """
        return self.num_items

    def shift_up(self, idx):
        """
        Shift up an item in the queue with recursion.
        Args:
            idx(int): The index of the item to be shifted up the array.
        """
        iparent = self.index_parent(idx)
        if iparent < 0 or self.arr[iparent] < self.arr[idx]:
            return None
        temp = self.arr[idx]
        self.arr[idx] = self.arr[iparent]
        self.arr[iparent] = temp
        return self.shift_up(iparent)

    def shift_down(self, idx):
        """
        Shifts down an item in the queue with recursion.
        Args:
            idx(int): Index of the item to be shifted down the array.
        """
        if self.num_items < idx:
            return None
        imin = self.index_minchild(idx)
        if imin < 0 or self.arr[idx] < self.arr[imin]:
            return None
        self.arr[idx], self.arr[imin] = self.arr[imin], self.arr[idx]
        return self.shift_down(imin)

    def enlarge(self):
        """Enlarges the array"""
        if self.capacity == self.num_items:
            newarr = [None] * (self.capacity * 2)
            for i in range(self.num_items):
                newarr[i] = self.arr[i]
            self.arr = newarr
            self.capacity = self.capacity * 2
        return self.arr

    def shrink(self):
        """Shrinks the array"""
        if self.capacity / self.num_items >= 4:
            newarr = [None] * (self.capacity // 2)
            for i in range(self.num_items):
                newarr[i] = self.arr[i]
            self.arr = newarr
            self.capacity = self.capacity // 2
        return self.arr

    def index_minchild(self, i):
        """
        Compute the index of the child with the lowest value.
        Args:
            i(int): index.
        Returns:
            int: index of the min child.
        """
        if self.num_items - 1 < index_left(i):
            return -1
        if self.num_items - 1 < index_right(i):
            return index_left(i)
        if self.arr[index_left(i)] < self.arr[index_right(i)]:
            return index_left(i)
        return index_right(i)

    def index_parent(self, i):
        """
        Compute the index of the parent.
        Args:
            i(int): index.
        Returns:
            int: index of parent.
        """
        idx = (i - 1) // 2
        if self.arr[idx] is None:
            return -1
        return idx


def index_left(i):
    """
    Compute the index of the left child.
    Args:
        i(int): index.
    Returns:
        int: index of the left child.
    """
    return 2 * i + 1


def index_right(i):
    """
    Compute the index of the right child.
    Args:
        i(int): index.
    Returns:
        int: index of the right child.
    """
    return 2 * i + 2
