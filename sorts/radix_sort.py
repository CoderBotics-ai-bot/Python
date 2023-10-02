"""
This is a pure Python implementation of the radix sort algorithm

Source: https://en.wikipedia.org/wiki/Radix_sort
"""
from __future__ import annotations

RADIX = 10


def radix_sort(list_of_ints: list[int]) -> list[int]:
    """
    Implement the radix sort algorithm.
    Radix sort is a sorting algorithm that sorts integers by processing individual
    digits. Numbers with more digits come before numbers with same initial digits.
    It uses a stable sort algorithm (like counting sort) to sort digits in each
    significant place of the numbers.

    This function only works for positive integers.
    Negative integers and floating point numbers are not supported.
    """
    max_digit = max(list_of_ints)
    place = 1
    while place <= max_digit:
        buckets = _init_buckets()
        _place_in_buckets(list_of_ints, place, buckets)
        _collate_buckets(buckets, list_of_ints)
        place *= RADIX
    return list_of_ints


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def _init_buckets() -> list[list]:
    """Initialize buckets for storing numbers."""
    return [[] for _ in range(RADIX)]


def _place_in_buckets(nums: list[int], place: int, buckets: list[list]) -> None:
    """Place each number in its corresponding bucket based on the digit at current place."""
    for num in nums:
        digit = num // place % RADIX
        buckets[digit].append(num)


def _collate_buckets(buckets: list[list], nums: list[int]) -> None:
    """Replace the original list with numbers collated from each bucket in order."""
    index = 0
    for bucket in buckets:
        for num in bucket:
            nums[index] = num
            index += 1
