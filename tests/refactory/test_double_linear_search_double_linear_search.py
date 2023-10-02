import pytest
from searches.double_linear_search import *


import pytest


def test_double_linear_search_no_errors():
    try:
        double_linear_search([1, 2, 3, 4, 5], 3)
    except Exception as e:
        pytest.fail(f"double_linear_search function raised an error: {e}")


def test_double_linear_search_not_none():
    assert double_linear_search([1, 2, 3, 4, 5], 3) is not None


def test_double_linear_search_item_is_in_array_start():
    assert double_linear_search([1, 2, 3, 4, 5], 1) == 0


def test_double_linear_search_item_is_in_array_end():
    assert double_linear_search([1, 2, 3, 4, 5], 5) == 4


def test_double_linear_search_item_is_in_array_middle():
    assert double_linear_search([1, 2, 3, 4, 5], 3) == 2


def test_double_linear_search_item_is_not_in_array():
    assert double_linear_search([1, 2, 3, 4, 5], 100) == -1


def test_double_linear_search_array_is_empty():
    assert double_linear_search([], 100) == -1
