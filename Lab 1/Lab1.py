"""
Functions for Lab 1.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


def get_max(arr):
    """
    Get the largest number in a given list of integers.
    Args:
        arr(list): a list of integers.
    Returns:
        int: the largest integer in the list.
    """
    if len(arr) == 0:
        return None
    else:
        max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max


def reverse(string):
    """
    Reverse a string.
    Args:
        string(string): e.g. 'Forrest'.
    Returns:
        string: the previous string but reversed, e.g. 'tserroF'.
    """
    if string == "":
        return string
    else:
        return string[-1] + reverse(string[:-1])


def search(arr, val):
    """
    Searches through the given sorted list for a specified value.
    Args:
        arr(list): sorted list of integers, in ascending order.
        val(int): targeted integer.
    Returns:
        int: index of the targeted value.
    """
    if not arr:
        return None
    return search_helper(arr, val, 0, len(arr)-1)


def search_helper(arr, val, lo, hi):
    """
    Recursive helper function for search.
    Args:
        arr(list): same as above.
        val(int): same as above.
        lo(int): The first index spot of the list, starting at 0.
        hi(int): The last index spot of the list, starting at -1.
    Returns:
        int: index of the val.
    Complexity:
        O(log(n))
    """
    guess = (hi + lo) // 2
    if arr[guess] == val:
        return guess
    elif arr[guess] > val:
        hi = guess - 1
        return search_helper(arr, val, lo, hi)
    else:
        lo = guess + 1
        return search_helper(arr, val, lo, hi)


def fib(n):
    """
    Calculates the fibonacci number at the nth term.
    Args:
        n(int): depth of the fib number.
    Returns:
        int: fibonacci number
    Complexity:
        O(2^n)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def factorial_rec(n):
    """
    Calculates n! vis recursion.
    Args:
        n(int): factorial length
    Returns:
        int: n!
    """
    if n == 1:
        return n
    else:
        return factorial_rec(n-1) * n


def factorial_iter(n):
    """
    Calculates n! vis iteration
    Args:
        n(int): factorial length
    Returns:;.
        int: n!
    """
    x = n
    while n > 1:
        n -= 1
        x *= n
    return x


'''
The iterative function will return the number after a second, but the recursive
function crashes before it can get there. Python limits recursion to 997 to
prevent stack overflow, and to reach 1000! the program needs to recurse more than 
996 times. Stack overflow occurs when too many items are written to the same stack,
which can cause the code to break down, so Python artificially limits the amount
of possible recursions to prevent this.
'''

