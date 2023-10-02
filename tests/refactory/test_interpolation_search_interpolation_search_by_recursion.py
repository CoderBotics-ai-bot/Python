from searches.interpolation_search import *
import pytest


def test_interpolation_search_by_recursion():
    sorted_collection = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    item = 5
    result = interpolation_search_by_recursion(
        sorted_collection, item, 0, len(sorted_collection) - 1
    )
    assert result is not None


def test_interpolation_search_by_recursion_item_not_in_collection():
    sorted_collection = [1, 2, 3, 4, 6, 7, 8, 9]
    item = 5
    result = interpolation_search_by_recursion(
        sorted_collection, item, 0, len(sorted_collection) - 1
    )
    assert result is None


def test_interpolation_search_by_recursion_single_item_collection():
    sorted_collection = [5]
    item = 5
    result = interpolation_search_by_recursion(
        sorted_collection, item, 0, len(sorted_collection) - 1
    )
    assert result == 0


def test_interpolation_search_by_recursion_single_item_collection_item_not_found():
    sorted_collection = [3]
    item = 5
    result = interpolation_search_by_recursion(
        sorted_collection, item, 0, len(sorted_collection) - 1
    )
    assert result is None
