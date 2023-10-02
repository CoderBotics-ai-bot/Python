#!/usr/bin/env python3

"""
This is pure Python implementation of binary search algorithms

For doctests run following command:
python3 -m doctest -v binary_search.py

For manual testing run:
python3 binary_search.py
"""
from __future__ import annotations

import bisect
from typing import List

def bisect_left(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> int:
    """Thin wrapper around Python's built-in `bisect.bisect_left` function."""
    if hi < 0:
        hi = len(sorted_collection)
    return bisect.bisect_left(sorted_collection, item, lo, hi)

def bisect_right(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> int:
    """
    Locates the insertion point in a sorted collection to maintain sorted order if the item
    is inserted at that position.

    The sorted_collection must be sorted in ascending order.
    The function uses binary search to find the insertion index.

    :param sorted_collection: list[int] Sorted list of integers.
    :param item: int An integer which needs to be inserted.
    :param lo: int Lowest index; defaults to 0 which means considering the whole list.
    :param hi: int Highest index; defaults to -1 which means considering the whole list.

    :return: The index where the item can be inserted while maintaining the sorted order of the list.
    """
    return bisect.bisect_right(
        sorted_collection, item, lo, hi if hi >= 0 else len(sorted_collection)
    )


def insort_left(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> None:
    """
    Inserts a given value into a sorted array before other values with the same value.

    It has the same interface as
    https://docs.python.org/3/library/bisect.html#bisect.insort_left .

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item to insert
    :param lo: lowest index to consider (as in sorted_collection[lo:hi])
    :param hi: past the highest index to consider (as in sorted_collection[lo:hi])

    Examples:
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_left(sorted_collection, 6)
    >>> sorted_collection
    [0, 5, 6, 7, 10, 15]

    >>> sorted_collection = [(0, 0), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item = (5, 5)
    >>> insort_left(sorted_collection, item)
    >>> sorted_collection
    [(0, 0), (5, 5), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item is sorted_collection[1]
    True
    >>> item is sorted_collection[2]
    False

    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_left(sorted_collection, 20)
    >>> sorted_collection
    [0, 5, 7, 10, 15, 20]

    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_left(sorted_collection, 15, 1, 3)
    >>> sorted_collection
    [0, 5, 7, 15, 10, 15]
    """
    sorted_collection.insert(bisect_left(sorted_collection, item, lo, hi), item)


def insort_right(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> None:
    """
    Inserts a given value into a sorted array after other values with the same value.

    It has the same interface as
    https://docs.python.org/3/library/bisect.html#bisect.insort_right .

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item to insert
    :param lo: lowest index to consider (as in sorted_collection[lo:hi])
    :param hi: past the highest index to consider (as in sorted_collection[lo:hi])

    Examples:
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_right(sorted_collection, 6)
    >>> sorted_collection
    [0, 5, 6, 7, 10, 15]

    >>> sorted_collection = [(0, 0), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item = (5, 5)
    >>> insort_right(sorted_collection, item)
    >>> sorted_collection
    [(0, 0), (5, 5), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item is sorted_collection[1]
    False
    >>> item is sorted_collection[2]
    True

    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_right(sorted_collection, 20)
    >>> sorted_collection
    [0, 5, 7, 10, 15, 20]

    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_right(sorted_collection, 15, 1, 3)
    >>> sorted_collection
    [0, 5, 7, 15, 10, 15]
    """
    sorted_collection.insert(bisect_right(sorted_collection, item, lo, hi), item)

def binary_search(sorted_collection: List[int], item: int) -> int | None:
    """
    Execute binary search algorithm on a sorted collection.

    This is a pure Python implementation of the binary search algorithm. The function
    makes use of the Python built-in function bisect_left from the standard library's
    bisect module. It takes an ascending sorted collection and an item to search for.
    It returns the index of the item if found, or None if the item is not in the collection.
    Please note that if the collection is not sorted in ascending order,
    the result will be unpredictable.

    Args:
        sorted_collection (List[int]): A list of integers, sorted in ascending order.
        item (int): The integer item to search for in the collection.

    Returns:
        int | None: The index of the item if found, or None if the item is not found.

    Examples:
        >>> binary_search([0, 5, 7, 10, 15], 0)
        0

        >>> binary_search([0, 5, 7, 10, 15], 15)
        4

        >>> binary_search([0, 5, 7, 10, 15], 5)
        1

        >>> binary_search([0, 5, 7, 10, 15], 6)

    """
    position = bisect.bisect_left(sorted_collection, item)

    # return position if item is present in collection
    if position != len(sorted_collection) and sorted_collection[position] == item:
        return position

    # item not present in sorted_collection
    return None


def binary_search_std_lib(sorted_collection: list[int], item: int) -> int | None:
    """Pure implementation of binary search algorithm in Python using stdlib

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 6)

    """
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return None

def binary_search_by_recursion(
    sorted_collection: List[int], item: int, left: int, right: int
) -> int | None:
    """Perform Binary Search on a Sorted Collection with Recursion

    If the item is not within the given slice (left:right) of the sorted collection, None is returned.
    If the item is found, the function returns the item's index within the entire collection, not the slice.

    Args:
        sorted_collection: A collection sorted in ascending order.
        item: The item to search for in the sorted collection.
        left: The leftmost index from where to start the search.
        right: The rightmost index up to which to search.

    Returns:
        The index of the item if found, else None.
    """

    # If the slice of the list does not exist, item is not found
    if right < left:
        return None

    midpoint = (left + right) // 2

    # If item is found at the midpoint
    if sorted_collection[midpoint] == item:
        return midpoint

    # If item is larger than the midpoint value, search in the right half
    if sorted_collection[midpoint] < item:
        return binary_search_by_recursion(sorted_collection, item, midpoint + 1, right)

    # If item is smaller midpoint value, search in the left half
    return binary_search_by_recursion(sorted_collection, item, left, midpoint - 1)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    collection = sorted(int(item) for item in user_input.split(","))
    target = int(input("Enter a single number to be found in the list:\n"))
    result = binary_search(collection, target)
    if result is None:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at position {result} in {collection}.")
