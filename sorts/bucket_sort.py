#!/usr/bin/env python3
"""
Illustrate how to implement bucket sort algorithm.

Author: OMKAR PATHAK
This program will illustrate how to implement bucket sort algorithm

Wikipedia says: Bucket sort, or bin sort, is a sorting algorithm that works
by distributing the elements of an array into a number of buckets.
Each bucket is then sorted individually, either using a different sorting
algorithm, or by recursively applying the bucket sorting algorithm. It is a
distribution sort, and is a cousin of radix sort in the most to least
significant digit flavour.
Bucket sort is a generalization of pigeonhole sort. Bucket sort can be
implemented with comparisons and therefore can also be considered a
comparison sort algorithm. The computational complexity estimates involve the
number of buckets.

Time Complexity of Solution:
Worst case scenario occurs when all the elements are placed in a single bucket.
The overall performance would then be dominated by the algorithm used to sort each
bucket. In this case, O(n log n), because of TimSort

Average Case O(n + (n^2)/k + k), where k is the number of buckets

If k = O(n), time complexity is O(n)

Source: https://en.wikipedia.org/wiki/Bucket_sort
"""
from __future__ import annotations


from typing import List



def bucket_sort(my_list: List[int]) -> List[int]:
    """
    A bucket sort algorithm implementation in Python.

    The function sorts an integer list in ascending order using the bucket sort algorithm.
    It uses the difference of the maximum and minimum values to create the bucket count

    If list is empty, the function returns an empty list

    Args:
        my_list (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The same list of integers, but sorted in ascending order.

    Raises:
        AssertionError: If the input list does not contain integers.
    """
    if not my_list:
        return []

    min_value, bucket_count = setup_buckets(my_list)

    buckets: list[list] = [[] for _ in range(bucket_count)]

    sort_into_buckets(my_list, min_value, buckets)

    return flatten_buckets(buckets)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    assert bucket_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bucket_sort([0, 1, -10, 15, 2, -2]) == [-10, -2, 0, 1, 2, 15]


def setup_buckets(my_list):
    min_value, max_value = min(my_list), max(my_list)
    bucket_count = int(max_value - min_value) + 1
    return min_value, bucket_count


def sort_into_buckets(my_list, min_value, buckets):
    for i in my_list:
        buckets[int(i - min_value)].append(i)


def flatten_buckets(buckets):
    return [v for bucket in buckets for v in sorted(bucket)]
