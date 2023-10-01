import pytest
from dynamic_programming.sum_of_subset import *


def test_is_sum_subset_no_error():
    # Testing if function executes without errors
    assert is_sum_subset([2, 4, 6, 8], 10) is not None


def test_is_sum_subset_edge_empty_list():
    # Testing for empty array input
    assert is_sum_subset([], 10) is False


def test_is_sum_subset_edge_zero_sum():
    # Testing for a required sum of zero
    assert is_sum_subset([1, 2, 3], 0) is True


def test_is_sum_subset_edge_exact_sum():
    # Testing for a case where required sum is exactly present in array
    assert is_sum_subset([1, 2, 3, 4, 5], 5) is True


def test_is_sum_subset_edge_sum_greater_than_total():
    # Testing for a case where required sum is greater than total sum of array
    assert is_sum_subset([1, 2, 3], 7) is False


def test_is_sum_subset_edge_all_zeros():
    # Testing for a case where the array is all zeros
    assert is_sum_subset([0, 0, 0, 0], 3) is False
