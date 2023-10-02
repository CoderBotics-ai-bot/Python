import pytest
from sorts.odd_even_sort import *


def test_odd_even_sort_executes():
    result = odd_even_sort([1, 2, 3, 4])
    assert result is not None


def test_odd_even_sort_sorted_array():
    result = odd_even_sort([1, 2, 3, 4])
    assert result == [1, 2, 3, 4]


def test_odd_even_sort_reversed_array():
    result = odd_even_sort([4, 3, 2, 1])
    assert result == [1, 2, 3, 4]


def test_odd_even_sort_negative_numbers():
    result = odd_even_sort([-10, -1, -5, -2])
    assert result == [-10, -5, -2, -1]


def test_odd_even_sort_floats():
    result = odd_even_sort([5.5, 3.3, 1.1, 2.2])
    assert result == [1.1, 2.2, 3.3, 5.5]


def test_odd_even_sort_empty_list():
    result = odd_even_sort([])
    assert result == []
