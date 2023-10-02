from sorts.exchange_sort import *
import pytest


def test_exchange_sort_no_errors():
    result = exchange_sort([5, 4, 3, 2, 1])
    assert result is not None


def test_exchange_sort_check_length_same():
    array = [5, 4, 3, 2, 1]
    result = exchange_sort(array)
    assert len(result) == len(array)


def test_exchange_sort_desending_order_input():
    array = [5, 4, 3, 2, 1]
    expected_result = [1, 2, 3, 4, 5]
    result = exchange_sort(array)
    assert result == expected_result


def test_exchange_sort_empty_input():
    array = []
    expected_result = []
    result = exchange_sort(array)
    assert result == expected_result


def test_exchange_sort_negative_values():
    array = [-1, -2, -3]
    expected_result = [-3, -2, -1]
    result = exchange_sort(array)
    assert result == expected_result


def test_exchange_sort_already_sorted_input():
    array = [1, 2, 3, 4, 5]
    expected_result = [1, 2, 3, 4, 5]
    result = exchange_sort(array)
    assert result == expected_result


def test_exchange_sort_mixed_positive_negative_values():
    array = [0, 10, -2, 5, 3]
    expected_result = [-2, 0, 3, 5, 10]
    result = exchange_sort(array)
    assert result == expected_result
