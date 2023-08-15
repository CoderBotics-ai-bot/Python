"""
Given an array of integers and another integer target,
we are required to find a triplet from the array such that it's sum is equal to
the target.
"""
from __future__ import annotations

from itertools import permutations
from random import randint
from timeit import repeat


def make_dataset() -> tuple[list[int], int]:
    arr = [randint(-1000, 1000) for i in range(10)]
    r = randint(-5000, 5000)
    return (arr, r)


dataset = make_dataset()


def triplet_sum1(arr: list[int], target: int) -> tuple[int, ...]:
    """
    Returns a triplet in the array with sum equal to target,
    else (0, 0, 0).
    >>> triplet_sum1([13, 29, 7, 23, 5], 35)
    (5, 7, 23)
    >>> triplet_sum1([37, 9, 19, 50, 44], 65)
    (9, 19, 37)
    >>> arr = [6, 47, 27, 1, 15]
    >>> target = 11
    >>> triplet_sum1(arr, target)
    (0, 0, 0)
    """
    for triplet in permutations(arr, 3):
        if sum(triplet) == target:
            return tuple(sorted(triplet))
    return (0, 0, 0)


def triplet_sum2(arr: list[int], target: int) -> tuple[int, int, int]:
    """
    Searches a sorted list for three values whose sum equals a given target.

    Args:
        arr: An input list of whole numbers. The function doesn't mutate the original list.
        target: The target sum the function tries to achieve by the sum of three numbers from the list.

    Returns:
        A tuple with three elements if such a triplet exists, in ascending order.
        If the function doesn't find any triplet with given sum, it returns a tuple with three zeros.
    """
    arr.sort()
    for i in range(len(arr) - 1):
        triplet = find_triplet(arr, target, i, i + 1)
        if triplet != (0, 0, 0):
            return triplet
    return (0, 0, 0)


def solution_times() -> tuple[float, float]:
    setup_code = """
from __main__ import dataset, triplet_sum1, triplet_sum2
"""
    test_code1 = """
triplet_sum1(*dataset)
"""
    test_code2 = """
triplet_sum2(*dataset)
"""
    times1 = repeat(setup=setup_code, stmt=test_code1, repeat=5, number=10000)
    times2 = repeat(setup=setup_code, stmt=test_code2, repeat=5, number=10000)
    return (min(times1), min(times2))



def find_triplet(
    arr: list[int], target: int, i: int, left: int
) -> tuple[int, int, int]:
    """
    Helper function to find a triplet that sums to target in a sorted list using two pointers technique.

    Args:
        arr: A sorted list of integers.
        target: Target sum.
        i: Current index.
        left: Left index.

    Returns:
        A tuple containing the triplet if found, else a tuple of zeros.
    """
    right = len(arr) - 1
    while left < right:
        current_sum = arr[i] + arr[left] + arr[right]
        if current_sum == target:
            return (arr[i], arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return (0, 0, 0)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    times = solution_times()
    print(f"The time for naive implementation is {times[0]}.")
    print(f"The time for optimized implementation is {times[1]}.")
