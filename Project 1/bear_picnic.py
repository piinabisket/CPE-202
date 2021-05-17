"""
Project 1 bear picnic function.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


def bears(num):
    """
        Determines if the number of given bears can conclude to 42 through a series
        of rules:
            1. If n is even, then you may give back n/2 bears.
            2. If n is divisible by 3 or 4, then you may multiply the last
               two digits of n and give back this many bears.
            3. If n is divisible by 5, then you may give back 42 bears.
            4. In each turn, you must give some bears back until you end up with 42 bears:
               If you are stuck in a situation where you can only give 0 bear back,
               the function shall return False.
            5. If the number of bears is less than 42, the function shall return False.
        Args:
            num(int): Number of initially given bears.
        Returns:
            bool: True or False, depending on if the number of bears can reach 42.
    """
    if num == 42:
        return True
    if num < 42:
        return False
    if num % 2 == 0 or num == 0:
        if bears(int(num / 2)):
            return True
    if num % 5 == 0:
        if bears(num - 42):
            return True
    if num % 3 == 0 or num % 4 == 0:
        num_str = str(int(num))
        remainders = int(num_str[-1]) * int(num_str[-2])
        if remainders > 0 and bears(num - remainders):
            return True
    return False
