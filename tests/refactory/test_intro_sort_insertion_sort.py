from sorts.intro_sort import *
import pytest


def test_insertion_sort_no_throw():
    array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]
    result = insertion_sort(array, 0, len(array))
    assert result is not None


def test_insertion_sort_empty_list():
    array = []
    result = insertion_sort(array)
    assert result == []


def test_insertion_sort_single_element():
    array = [5]
    result = insertion_sort(array)
    assert result == [5]


def test_insertion_sort_already_sorted():
    array = [1, 2, 3, 4, 5]
    result = insertion_sort(array)
    assert result == [1, 2, 3, 4, 5]


def test_insertion_sort_reverse_sorted():
    array = [5, 4, 3, 2, 1]
    result = insertion_sort(array)
    assert result == [1, 2, 3, 4, 5]


def test_insertion_sort_negative_numbers():
    array = [5, -4, 3, -2, 1]
    result = insertion_sort(array)
    assert result == [-4, -2, 1, 3, 5]
