
import pytest
from sorts.counting_sort import *
from typing import List


def test_counting_sort_no_errors():
    initial_list = [0, 5, 3, 2, 2]
    assert counting_sort(initial_list) is not None


def test_counting_sort_empty_input():
    assert counting_sort([]) == []


def test_counting_sort_negative_numbers():
    initial_list = [-2, -5, -45]
    result = counting_sort(initial_list)
    assert result == [-45, -5, -2]


def test_counting_sort_large_input():
    initial_list = [1000000, 5, 300000, 2, 2]
    result = counting_sort(initial_list)
    assert result == [2, 2, 5, 300000, 1000000]
