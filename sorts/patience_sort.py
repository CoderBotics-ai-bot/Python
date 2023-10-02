from __future__ import annotations

from bisect import bisect_left
from functools import total_ordering
from heapq import merge

"""
A pure Python implementation of the patience sort algorithm

For more information: https://en.wikipedia.org/wiki/Patience_sorting

This algorithm is based on the card game patience

For doctests run following command:
python3 -m doctest -v patience_sort.py

For manual testing run:
python3 patience_sort.py
"""


@total_ordering
class Stack(list):
    def __lt__(self, other):
        return self[-1] < other[-1]

    def __eq__(self, other):
        return self[-1] == other[-1]


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(patience_sort(unsorted))

def patience_sort(collection: list) -> list:
    """Sorts a collection in ascending order using patience sort algorithm.

    Args:
        collection (List[Any]): The list to be sorted.

    Returns:
        List[Any]: The sorted list.
    """
    if isinstance(collection, list) and len(collection) > 0:
        stacks: list = _create_stacks(collection)
        _merge_stacks(stacks, collection)
    return collection


def _create_stacks(collection: list) -> list:
    """Creates stacks from the input collection.

    Args:
        collection (List[Any]): The list to be sorted.

    Returns:
        List[List[Any]]: The list of stacks.
    """
    stacks: list = []
    for element in collection:
        new_stack = Stack([element])
        i = bisect_left(stacks, new_stack)
        if i != len(stacks):
            stacks[i].append(element)
        else:
            stacks.append(new_stack)
    return stacks


def _merge_stacks(stacks: list, collection: list):
    """Merges the sorted stacks back into the collection.

    Args:
        stacks (List[List[Any]]): The sorted stacks.
        collection (List[Any]): The list into which the merged stacks are put.
    """
    collection[:] = merge(*(reversed(stack) for stack in stacks))
