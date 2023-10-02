"""
Python program for Bitonic Sort.

Note that this program works only when size of input is a power of 2.
"""
from __future__ import annotations

def comp_and_swap(array: list[int], index1: int, index2: int, direction: int) -> None:
    """
    Compare and swap elements at `index1` and `index2` in the `array` depending on the `direction`.

    Parameters
    ----------
    array : list[int]
        The list of integers to be sorted.
    index1 : int
        The index of the first element to be compared.
    index2 : int
        The index of the second element to be compared.
    direction : int
        The direction of the sorting. 1 for ascending and 0 for descending.

    Returns
    -------
    None :
        The function modifies the input list in-place and does not return anything.

    Examples
    --------
    >>> arr = [12, 42, -21, 1]
    >>> comp_and_swap(arr, 1, 2, 1)
    >>> arr
    [12, -21, 42, 1]

    >>> comp_and_swap(arr, 1, 2, 0)
    >>> arr
    [12, 42, -21, 1]

    >>> comp_and_swap(arr, 0, 3, 1)
    >>> arr
    [1, 42, -21, 12]

    >>> comp_and_swap(arr, 0, 3, 0)
    >>> arr
    [12, 42, -21, 1]
    """
    if should_swap(array[index1], array[index2], direction):
        array[index1], array[index2] = array[index2], array[index1]


def bitonic_merge(array: list[int], low: int, length: int, direction: int) -> None:
    """
    It recursively sorts a bitonic sequence in ascending order, if direction = 1, and in
    descending if direction = 0.
    The sequence to be sorted starts at index position low, the parameter length is the
    number of elements to be sorted.

    >>> arr = [12, 42, -21, 1]
    >>> bitonic_merge(arr, 0, 4, 1)
    >>> arr
    [-21, 1, 12, 42]

    >>> bitonic_merge(arr, 0, 4, 0)
    >>> arr
    [42, 12, 1, -21]
    """
    if length > 1:
        middle = int(length / 2)
        for i in range(low, low + middle):
            comp_and_swap(array, i, i + middle, direction)
        bitonic_merge(array, low, middle, direction)
        bitonic_merge(array, low + middle, middle, direction)


def should_swap(item1: int, item2: int, direction: int) -> bool:
    """
    Determine if two items should be swapped depending on the direction

    Parameters
    ----------
    item1 : int
        The first item to be compared.
    item2 : int
        The second item to be compared.
    direction : int
        The direction of the sorting. 1 for ascending and 0 for descending.

    Returns
    -------
    bool:
        Returns True if the items need to be swapped, False otherwise.
    """
    return item1 > item2 if direction == 1 else item1 < item2


def bitonic_sort(array: list[int], low: int, length: int, direction: int) -> None:
    """
    This function first produces a bitonic sequence by recursively sorting its two
    halves in opposite sorting orders, and then calls bitonic_merge to make them in the
    same order.

    >>> arr = [12, 34, 92, -23, 0, -121, -167, 145]
    >>> bitonic_sort(arr, 0, 8, 1)
    >>> arr
    [-167, -121, -23, 0, 12, 34, 92, 145]

    >>> bitonic_sort(arr, 0, 8, 0)
    >>> arr
    [145, 92, 34, 12, 0, -23, -121, -167]
    """
    if length > 1:
        middle = int(length / 2)
        bitonic_sort(array, low, middle, 1)
        bitonic_sort(array, low + middle, middle, 0)
        bitonic_merge(array, low, length, direction)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item.strip()) for item in user_input.split(",")]

    bitonic_sort(unsorted, 0, len(unsorted), 1)
    print("\nSorted array in ascending order is: ", end="")
    print(*unsorted, sep=", ")

    bitonic_merge(unsorted, 0, len(unsorted), 0)
    print("Sorted array in descending order is: ", end="")
    print(*unsorted, sep=", ")
