from sorts.strand_sort import *
import pytest


def test_strand_sort():
    # Test with positive integers
    assert strand_sort([4, 2, 5, 3, 0, 1]) == [0, 1, 2, 3, 4, 5]
    assert strand_sort([4, 2, 5, 3, 0, 1], reverse=True) == [5, 4, 3, 2, 1, 0]

    # Test with negative integers
    assert strand_sort([-5, -1, -4, 2, 0]) == [-5, -4, -1, 0, 2]
    assert strand_sort([-5, -1, -4, 2, 0], reverse=True) == [2, 0, -1, -4, -5]

    # Test with repeating elements
    assert strand_sort([2, 2, 5, 3, 2, 1]) == [1, 2, 2, 2, 3, 5]
    assert strand_sort([2, 2, 5, 3, 2, 1], reverse=True) == [5, 3, 2, 2, 2, 1]

    # Test with an empty list
    assert strand_sort([]) == []
    assert strand_sort([], reverse=True) == []

    # Test with a list of same elements
    assert strand_sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]

    # Test with a list of one element
    assert strand_sort([1]) == [1]
