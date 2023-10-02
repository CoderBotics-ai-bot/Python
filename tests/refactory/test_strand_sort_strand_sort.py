from sorts.strand_sort import *
import pytest


def test_strand_sort_no_errors():
    """
    Test if strand_sort doesn't throw any errors and returns not None value
    """
    result = strand_sort([4, 2, 5, 3, 0, 1])
    assert result is not None


def test_strand_sort_ascending_order():
    """
    Test if strand_sort correctly sorts an array in ascending order
    """
    result = strand_sort([4, 2, 5, 3, 0, 1])
    assert result == [0, 1, 2, 3, 4, 5]


def test_strand_sort_descending_order():
    """
    Test if strand_sort correctly sorts an array in descending order if reverse parameter is set to True
    """
    result = strand_sort([4, 2, 5, 3, 0, 1], True)
    assert result == [5, 4, 3, 2, 1, 0]


def test_strand_sort_empty_array():
    """
    Test if strand_sort return an empty array if input array is empty
    """
    result = strand_sort([])
    assert result == []
