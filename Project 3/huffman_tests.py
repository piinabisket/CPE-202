"""
Test for Project 3, compressing a text file with Huffman Encoding.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


import unittest
from huffman_coding import *


class TestHuffman(unittest.TestCase):
    def test_cnt_freq(self):
        freq_list = cnt_freq("file1.txt")
        test_list = [0] * 256
        test_list[0] = 1
        test_list[97:104] = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freq_list, test_list)

    def test_create_huff_tree_and_code(self):
        code = create_code(create_huff_tree(cnt_freq("file1.txt")))
        self.assertEqual(code[ord('a')], '11111')
        self.assertEqual(code[ord('d')], '0')

    def test_huffman_encoding(self):
        huffman_encode("file1.txt", "output.txt")
        self.assertEqual(100110111, 100110111)

    def test_huffman_decoding(self):
        huffman_decode("file1_soln_compressed.txt", "output.txt")
        self.assertEqual('ddddddddaaaabbbeeee', 'ddddddddaaaabbbeeee')


if __name__ == "__main__":
    unittest.main()