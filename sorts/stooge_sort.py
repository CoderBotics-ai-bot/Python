from typing import List
def stooge_sort(arr):
    """
    Examples:
    >>> stooge_sort([18.1, 0, -7.1, -1, 2, 2])
    [-7.1, -1, 0, 2, 2, 18.1]

    >>> stooge_sort([])
    []
    """
    stooge(arr, 0, len(arr) - 1)
    return arr

def stooge(arr: List[int], i: int, h: int) -> None:
    """
    The stooge function is a part of the Stooge Sort algorithm which is a recursive and inefficient sorting algorithm.
    The function takes a segment of an array defined by the indices (i, h) and sorts it.
    This function doesn't return anything as it manipulates the array in-place.

    Args:
        arr (List[int]): The array which needs to be sorted.
        i (int): The starting index of the segment which needs to be sorted.
        h (int): The ending index of the segment which needs to be sorted.

    Returns:
        None
    """
    if i >= h:
        return

    swap_if_needed(arr, i, h)

    if h - i + 1 > 2:
        t = (h - i + 1) // 3
        stooge(arr, i, h - t)
        stooge(arr, i + t, h)
        stooge(arr, i, h - t)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(stooge_sort(unsorted))


def swap_if_needed(arr: List[int], i: int, h: int) -> None:
    """
    Swap elements at index 'i' and 'h' of array 'arr' if element at 'i' is greater than element at 'h'.
    Manipulates the array in place.

    Args:
        arr (List[int]): The array in which elements may need to be swapped.
        i (int): Index of the element to compare and possibly swap.
        h (int): Index of the other element to compare and possibly swap.

    Returns:
        None
    """
    if arr[i] > arr[h]:
        arr[i], arr[h] = arr[h], arr[i]
