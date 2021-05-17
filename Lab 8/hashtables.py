"""
Code for Lab 8.\\
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""

from node import *


class HashTableSepchain:
    """
    Hashtable using Separate Chain probing.
    Attributes:
        table_size (int): Size of the table.
        hash (list): Hash table.
        num_items (int): Number of items.
        num_collisions (int): Number of collisions.
    """
    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash = [None] * table_size
        self.num_collisions = 0
        self.num_items = 0

    def __repr__(self):
        return "Hash Table: %s, Table Size: %d," \
               " Num Items: %d, Num Collisions: %d" \
               % (self.hash, self.table_size, self.num_items, self.num_collisions)

    def __eq__(self, other):
        return self.hash == other.table and self.num_items == other.num_items, \
               self.num_collisions == other.num_collisions, self.table_size == other.table_size

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, data):
        pass

    def __contains__(self, key):
        pass


class HashTableLinear:
    """ Hashtable using linear probing.
    Attributes:
        table_size (int): Size of the table.
        hash (list): Hash table.
        num_items (int): Number of items.
        num_collisions (int): Number of collisions.
    """
    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash = [None] * self.table_size
        self.num_items = 0
        self.num_collisions = 0
        self.deleted = Node(Dummy(), Dummy())

    def __eq__(self, other):
        return self.table_size == other.table_size, \
               self.hash == other.hash, \
               self.num_items == other.num_items, \
               self.num_collisions == other.num_collisions

    def __repr__(self):
        return "Hash Table: %s, Table Size: %d," \
               " Num Items: %d, Num Collisions: %d" \
               % (self.hash, self.table_size, self.num_items, self.num_collisions)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """
        Inserts key value pair into hash table.
        Arguments:
            key (str): Key to be inserted into hash table.
            data (any): Data associated with key.
        """
        if self.load_factor() >= 0.75:
            new_table_size = 2 * self.table_size + 1
            self.table_size = new_table_size
            self.resize()
        val = hash_string(key, self.table_size)
        h = len(self.hash)
        i = h % self.table_size
        if self.hash[i] is None:
            self.hash[i] = Node(key, data)
        else:
            self.hash[i].val = data
        while self.hash[i] is not None and key != self.hash[i].key:
            i = (i + 1) % self.table_size

    def get(self, key):
        """
        Returns the value of a key value pair.
        Arguments:
            key (str): Key to be found.
        Returns:
            any: Value associated key.
        Raises:
            KeyError: Raised if the key isn't found.
        """
        len_hash, val = len(self.hash), hash_string(key, self.table_size)
        i = val % len_hash
        while self.hash[i] is not None and key != self.hash[i].key:
            i = (i + 1) % self.table_size
        if self.hash[i] is not None and key == self.hash[i].key:
            return self.hash[i].val
        raise KeyError

    def contains(self, key):
        """
        Checks to see if a key exists.
        Arguments:
            key (str): Key to be search for.
        Returns:
            bool: True if found.
        """
        try:
            self.get(key)
            return True
        except:
            return False

    def remove(self, key):
        """
        Removes a key value pair from the hash table.
        Arguments:
            key (str): key to be removed.
        Returns:
            any: key value pair removed.
        Raises:
            KeyError: Raised if the key value pair doesn't exist.
        """
        hash0 = hash_string(key, self.table_size)
        hash_val = hash0 % self.table_size
        len_hash, h = len(self.hash), hash_string(key, self.table_size)
        i = h % len_hash
        if self.hash[hash_val] is None:
            raise KeyError
        while key != self.hash[i].key:
            i = (i + 1) % self.table_size
        self.hash[i] = None
        i = (i + 1) % self.table_size
        while self.hash[i]:
            key_to_redo, val_to_redo = self.hash[i].key, self.hash[i].val
            self.hash[i] = None
            self.put(key_to_redo, val_to_redo)
            i = (i + 1) % self.table_size

    def size(self):
        """
        Returns the size of the hash table.
        Returns:
            int: number of items in the table.
        """
        return self.num_items

    def load_factor(self):
        """
        Returns load factor of hash table.
        Returns:
            int: Current load factor of table.
        """
        return self.num_items / self.table_size

    def collisions(self):
        """
        Returns number of collisions that have occurred during insertion.
        Returns:
            int: Number of collisions.
        """
        return self.num_collisions

    def resize(self):
        """
        Resizes hash table.
        """
        self.num_collisions = 0
        temp_num_items = self.num_items
        temp = self.hash
        self.hash = [None] * self.table_size
        for item in temp:
            if item is not None:
                node = item
                while node is not None:
                    self.put(node.key, node.val)
                    node = node.next
        self.num_items = temp_num_items


class HashTableQuadratic:
    """ Hashtable using quadratic probing.
    Attributes:
        table_size (int): Size of the table.
        hash (list): Hash table.
        num_items (int): Number of items.
        num_collisions (int): Number of collisions.
        deleted (Node): Deleted Node.
    """
    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash = [None] * self.table_size
        self.num_items = 0
        self.num_collisions = 0
        self.deleted = Node(Dummy(), Dummy())

    def __eq__(self, other):
        return self.table_size == other.table_size, \
               self.hash == other.hash, \
               self.num_items == other.num_items, \
               self.num_collisions == other.num_collisions

    def __repr__(self):
        return "Hash Table: %s, Table Size: %d," \
               " Num Items: %d, Num Collisions: %d" \
               % (self.hash, self.table_size, self.num_items, self.num_collisions)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """
        Inserts key value pair into hash table.
        Arguments:
            key (str): Key to be inserted into hash table.
            data (any): Data associated with key.
        """
        if self.load_factor() >= 0.75:
            new_table_size = 2 * self.table_size
            self.table_size = new_table_size
            self.resize()
        h = hash_string(key, self.table_size)
        i = 1
        while self.hash[h] and self.hash[h] != self.deleted and self.hash[h].key != key:
            h = (h + i * i) % self.table_size
            self.collisions += 1
            i += 1
        self.hash[h] = Node(key, data)
        self.num_items += 1

    def get(self, key):
        """
        Returns the value of a key value pair.
        Arguments:
            key (str): Key to be found.
        Returns:
            any: Value associated key.
        Raises:
            KeyError: Raised if the key isn't found.
        """
        len_hash, val = len(self.hash), hash_string(key, self.table_size)
        i = val % len_hash
        while self.hash[i] is not None and key != self.hash[i].key:
            i = (i + 1) % self.table_size
        if self.hash[i] is not None and key == self.hash[i].key:
            return self.hash[i].val
        raise KeyError

    def contains(self, key):
        """
        Checks to see if a key exists.
        Arguments:
            key (str): Key to be search for.
        Returns:
            bool: True if found.
        """
        try:
            self.get(key)
            return True
        except:
            return False

    def remove(self, key):
        """
        Removes a key value pair from the hash table.
        Arguments:
            key (str): key to be removed.
        Returns:
            any: key value pair removed.
        Raises:
            KeyError: Raised if the key value pair doesn't exist.
        """
        hash0 = hash_string(key, self.table_size)
        hash_val = hash0 % self.table_size
        i = 1
        while self.hash[hash_val] and self.hash[hash_val].key != key:
            hash_val = (hash0 + i * i) % self.table_size
            i += 1
        if self.hash[hash_val] is None:
            raise KeyError
        temp = self.hash[hash_val]
        self.hash[hash_val] = self.deleted
        self.num_items -= 1
        return temp

    def size(self):
        """
        Returns the size of the hash table.
        Returns:
            int: number of items in the table.
        """
        return self.num_items

    def load_factor(self):
        """
        Returns load factor of hash table.
        Returns:
            int: Current load factor of table.
        """
        return self.num_items / self.table_size

    def collisions(self):
        """
        Returns number of collisions that have occurred during insertion.
        Returns:
            int: Number of collisions.
        """
        return self.num_collisions

    def resize(self):
        """
        Resizes hash table.
        """
        self.num_collisions = 0
        temp_num_items = self.num_items
        temp = self.hash
        self.hash = [None] * self.table_size
        for item in temp:
            if item is not None:
                node = item
                while node is not None:
                    self.put(node.key, node.val)
                    node = node.next
        self.num_items = temp_num_items


class Dummy:
    """Dummy object."""
    def __init__(self):
        pass


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
