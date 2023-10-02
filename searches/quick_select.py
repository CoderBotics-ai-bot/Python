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

def quick_select(items: List[int], index: int) -> int:
    """
    Performs the Quickselect algorithm to find the `index`-th smallest item in items.
    Returns None if `index` is not a valid index within `items`.
    """
    if not is_valid_index(index, len(items)):
        return None

    pivot = choose_pivot(items)
    smaller, equal, larger = partition(items, pivot)

    return handle_partitions(index, pivot, smaller, equal, larger)


def is_valid_index(index: int, length: int) -> bool:
    """
    Check if the provided index is within the valid range of the list length.
    """
    return 0 <= index < length


def choose_pivot(items: List[int]) -> int:
    """
    Choose a random pivot from the given list of items.
    """
    return items[random.randint(0, len(items) - 1)]


def handle_partitions(
    index: int, pivot: int, smaller: List[int], equal: List[int], larger: List[int]
) -> int:
    """
    Determine which partition the index falls into and handle accordingly.
    """
    m = len(smaller)

    if m <= index < m + len(equal):
        return pivot  # index is within the 'equal' partition
    elif m > index:
        return quick_select(smaller, index)  # index is within the 'smaller' partition
    else:
        return quick_select(
            larger, index - m - len(equal)
        )  # index is within the 'larger' partition


def partition(data: List[int], pivot: int) -> Tuple[List[int], List[int], List[int]]:
    """
    Helper function for partitioning the data into three lists:
    elements less than the pivot, elements equal to the pivot, and elements greater than the pivot.
    """
    smaller, equal, greater = [], [], []
    for element in data:
        if element < pivot:
            smaller.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    return smaller, equal, greater
