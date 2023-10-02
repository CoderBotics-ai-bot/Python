"""
Python implementation of the MSD radix sort algorithm.
It used the binary representation of the integers to sort
them.
https://en.wikipedia.org/wiki/Radix_sort
"""
from __future__ import annotations
from typing import List


from typing import List, Tuple



def msd_radix_sort(list_of_ints: List[int]) -> List[int]:
    """
    Implements the Most Significant Digit (MSD) radix sort algorithm and sorts a list of positive integers.

    The MSD radix sort algorithm works by sorting the numbers according to the leading digits
    (most significant digits) first, then proceeding towards the least significant digit.

    This function only works with positive integers and if there exist any negative integers in
    the list, a ValueError Exception is raised.

    Args:
    list_of_ints (List[int]): A list of positive integers that will be sorted.

    Returns:
    List[int]: A sorted list of integers.

    Raises:
    ValueError: If any number in the input list is negative.

    Examples:
    >>> msd_radix_sort([40, 12, 1, 100, 4])
    [1, 4, 12, 40, 100]

    >>> msd_radix_sort([])
    []

    >>> msd_radix_sort([123, 345, 123, 80])
    [80, 123, 123, 345]

    >>> msd_radix_sort([1209, 834598, 1, 540402, 45])
    [1, 45, 1209, 540402, 834598]

    >>> msd_radix_sort([-1, 34, 45])
    Traceback (most recent call last):
        ...
    ValueError: All numbers must be positive
    """
    if not list_of_ints:
        return []
    if min(list_of_ints) < 0:
        raise ValueError("All numbers must be positive")
    most_bits = 0 if not list_of_ints else max(len(bin(x)[2:]) for x in list_of_ints)
    return _msd_radix_sort(list_of_ints, most_bits)

def msd_radix_sort_inplace(list_of_ints: List[int]):
    """
    In-Place implementation of the MSD Radix Sort Algorithm.

    This function sorts a list of integers in-place.

    Args:
        list_of_ints (List[int]): List of integers to be sorted.

    Raises:
        ValueError: If the list contains negative integers.

    Side Effects:
        Modifies the input list in-place.

    Examples:
        >>> lst = [1, 345, 23, 89, 0, 3]
        >>> msd_radix_sort_inplace(lst)
        >>> print(lst)
        [0, 1, 3, 23, 89, 345]

        >>> lst = [1, 43, 0, 0, 0, 24, 3, 3]
        >>> msd_radix_sort_inplace(lst)
        >>> print(lst)
        [0, 0, 0, 1, 3, 3, 24, 43]

        >>> lst = []
        >>> msd_radix_sort_inplace(lst)
        >>> print(lst)
        []
    """
    list_len = len(list_of_ints)
    if list_len < 2:
        return
    if any(x < 0 for x in list_of_ints):
        raise ValueError("All numbers must be positive")

    most_bits = max(len(bin(x)[2:]) for x in list_of_ints)

    _msd_radix_sort_inplace(list_of_ints, most_bits, 0, list_len)

def _msd_radix_sort(list_of_ints: List[int], bit_position: int) -> List[int]:
    """
    Sort a list of integers using radix sort.

    Args:
        list_of_ints (List[int]): The original list of integers.
        bit_position (int): The position of the bit in the binary representation of the integers.

    Returns:
        List[int]: The sorted list.
    """
    if bit_position == 0 or len(list_of_ints) <= 1:
        return list_of_ints

    zeros, ones = split_bits(list_of_ints, bit_position)

    return _msd_radix_sort(zeros, bit_position - 1) + _msd_radix_sort(
        ones, bit_position - 1
    )


def split_bits(
    list_of_ints: List[int], bit_position: int
) -> tuple[List[int], List[int]]:
    """
    Split the list into two based on the bit at the given position.

    Args:
        list_of_ints (List[int]): The list to split.
        bit_position (int): The position of the bit in the binary representation of the integers.

    Returns:
        Tuple of two lists - one with numbers having 0 at bit_position, another with 1.
    """
    zeros = [
        number for number in list_of_ints if not (number >> (bit_position - 1)) & 1
    ]
    ones = [number for number in list_of_ints if (number >> (bit_position - 1)) & 1]

    return zeros, ones


def _msd_radix_sort_inplace(
    list_of_ints: list[int], bit_position: int, begin_index: int, end_index: int
):
    """
    Sort the given list based on the bit at bit_position. Numbers with a
    0 at that position will be at the start of the list, numbers with a
    1 at the end.
    >>> lst = [45, 2, 32, 24, 534, 2932]
    >>> _msd_radix_sort_inplace(lst, 1, 0, 3)
    >>> lst == [32, 2, 45, 24, 534, 2932]
    True
    >>> lst = [0, 2, 1, 3, 12, 10, 4, 90, 54, 2323, 756]
    >>> _msd_radix_sort_inplace(lst, 2, 4, 7)
    >>> lst == [0, 2, 1, 3, 12, 4, 10, 90, 54, 2323, 756]
    True
    """
    if bit_position == 0 or end_index - begin_index <= 1:
        return

    bit_position -= 1

    i = begin_index
    j = end_index - 1
    while i <= j:
        changed = False
        if not (list_of_ints[i] >> bit_position) & 1:
            # found zero at the beginning
            i += 1
            changed = True
        if (list_of_ints[j] >> bit_position) & 1:
            # found one at the end
            j -= 1
            changed = True

        if changed:
            continue

        list_of_ints[i], list_of_ints[j] = list_of_ints[j], list_of_ints[i]
        j -= 1
        if j != i:
            i += 1

    _msd_radix_sort_inplace(list_of_ints, bit_position, begin_index, i)
    _msd_radix_sort_inplace(list_of_ints, bit_position, i, end_index)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
