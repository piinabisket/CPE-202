"""
Linear hash table code.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


class Node:
    """
    Stores key-value pairs for use in HashTableLinear
    Attributes:
        key(str): the key
        val(any): the value
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __repr__(self):
        return 'Key: %s Value: %s' % (self.key, self.val)

    def __eq__(self, other):
        return self.key == other.key and self.val == other.val

    def __getitem__(self, item):
        if item == 0:
            return self.key
        elif item == 1:
            return self.val


class HashTableLinear:
    """
    Stores a hash table using linear probing, consisting of key-value pairs.
    Attributes:
        table_size(int): size of the hash table
        table(list): list of Node Objects
        num_collisions(int): number of collisions when creating the hash table
        num_items(int): number of items in the hash table
        """

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.table = [None] * table_size
        self.num_collisions = 0
        self.num_items = 0

    def __repr__(self):
        return 'Hash: %s' % self.table

    def __eq__(self, other):
        return (self.table == other.table and self.num_items == other.num_items
                and self.num_collisions == other.num_collisions
                and self.table_size == other.table_size)

    def __getitem__(self, key):
        try:
            key += 1
            key -= 1
            if key == 0:
                return
        except:
            return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def resize(self):
        """
        Resizes an array in the case of the load factor becoming too large
        Returns:
            N/A, however it updates the table
        """
        num_items = self.num_items
        size = 2 * self.table_size + 1
        new_table = [None] * size
        self.table_size = size
        old_table = self.table
        self.table = new_table
        for item in old_table:
            if item is not None:
                node = item
                self.put(node.key, node.val)
        self.table = new_table
        self.num_items = num_items

    def put(self, key, data):
        """
        Inserts a key-value pair into the hash table
        Arguments:
            key(str): the key
            data(any): the value
        """
        self.num_items += 1
        size, hash_num = self.table_size, hash_string(key, self.table_size)
        if self.load_factor() >= 0.75:
            num_items = self.num_items
            self.resize()
            self.num_items = num_items
        i = hash_num % size
        while self.table[i] is not None and key != self.table[i].key:
            i = (i + 1) % size
        if self.table[i] is None:
            self.table[i] = Node(key, data)
        else:
            self.table[i].val = data
            self.num_collisions += 1

    def get(self, key):
        """
        Returns value of a key
        Arguments:
            key(str): the key of the item
        Returns:
            any: the value of the key
        Raises:
            KeyError: raises KeyError when the key does not exist in the hash table
        """
        size, hash_num = self.table_size, hash_string(key, self.table_size)
        i = hash_num % size
        while self.table[i] is not None and key != self.table[i].key:
            i = (i + 1) % size
        if self.table[i] is not None and key == self.table[i].key:
            return self.table[i].val
        raise KeyError

    def contains(self, key):
        """
        Checks for a key in the hash table.
        Arguments:
            key(str): the key of the item
        Returns:
            bool: True if exists
        """
        try:
            self.get(key)
            return True
        except:
            return False

    def remove(self, key):
        """
        Removes a key-value pair from the hash table
        Arguments:
            key(str): key of key-value pair to be deleted
        Returns:
            Node: the key-value pair
        Raises:
            KeyError: raises KeyError if key does not exist in the hash table
        """
        i = hash_string(key, self.table_size)
        num_items = self.num_items
        while self.table[i] is not None and self.table[i].key != key:
            i = (i + 1) % self.table_size
        if self.table[i] is None:
            raise KeyError
        else:
            temp = self.table[i]
            self.table[i] = None
            i = (i + 1) % self.table_size
            while self.table[i] is not None:
                self.put(self.table[i].key, self.table[i].val)
                i = (i + 1) % self.table_size
        self.num_items = num_items - 1
        return temp

    def size(self):
        """
        Returns the number of items in the hash table
        Returns:
            int: number of items
        """
        return self.num_items

    def load_factor(self):
        """
        Returns current load factor of the hash table, max 0.75
        Returns:
            float: load factor of the hash table
        """
        return self.num_items / self.table_size

    def collisions(self):
        """
        Returns number of collisions that occurred in the hash table
        Returns:
            int: number of collisions
        """
        return self.num_collisions

    def keys(self):
        """
        Gets list of keys in the hash table
        Returns:
            list: list of the keys in the hash table
        """
        keys = []
        for i in self.table:
            if i is not None:
                keys.append(i.key)
        return keys


def import_stopwords(filename, hashtable):
    """
    Imports text from a file, turns it into a hash table.
    Arguments:
        filename (str): Name of file to be read from.
        hashtable (HashTable Object): Type of hash table to use.
    Returns:
        HashTable Object: A hash table of the words.
    """
    openfile = open(filename, "r")
    file = openfile.readline()
    file = str(file)
    file = file.split(' ')
    for word in file:
        hashtable.put(word, 0)
    openfile.close()
    return hashtable


def hash_string(string, size):
    """
    Converts a string into a hash.
    Arguments:
        string (str): String to be converted.
        size (int): Size.
    Returns:
        int: hashed string.
    """
    hash = 0
    for c in string:
        hash = (hash * 31 + ord(c)) % size
    return hash
