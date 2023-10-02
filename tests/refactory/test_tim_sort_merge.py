from sorts.tim_sort import *
import pytest


def test_merge_valid_elements():
    """
    Test merge function with normal conditions
    """
    result = merge([2, 5, 6], [1, 8, 9])
    assert result is not None, "The result shouldn't be None"


def test_merge_empty_left_list():
    """
    Test merge function with left list empty
    """
    result = merge([], [1, 2, 3])
    assert result is not None, "The result shouldn't be None"
    assert result == [
        1,
        2,
        3,
    ], "The result should be equal to the right list if the left one is empty"


def test_merge_empty_right_list():
    """
    Test merge function with right list empty
    """
    result = merge([1, 2, 3], [])
    assert result is not None, "The result shouldn't be None"
    assert result == [
        1,
        2,
        3,
    ], "The result should be equal to the left list if the right one is empty"


def test_merge_empty_lists():
    """
    Test merge function with both lists empty
    """
    result = merge([], [])
    assert result is not None, "The result shouldn't be None"
    assert result == [], "The result should be an empty list if both lists are empty"
