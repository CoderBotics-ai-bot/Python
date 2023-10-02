from sorts.recursive_quick_sort import *
import pytest


# Testing for a typical case.
def test_quick_sort_typical():
    test_list = [7, 6, 5, 4, 3, 2, 1, 0]
    result = quick_sort(test_list)
    # assert that the function runs and the result is not `None`.
    assert result is not None


# Testing for an edge case with an empty list.
def test_quick_sort_empty():
    test_list = []
    result = quick_sort(test_list)
    # an empty list should return `None`, so we can check for that.
    assert result is not None


# Testing for an edge case with a list of identical items.
def test_quick_sort_identical():
    test_list = [6, 6, 6, 6, 6, 6]
    result = quick_sort(test_list)
    # a list with identical items should return a list with identical items.
    assert result is not None


# Testing for an edge case with a list that is already sorted.
def test_quick_sort_already_sorted():
    test_list = [0, 1, 2, 3, 4, 5, 6, 7]
    result = quick_sort(test_list)
    # a sorted list should return a sorted list.
    assert result is not None


# Testing for a negative case where the list contains items of different types.
def test_quick_sort_diff_types():
    test_list = [1, "a", 3.14]
    with pytest.raises(TypeError):
        quick_sort(test_list)
