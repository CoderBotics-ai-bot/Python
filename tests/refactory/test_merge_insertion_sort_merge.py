from sorts.merge_insertion_sort import *
import pytest


def test_merge_no_errors():
    """Tests if the function runs without throwing an error"""
    try:
        merge([[1, 3], [5, 7]], [[2, 4], [6, 8]])
    except Exception as e:
        pytest.fail(f"Test failed with error: {e}")


def test_merge_not_none():
    """Tests if the function return is not None"""
    assert (
        merge([[1, 3], [5, 7]], [[2, 4], [6, 8]]) is not None
    ), "Test failed, the function returned None"


def test_merge_ordered_sublists():
    """Tests if the function correctly merges the sublists maintaining the order"""
    assert merge([[1, 3], [5, 7]], [[2, 4], [6, 8]]) == [
        [1, 3],
        [2, 4],
        [5, 7],
        [6, 8],
    ], "Test failed, the output is not as expected"


def test_merge_empty_sublists():
    """Tests if the function correctly handles empty sublists"""
    assert merge([], []) == [], "Test failed, the output is not as expected"


def test_merge_single_element_sublists():
    """Tests if the function handles sublists with single elements"""
    assert merge([[1], [3]], [[2], [4]]) == [
        [1],
        [2],
        [3],
        [4],
    ], "Test failed, the output is not as expected"
