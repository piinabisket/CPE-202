"""
Code for Project 3, compressing a text file with Huffman Encoding.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""

from min_pq import *
from huffman import *
from huffman_bit_writer import *
from huffman_bit_reader import *


def cnt_freq(filename):
    """
    Counts the frequency of characters in a text file.
    Arguments:
        filename (str): Name of file to be read.
    Returns:
        list: A list of size 256, where the index indicates the ASCII value of a given character,
              and the integer at that spot is the number of times that character appears.
    """
    file = filename
    count = [0] * 256
    for char in filename:
        count[ord(char)] += 1
    return create_code(create_huff_tree(count))


def create_huff_tree(list_of_freqs):
    """
    Creates a huffman tree from the list given from cnt_freq().
    Arguments:
        list_of_freqs(list): List given by cnt_freq().
    Returns:
        HuffmanNode: A tree comprised of HuffmanNode objects,
                     where high frequency character objects go left, and low
        frequency objects go right.
    """
    size = len(list_of_freqs)
    huff_tree = MinPQ()
    for i in range(size):
        if list_of_freqs[i] > 0:
            huff_tree.insert(HuffmanNode(list_of_freqs[i], chr(i)))
    while huff_tree.size() > 1:
        node1 = huff_tree.del_min()
        node2 = huff_tree.del_min()
        if ord(node1.char) < ord(node2.char):
            min_char = node1.char
        else:
            min_char = node2.char
        huff_tree.insert(HuffmanNode(node1.freq + node2.freq, min_char, node1, node2))
    return huff_tree.del_min()


def create_code(root_node):
    """
    Creates a list of size 256, where index correlates to ASCII character,
    and the number at the spot correlates to it's frequency in binary.
    Arguments:
        root_node (HuffmanNode): Huffman Tree given by create_huff_tree.
    Returns:
        list: List of size 256 with binary code representing character frequency.
    """
    code_list = [''] * 256
    codes = create_code_helper(root_node, '', code_list)
    return codes


def create_code_helper(tree, code, code_list):
    """
    Recursive helper function for create_code.
    """
    if tree is None:
        return code_list
    if tree.left is None and tree.right is None:
        code_list[ord(tree.char)] = code
    create_code_helper(tree.left, code + '0', code_list)
    create_code_helper(tree.right, code + '1', code_list)
    return code_list


def huffman_encode(in_file, out_file):
    """
    Reads a given file, and returns both an output file with a string of the binary, and
    a file containing the compressed version of the original file, via Huffman encoding.
    Arguments:
        in_file (str): Name of the file to be compressed.
        out_file (str): Name of file to be written to.
    """
    encoded = ''
    if '.txt' in out_file:
        compressed = out_file[:-4] + '_compressed.txt'
    else:
        compressed = out_file + '_compressed.txt'
    compressed_file = HuffmanBitWriter(compressed)
    freqs = cnt_freq(in_file)
    code_array = create_code(create_huff_tree(freqs))
    input_file = open(in_file, 'r')
    output_file = open(out_file, 'w')
    lines = input_file.readlines()
    for item in lines:
        for bit in item:
            encoded += str(code_array[ord(bit)])
    output_file.write(create_header(freqs) + encoded)
    compressed_file.write_str(create_header(freqs))
    compressed_file.write_code(encoded)
    compressed_file.write_code(code_array[0])
    compressed_file.close()
    output_file.close()


def create_header(list_of_freqs):
    """
    Creates the header for the output file in huffman_encoding().
    Arguments:
        list_of_freqs (list): List returned from cnt_freq().
    Returns:
        str: A string formatted to act as the header for the
             output of huffman_encoding().
    """
    header = ''
    size = len(list_of_freqs)
    for i in range(size):
        if list_of_freqs[i] != 0:
            header += '%s %s ' % (i, list_of_freqs[i])
    header += '\n'
    return header


def huffman_decode(encoded_file, decode_file):
    """
    Decodes a compressed Huffman Encoded file.
    Arguments:
        encoded_file (str): Encoded file to be decompressed.
        decode_file (str): File to write decoded text to.
    """
    encoded_file_opened = HuffmanBitReader(encoded_file)
    decode_file = HuffmanBitWriter(decode_file)
    freq_string = encoded_file_opened.read_str()
    freq_string = str(freq_string[:-2]).strip(' ').strip('b').strip("'")
    freq_string = list(freq_string.split(' '))
    tree = create_huff_tree(parse_header(freq_string))
    temp_tree = tree
    decoded = ''
    while True:
        bit = encoded_file_opened.read_bit()
        if bit:
            temp_tree = temp_tree.right
        else:
            temp_tree = temp_tree.left
        if temp_tree.left is None and temp_tree.right is None:
            if ord(temp_tree.char) == 0:
                break
            decoded += temp_tree.char
            temp_tree = tree
    decode_file.write_str(decoded)
    decode_file.close()
    encoded_file_opened.close()


def parse_header(header_string):
    """
    Parses the header of a compressed file.
    Arguments:
        header_string (str): String of header from compressed file.
    Returns:
        list: A list formatted like the return from cnt_freq().
    """
    fixit = [0] * 256
    counter = 0
    index = 0
    for item in header_string:
        if counter % 2 == 0:
            index = int(item)
        else:
            fixit[index] = int(item)
        counter += 1
    return fixit


if __name__ == "__main__":
    print('%s' % cnt_freq('shoeless'))
