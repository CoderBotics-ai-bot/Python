"""
The maximum subarray sum problem is the task of finding the maximum sum that can be
obtained from a contiguous subarray within a given array of numbers. For example, given
the array [-2, 1, -3, 4, -1, 2, 1, -5, 4], the contiguous subarray with the maximum sum
is [4, -1, 2, 1], so the maximum subarray sum is 6.

Kadane's algorithm is a simple dynamic programming algorithm that solves the maximum
subarray sum problem in O(n) time and O(1) space.

Reference: https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""
from collections.abc import Sequence

def max_subarray_sum(
    arr: Sequence[float], allow_empty_subarrays: bool = False
) -> float:
    """
    Solves the maximum subarray sum problem using Kadane's algorithm.
    :param arr: the given array of numbers
    :param allow_empty_subarrays: if True, then the algorithm considers empty subarrays
    :return: maximum subarray sum
    """
    if not arr:
        return 0.0

    max_sum = 0.0 if allow_empty_subarrays else float("-inf")
    curr_sum = 0.0

    for num in arr:
        curr_sum_candidate = curr_sum + num
        curr_sum = max(0 if allow_empty_subarrays else num, curr_sum_candidate)
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"{max_subarray_sum(nums) = }")
