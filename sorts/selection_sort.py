"""
This is a pure Python implementation of the selection sort algorithm

For doctests run following command:
python -m doctest -v selection_sort.py
or
python3 -m doctest -v selection_sort.py

For manual testing run:
python selection_sort.py
"""


from typing import List, TypeVar

Comparable = TypeVar("Comparable")

def selection_sort(collection: List[Comparable]) -> List[Comparable]:
    """
    Pure implementation of the selection sort algorithm in Python.

    This function sorts mutable ordered collections with heterogeneous comparable
    items inside in ascending order. It uses the selection sort algorithm, which
    iteratively selects the smallest or largest element from the unsorted section
    and moves it to the end of the sorted section.

    Args:
        collection (List[Comparable]): The collection to be sorted.

    Returns:
        List[Comparable]: The same collection sorted in ascending order.

    Examples:
        >>> selection_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]

        >>> selection_sort([])
        []

        >>> selection_sort([-2, -5, -45])
        [-45, -5, -2]
    """

    for i in range(len(collection) - 1):
        least = min(range(i, len(collection)), key=collection.__getitem__)
        collection[i], collection[least] = collection[least], collection[i]  # Swap

    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(selection_sort(unsorted))
