import pytest
from searches.double_linear_search_recursion import *


def test_search():
    # Test if the function doesn't error with valid input
    assert search([1, 2, 3, 4, 5], 2) is not None


def test_search_empty_list():
    # Test if the function returns -1 when the list is empty
    assert search([], 1) == -1


def test_search_single_element():
    # Test if the function returns correct index when the list has one element
    assert search([5], 5) == 0


def test_search_element_not_found():
    # Test if the function returns -1 when the element is not in the list
    assert search([1, 2, 3, 4, 5], 6) == -1


def test_search_multiple_occurrences():
    # Test if the function returns the first index when the element appears multiple times
    # in the list
    assert search([1, 2, 2, 2, 3], 2) == 1
