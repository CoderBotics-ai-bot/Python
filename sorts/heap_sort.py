"""
This is a pure Python implementation of the heap sort algorithm.

For doctests run following command:
python -m doctest -v heap_sort.py
or
python3 -m doctest -v heap_sort.py

For manual testing run:
python heap_sort.py
"""


from typing import List


def heapify(unsorted: List[int], index: int, heap_size: int) -> None:
    """
    Transform list into heap, in-place, in O(len(unsorted)) time.

    Args:
    unsorted  : List of integers
    index     : Integer
    heap_size : Integer

    This function transforms the given list of integers into a heap structure,
    in-place, in linear time. A heap is a complete binary tree, where each node
    is greater than or equal to its child nodes.
    """
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size:
        largest = swap_if_greater(unsorted, largest, left_index)

    if right_index < heap_size:
        largest = swap_if_greater(unsorted, largest, right_index)

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    """
    Pure implementation of the heap sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> heap_sort([])
    []

    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted

def swap_if_greater(unsorted: List[int], first_index: int, second_index: int) -> int:
    """
    Swap two elements in the list if the element at the first index is greater than the element at the second index.

    Args:
    unsorted     : List of integers
    first_index  : Index of the first element
    second_index : Index of the second element

    Returns:
    The new index of the element that was at the first index
    """
    if unsorted[first_index] > unsorted[second_index]:
        unsorted[first_index], unsorted[second_index] = (
            unsorted[second_index],
            unsorted[first_index],
        )
        return first_index
    return second_index


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(heap_sort(unsorted))
