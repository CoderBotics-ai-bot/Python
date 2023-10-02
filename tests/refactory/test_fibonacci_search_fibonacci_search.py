import pytest
from searches.fibonacci_search import *


def test_fibonacci_search_no_error():
    arr = [1, 3, 5, 7, 9]
    val = 5
    assert fibonacci_search(arr, val) is not None


def test_fibonacci_search_element_not_present():
    arr = [1, 3, 5, 7, 9]
    val = 6
    assert fibonacci_search(arr, val) == -1


def test_fibonacci_search_empty_list():
    arr = []
    val = 1
    assert fibonacci_search(arr, val) == -1


def test_fibonacci_search_single_element_in_list():
    arr = [5]
    val = 5
    assert fibonacci_search(arr, val) == 0


def test_fibonacci_search_negative_number():
    arr = [-10, 0, 10, 20, 30]
    val = -10
    assert fibonacci_search(arr, val) == 0


def test_fibonacci_search_large_list():
    arr = list(range(1000))
    val = 777
    assert fibonacci_search(arr, val) == 777
