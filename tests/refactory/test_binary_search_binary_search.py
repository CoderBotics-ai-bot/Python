from searches.binary_search import *
import pytest


@pytest.fixture
def sorted_list():
    return [0, 5, 7, 10, 15]


def test_binary_search_no_errors(sorted_list):
    """Test that the function doesn't throw an error"""
    item = 7
    binary_search(sorted_list, item)


def test_binary_search_none_return(sorted_list):
    """Test that the function returns None when the item is not found"""
    assert binary_search(sorted_list, 100) is None


def test_binary_search_item_at_start(sorted_list):
    """Test that the function returns the correct index for an item at the start of the list"""
    assert binary_search(sorted_list, 0) == 0


def test_binary_search_item_at_end(sorted_list):
    """Test that the function returns the correct index for an item at the end of the list"""
    assert binary_search(sorted_list, 15) == 4


def test_binary_search_item_in_middle(sorted_list):
    """Test that the function returns the correct index for an item in the middle of the list"""
    assert binary_search(sorted_list, 7) == 2


def test_binary_search_empty_list():
    """Test that the function returns None when an empty list is provided"""
    assert binary_search([], 5) is None


def test_binary_search_large_list():
    """Test that the function works correctly for large lists"""
    assert binary_search(list(range(1000000)), 999999) == 999999


def test_binary_search_negative_numbers():
    """Test that the function works correctly for lists with negative numbers"""
    assert binary_search([-10, -5, 0, 5, 10], -5) == 1
