from __future__ import annotations

arr = [-10, -5, 0, 5, 5.1, 11, 13, 21, 3, 4, -21, -10, -5, -1, 0]
expect = [-5, 0, 5, 5.1, 11, 13, 21, -1, 4, -1, -10, -5, -1, 0, -1]


def next_greatest_element_slow(arr: list[float]) -> list[float]:
    """
    Get the Next Greatest Element (NGE) for all elements in a list.
    Maximum element present after the current one which is also greater than the
    current one.
    >>> next_greatest_element_slow(arr) == expect
    True
    """

    result = []
    arr_size = len(arr)

    for i in range(arr_size):
        next_element: float = -1
        for j in range(i + 1, arr_size):
            if arr[i] < arr[j]:
                next_element = arr[j]
                break
        result.append(next_element)
    return result


def next_greatest_element_fast(arr: list[float]) -> list[float]:
    """
    Like next_greatest_element_slow() but changes the loops to use
    enumerate() instead of range(len()) for the outer loop and
    for in a slice of arr for the inner loop.
    >>> next_greatest_element_fast(arr) == expect
    True
    """
    result = []
    for i, outer in enumerate(arr):
        next_item: float = -1
        for inner in arr[i + 1 :]:
            if outer < inner:
                next_item = inner
                break
        result.append(next_item)
    return result

def next_greatest_element(arr: list[float]) -> list[float]:
    """
    Get the Next Greatest Element (NGE) for all elements in a list.

    Args:
    arr (list[float]): List of numbers for which NGE is to be calculated.

    Returns:
    list[float]: List of NGEs for each element in the input list.
                 For any numbers without a corresponding NGE, -1 is returned.
    """
    return [find_next_greater(arr, i) for i in range(len(arr))]


if __name__ == "__main__":
    from doctest import testmod
    from timeit import timeit

    testmod()
    print(next_greatest_element_slow(arr))
    print(next_greatest_element_fast(arr))
    print(next_greatest_element(arr))

    setup = (
        "from __main__ import arr, next_greatest_element_slow, "
        "next_greatest_element_fast, next_greatest_element"
    )
    print(
        "next_greatest_element_slow():",
        timeit("next_greatest_element_slow(arr)", setup=setup),
    )
    print(
        "next_greatest_element_fast():",
        timeit("next_greatest_element_fast(arr)", setup=setup),
    )
    print(
        "     next_greatest_element():",
        timeit("next_greatest_element(arr)", setup=setup),
    )


def find_next_greater(arr: list[float], index: int) -> float:
    """
    Find the Next Greatest Element (NGE) for an element in a list.

    Args:
    arr (list[float]): List of numbers for which NGE is to be calculated.
    index (int): Position of the element for which NGE is to be calculated.

    Returns:
    float: NGE for the element at position 'index'.
           If there is no NGE, -1 is returned.
    """
    for next_index in range(index + 1, len(arr)):
        if arr[next_index] > arr[index]:
            return arr[next_index]
    return -1
