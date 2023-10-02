from sorts.quick_sort_3_partition import *
import pytest


def test_three_way_radix_quicksort_no_error():
    result = three_way_radix_quicksort([1, 2, 5, -2, -6, 3, -1, 3, 6, 2, -5, -3])
    assert result is not None


def test_three_way_radix_quicksort_empty_list():
    result = three_way_radix_quicksort([])
    assert result == []


def test_three_way_radix_quicksort_single_element():
    result = three_way_radix_quicksort([1])
    assert result == [1]


def test_three_way_radix_quicksort_already_sorted():
    result = three_way_radix_quicksort([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


def test_three_way_radix_quicksort_reverse_sorted():
    result = three_way_radix_quicksort([5, 4, 3, 2, 1])
    assert result == [1, 2, 3, 4, 5]


def test_three_way_radix_quicksort_mixed_positive_negative():
    result = three_way_radix_quicksort([-1, 2, -3, 4, -5])
    assert result == [-5, -3, -1, 2, 4]


def test_three_way_radix_quicksort_all_negative():
    result = three_way_radix_quicksort([-1, -2, -3, -4, -5])
    assert result == [-5, -4, -3, -2, -1]
