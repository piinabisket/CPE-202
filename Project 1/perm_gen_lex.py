"""
Project 1 permutations function.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


def perm_gen_lex(lex):
    """
        Recursive function that returns all possible permutations of lower-case letters
        in alphabetical order.
        Args:
            input(str): A lower-case, alphabetically ordered string of letters.
        Returns:
            list: A list of all possible permutations of that string in lexicographic order.
                  e.g. 'abc' would be ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    permutations = []
    if len(lex) == 0:
        return permutations
    for i in range(len(lex)):
        char = lex[i]
        simple = perm_gen_lex(lex.replace(lex[i], ""))
        if len(simple) == 0:
            permutations += char
        else:
            for string in simple:
                permutations.append(char + string)
    return permutations
