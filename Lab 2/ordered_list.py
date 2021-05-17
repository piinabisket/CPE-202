class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class OrderedList:
    """
    Ordered List object
    Attributes:
        head (Node): head of the list
        tail (Node): tail of the list
        num_items (int): number of items stored in the list
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    def __repr__(self):
        return 'test_class'

    def add(self, item):
        

if __name__ == "__main__":
