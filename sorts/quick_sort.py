"""
A pure Python implementation of the quick sort algorithm

For doctests run following command:
python3 -m doctest -v quick_sort.py

For manual testing run:
python3 quick_sort.py
"""
from __future__ import annotations

from random import randrange


from typing import List, Tuple


def quick_sort(collection: List[int]) -> List[int]:
    """Sort the input collection in ascending order using quicksort algorithm."""

    if len(collection) < 2:
        return collection

    pivot, pivot_index = select_pivot(collection)
    lesser, greater = divide_elements(collection, pivot, pivot_index)

    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(quick_sort(unsorted))

def select_pivot(collection: List[int]) -> Tuple[int, int]:
    """Randomly select a pivot and its index."""

    pivot_index = randrange(len(collection))
    pivot = collection[pivot_index]

    return pivot, pivot_index


def divide_elements(
    collection: List[int], pivot: int, pivot_index: int
) -> Tuple[List[int], List[int]]:
    """Divide collection into lists of elements lesser and greater than the pivot."""

    lesser, greater = [], []

    for i, element in enumerate(collection):
        if i == pivot_index:
            continue
        if element > pivot:
            greater.append(element)
        else:
            lesser.append(element)

    return lesser, greater
