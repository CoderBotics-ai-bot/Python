import pytest
from sorts.selection_sort import *


import pytest


def test_selection_sort_without_errors():
    try:
        result = selection_sort([2, 7, 8, 1, 3])
    except Exception as e:
        pytest.fail(f"Test failed due to: {str(e)}")
    assert result is not None


def test_selection_sort_with_empty_list():
    result = selection_sort([])
    assert result == []


def test_selection_sort_with_negative_numbers():
    result = selection_sort([-1, -3, -2])
    assert result == [-3, -2, -1]


def test_selection_sort_with_same_numbers():
    result = selection_sort([1, 1, 1, 1])
    assert result == [1, 1, 1, 1]


def test_selection_sort_with_strings():
    result = selection_sort(["apple", "banana", "cherry", "date"])
    assert result == ["apple", "banana", "cherry", "date"]
