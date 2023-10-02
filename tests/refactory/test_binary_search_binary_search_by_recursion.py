from searches.binary_search import *
import pytest


def test_binary_search_by_recursion_no_errors():
    assert binary_search_by_recursion([0, 5, 7, 10, 15], 15, 0, 4) is not None


def test_binary_search_by_recursion_none_return():
    assert binary_search_by_recursion([0, 5, 7, 10, 15], 6, 0, 4) is None


def test_binary_search_by_recursion_item_at_start():
    assert binary_search_by_recursion([0, 5, 7, 10, 15], 0, 0, 4) == 0


def test_binary_search_by_recursion_item_at_end():
    assert binary_search_by_recursion([0, 5, 7, 10, 15], 15, 0, 4) == 4


def test_binary_search_by_recursion_item_in_middle():
    assert binary_search_by_recursion([0, 5, 7, 10, 15], 7, 0, 4) == 2


def test_binary_search_by_recursion_different_lengths():
    assert binary_search_by_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 0, 9) == 5
    assert binary_search_by_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 0, 8) == 2


def test_binary_search_by_recursion_empty_list():
    assert binary_search_by_recursion([], 1, 0, -1) is None


def test_binary_search_by_recursion_single_element_list():
    assert binary_search_by_recursion([1], 1, 0, 0) == 0
    assert binary_search_by_recursion([1], 2, 0, 0) is None


None
