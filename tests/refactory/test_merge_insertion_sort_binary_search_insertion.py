from sorts.merge_insertion_sort import *
import pytest


def test_binary_search_insertion_no_errors():
    """Tests if the binary_search_insertion function executes without errors"""
    try:
        binary_search_insertion([2, 4, 6, 8, 10], 5)
    except Exception as e:
        assert False, f"Exception occurred: {e}"
    assert True


def test_binary_search_insertion_not_none():
    """Tests if the binary_search_insertion function returns a not None value"""
    result = binary_search_insertion([2, 4, 6, 8, 10], 5)
    assert result is not None, "Returned result is None"


def test_binary_search_insertion_insert_correct_position():
    """Tests if the binary_search_insertion function correctly inserts the given item at the right position"""
    result = binary_search_insertion([1, 2, 4, 6], 5)
    assert result == [
        1,
        2,
        4,
        5,
        6,
    ], "The item was not inserted at the correct position"


def test_binary_search_insertion_empty_list():
    """Tests if the binary_search_insertion function handles empty list"""
    result = binary_search_insertion([], 5)
    assert result == [5], "The function does not handle empty list correctly"


def test_binary_search_insertion_negative_numbers():
    """Tests if the binary_search_insertion function handles negative numbers correctly"""
    result = binary_search_insertion([-5, -3, -1], -4)
    assert result == [
        -5,
        -4,
        -3,
        -1,
    ], "The function does not handle negative numbers correctly"
