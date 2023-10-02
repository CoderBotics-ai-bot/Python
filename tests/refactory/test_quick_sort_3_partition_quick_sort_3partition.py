from sorts.quick_sort_3_partition import *
import pytest


def test_quick_sort_3partition_no_error():
    data = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
    quick_sort_3partition(data, 0, len(data) - 1)
    assert data is not None


def test_quick_sort_3partition_sorted_list():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quick_sort_3partition(data, 0, len(data) - 1)
    assert data == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_quick_sort_3partition_unsorted_list():
    data = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
    quick_sort_3partition(data, 0, len(data) - 1)
    assert data == [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]


def test_quick_sort_3partition_duplicate_values():
    data = [9, 7, 5, 11, 12, 5, 14, 3, 10, 6]
    quick_sort_3partition(data, 0, len(data) - 1)
    assert data == [3, 5, 5, 6, 7, 9, 10, 11, 12, 14]


def test_quick_sort_3partition_negative_values():
    data = [-9, -7, -5, -11, -12, -2, -14, -3, -10, -6]
    quick_sort_3partition(data, 0, len(data) - 1)
    assert data == [-14, -12, -11, -10, -9, -7, -6, -5, -3, -2]


def test_quick_sort_3partition_single_value():
    data = [1]
    quick_sort_3partition(data, 0, len(data) - 1)
    assert data == [1]
