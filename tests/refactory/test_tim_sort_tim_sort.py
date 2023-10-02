from sorts.tim_sort import *
import pytest


def test_tim_sort_without_errors():
    result = tim_sort(list(reversed(list(range(7)))))
    assert result is not None


def test_tim_sort_sorting_strings():
    result = tim_sort("Python")
    assert result == ["P", "h", "n", "o", "t", "y"]


def test_tim_sort_sorting_floats():
    result = tim_sort((1.1, 1, 0, -1, -1.1))
    assert result == [-1.1, -1, 0, 1, 1.1]


def test_tim_sort_comparing_to_sorted_function():
    result = tim_sort([3, 2, 1])
    assert result == sorted([3, 2, 1])
