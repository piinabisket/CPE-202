"""
Code for Project 3, creates a Node for a Huffman Tree.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


class HuffmanNode:
    """
    HuffmanNode is either a HuffmanNode, or None.
    Attributes:
        freq (int): Frequency of a character.
        char (str): Character.
        left (HuffmanNode): The left branch of a Huffman Tree.
        right (HuffmanNode): The right branch of a Huffman Tree.
    """

    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Checks for equivalency.
        """
        return self.char == other.char, self.freq == other.freq, \
               self.left == other.left, self.right == other.right

    def __repr__(self):
        """
        Returns formatted character and frequency assigned to HuffmanNode.
        """
        return "{Char: %s, Freq: %s}" % (self.char, self.freq)

    def __lt__(self, other):
        """
        Overrides Python less than (<) operator when comparing two HuffmanNodes,
        to return True if the frequency is
        less, false if the frequency is greater, and compare the ASCII value
        of the character as a tie-breaker when
        frequency is even.
        """
        if self.freq < other.freq:
            return True
        if self.freq == other.freq:
            if ord(self.char) < ord(other.char):
                return True
        return False
