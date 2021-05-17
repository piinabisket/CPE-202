"""
Project 1 base convert function.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


def convert(num, base):
    """
        Converts a given number to a given base.
        Args:
            num(int): Number to be base-converted.
            base(int): base to convert to.
        Returns:
            str: The given base equivalent of the given number. e.g. (316, 16) == '13C'
    """
    if num == 0:
        return ""
    if num % base > 9:
        return convert(num // base, base) + chr(num % base + 55)
    return convert(num // base, base) + str(num % base)
