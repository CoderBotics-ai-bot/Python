"""
A Python implementation of the quick select algorithm, which is efficient for
calculating the value that would appear in the index of a list if it would be
sorted, even if it is not already sorted
https://en.wikipedia.org/wiki/Quickselect
"""
import random


from typing import List, Tuple

def _partition(data: List[int], pivot: int) -> Tuple[List[int], List[int], List[int]]:
    """
    Partitions the data into three lists: less than, equal to, and greater than the pivot.

    This function performs a three-way partition of the data based on the pivot. It divides
    the data into three lists:
        1. Numbers less than the pivot.
        2. Numbers equal to the pivot.
        3. Numbers greater than the pivot.

    Args:
        data (List[int]): The data to be sorted.
        pivot (int): The value to partition the data on.

    Returns:
        Tuple[List[int], List[int], List[int]]: A tuple containing three lists: numbers less than,
        equal to, and greater than the pivot.

    """
    less = [x for x in data if x < pivot]
    equal = [x for x in data if x == pivot]
    greater = [x for x in data if x > pivot]

    return less, equal, greater


def quick_select(items: list, index: int):
    """
    >>> quick_select([2, 4, 5, 7, 899, 54, 32], 5)
    54
    >>> quick_select([2, 4, 5, 7, 899, 54, 32], 1)
    4
    >>> quick_select([5, 4, 3, 2], 2)
    4
    >>> quick_select([3, 5, 7, 10, 2, 12], 3)
    7
    """
    # index = len(items) // 2 when trying to find the median
    #   (value of index when items is sorted)

    # invalid input
    if index >= len(items) or index < 0:
        return None

    pivot = items[random.randint(0, len(items) - 1)]
    count = 0
    smaller, equal, larger = _partition(items, pivot)
    count = len(equal)
    m = len(smaller)

    # index is the pivot
    if m <= index < m + count:
        return pivot
    # must be in smaller
    elif m > index:
        return quick_select(smaller, index)
    # must be in larger
    else:
        return quick_select(larger, index - (m + count))
