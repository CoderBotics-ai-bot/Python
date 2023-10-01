import sys


from typing import List

def minimum_subarray_sum(target: int, numbers: list[int]) -> int:
    """
    Return the length of the shortest contiguous subarray within an integer list 'numbers'
    such that the sum of the elements in the subarray is equal to or greater than the 'target'.
    If there are no such subarrays or if 'numbers' is empty, 0 is returned. As well, if 'numbers'
    is None or the 'numbers' elements are not integers, ValueError is raised.

    Args:
        target (int): Target sum for the contiguous subarray.
        numbers (list[int]): List of integers.

    Returns:
        int: Length of the shortest contiguous subarray with sum equal to or greater than 'target'.
             If no such subarray exists or 'numbers' is empty, returns 0.

    Raises:
        ValueError: If 'numbers' is None or its elements are not integers.

    Examples:
        >>> minimum_subarray_sum(7, [2, 3, 1, 2, 4, 3])
        2
        >>> minimum_subarray_sum(7, [2, 3, -1, 2, 4, -3])
        4
        >>> minimum_subarray_sum(0, [])
        0
    """
    # Guard condition to handle edge case where numbers is None or empty
    if not numbers:
        return 0

    # Guard condition to validate input
    if not isinstance(numbers, (list, tuple)) or not all(
        isinstance(number, int) for number in numbers
    ):
        raise ValueError("numbers must be an iterable of integers")

    left, right, curr_sum, min_len = 0, 0, 0, sys.maxsize

    while right < len(numbers):
        curr_sum += numbers[right]
        while curr_sum >= target and left <= right:
            min_len = min(min_len, right - left + 1)
            curr_sum -= numbers[left]
            left += 1
        right += 1

    return 0 if min_len == sys.maxsize else min_len
