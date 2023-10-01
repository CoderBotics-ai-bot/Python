from dynamic_programming.max_subarray_sum import *
import pytest


def test_max_subarray_sum_no_errors():
    """Check if the function max_subarray_sum does not throw any errors."""
    assert max_subarray_sum([1, 2, 3, -1, 2, -3, 4, -5, 6, 7]) is not None


def test_max_subarray_sum_empty_list():
    """Check if the function max_subarray_sum can handle an empty list."""
    assert max_subarray_sum([]) != None


def test_max_subarray_sum_negative_numbers():
    """Check if the function max_subarray_sum handles negative numbers correctly."""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) != float("-inf")


def test_max_subarray_sum_one_element():
    """Check if the function max_subarray_sum can handle a list with one element."""
    assert max_subarray_sum([100]) == 100


def test_max_subarray_sum_allow_empty_true():
    """Check if the function max_subarray_sum handles the allow_empty_subarrays parameter correctly when set to True."""
    assert max_subarray_sum([-1, -2, -3, -4, -5], allow_empty_subarrays=True) == 0
