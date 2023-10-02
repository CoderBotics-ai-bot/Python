"""
Source: https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort

This is a non-parallelized implementation of odd-even transposition sort.

Normally the swaps in each set happen simultaneously, without that the algorithm
is no better than bubble sort.
"""


from typing import List


def odd_even_transposition(arr: List[float]) -> List[float]:
    """
    Perform odd-even transposition sort on the given list.

    Args:
        arr (List[float]): The list to be sorted.

    Returns:
        List[float]: The sorted list.
    """
    for i in range(len(arr)):
        swap_elements(arr, i % 2)
    return arr


if __name__ == "__main__":
    arr = list(range(10, 0, -1))
    print(f"Original: {arr}. Sorted: {odd_even_transposition(arr)}")

def swap_elements(arr: List[float], start_index: int) -> None:
    """
    Swap adjacent elements in the list starting from a specific index.

    Args:
        arr (List[float]): The list in which to swap elements.
        start_index (int): The index from which to start swapping.

    Returns:
        None: The function operates on the input list and doesn't return anything.
    """
    for i in range(start_index, len(arr) - 1, 2):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
