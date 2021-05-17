"""
Code for project 4
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


import os
import math
from hashtables import HashTableLinear


class SearchEngine:
    """
    Builds and maintains an inverted index of documents stored in a specified directory and
    provides a functionality to search documents with query terms.
    Arguments:
        directory (str): a directory name.
        stopwords (HashTableQuadratic): a hash table containing stopwords.
        doc_length (HashTableQuadratic): a hash table containing the total number of words
                    in each document.
        term_freqs (HashTableQuadratic): a hash table of hash tables for each term. Each hash table
                    contains the frequency of the term in documents

    """

    def __init__(self, directory, stopwords):
        self.doc_length = HashTableLinear()
        self.term_freqs = HashTableLinear()
        self.stopwords = stopwords
        self.index_files(directory)

    def read_file(self, infile):
        """
        A helper function to read a file
        Argumentss:
            infile (str) : the path to a file
        Returns:
            list : a list of str read from a file
        """
        with open(infile, 'r') as infile:
            open_file = infile.read()
            list_file = []
            for item in open_file.split():
                if self.stopwords.contains(item) is False:
                    list_file.append(item)
        return list_file

    def parse_words(self, lines):
        """
        splits strings into words by spaces.
        Converts words to lower cases,
        and removes newline chars, parentheses, brackets such as “[“, “]”, “{“, “}”
        and punctuations such as “,”, “.”, “?”, “!”.
        Excludes stopwords.
        Args:
            lines (list) : a list of strings
        Returns:
            list : a list of words
        """
        words_list = []
        new_list = []
        for line in lines:
            words_list += line.split()
        for word in words_list:
            new_word = word
            for char in word:
                if not 65 <= ord(char) <= 122:
                    new_word = new_word.replace(char, '')
                if 65 <= ord(char) <= 90:
                    new_word = new_word.replace(char, char.lower())
            new_list.append(new_word)
        new_list = self.exclude_stopwords(new_list)
        return new_list

    def exclude_stopwords(self, terms):
        """
        exclude stopwords from the list of terms
        Args:
            terms (list):
        Returns:
            list : a list of str with stopwords removed
        """
        new_file = []
        for item in terms:
            if self.stopwords.contains(item) is False:
                new_file.append(item)
        return new_file

    def count_words(self, file_path_name, words):
        """
        Counts words in a file and store the frequency of each
        word in the term_freqs hash table.
        Args:
            file_path_name (str) : the file name
            words (list) : a list of words
        """
        self.doc_length.put(file_path_name, 0)
        for item in words:
            if self.term_freqs.contains(item):
                if self.term_freqs.get(item).contains(file_path_name):
                    self.term_freqs[item][file_path_name] += 1
                else:
                    self.term_freqs[item].put(file_path_name, 1)
            else:
                h = HashTableLinear()
                h.put(file_path_name, 1)
                self.term_freqs.put(item, h)
            self.doc_length[file_path_name] += 1

    def index_files(self, directory):
        """index all text files in a given directory
        Args:
            directory (str): the path of a directory
        """
        directory_open = os.listdir(directory)
        for item in directory_open:
            file_dir = os.path.join(directory, item)
            if os.path.isfile(item):
                text_check = os.path.splitext(item)
                if text_check[1] == '.txt':
                    self.count_words(file_dir, self.parse_words(self.read_file(item)))

    def get_wf(self, tf):
        """
        Computes the weighted frequency
        Args:
            tf (float) : term frequency
        Returns:
            float : the weighted frequency
        """
        if tf > 0:
            wf = 1 + math.log(tf)
        else:
            wf = 0
        return wf

    def get_scores(self, terms):
        """
        Creates a list of scores for each file in corpus
        The score = weighted frequency / the total word count in the file.
        Compute this score for each term in a query and sum all the scores.
        Args:
            terms (list) : a list of str
        Returns:
            list : a list of tuples, each containing the file_path_name and its relevancy score.
        """
        scores = HashTableLinear()
        keys = self.term_freqs.keys()
        for key in keys:
            scores.put(self.term_freqs[key].table[-1][0], 0)
        for item in terms:
            self.term_freqs[item].table[-1][0] /= self.doc_length(self.term_freqs.get(item))

    def rank(self, scores):
        """
        ranks files in the descending order of relevancy
        Args:
            scores(list) : a list of tuples: (file_path_name, score)
        Returns:
            list : a list of tuples: (file_path_name, score) sorted in descending order of
                relevancy
        """
        pass

    def search(self, query):
        """ search for the query terms in files.
        Args:
            query (str) : query input: e.g. “computer science”
        Returns:
            list :  a list of tuples: (file_path_name, score) sorted in descending order of
            relevancy excluding files whose relevancy score is 0.
        """
        pass


def main():
    """ The driver of the program.
    1.    It asks the user to input the path of the directory containing documents.
    2.    It creates an object of SearchEngine importing stop words, and builds
          aninverted index on the documents.
    3.    It asks the user to input a search query (keywords separated by space: e.g.computer science).
    4.    The user must prepend “s:” to a query indicating that the user wants to dosearch.
          The user must type “:q” if he/she wants to quit.
    5.    It searches for documents containing any of the keywords using the search()method.
          The method is going to return a list of tuples(file_path_name, score).
    6.    It shows a list of files (including their paths) containing the keywords
          indescending order of relevancy. You may create a helper function / method forprinting
          the list of files nicely on the screen.
    7.    Until the user types “q:” for quitting, it keeps
          asking the user to enter a newquery.    """
    pass


if __name__ == "__main__":
    main()
