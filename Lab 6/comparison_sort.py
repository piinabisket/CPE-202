"""
Functions for Lab 6
Course: CPE202
Quarter: Spring 2020
Author: Forrest Dudley
"""

import random
import time


def selection_sort(alist):
    size = len(alist)
    comparisons = 0
    for i in reversed(range(1, size)):
        max_index = 0
        for j in range(1, i+1):
            if alist[j] > alist[max_index]:
                max_index = j
            comparisons += 1
        alist[max_index], alist[i] = alist[i], alist[max_index]
    return comparisons


def merge_sort(alist, comparisons=0):
    length = len(alist)
    if length <= 1:
        return alist
    midpoint = length//2
    left = merge_sort(alist[:midpoint], comparisons)
    right = merge_sort(alist[midpoint:], comparisons)
    return merge(left, right, comparisons), comparisons


def merge(left, right, comparisons):
    merged = []
    if type(right) is tuple:
        right = right[0][0]
    if type(left) is tuple:
        left = left[0][0]
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
        comparisons += 1
    if left_index < len(left):
        merged = merged + left[left_index:]
    if right_index < len(right):
        merged = merged + right[right_index:]
    return merged, comparisons

