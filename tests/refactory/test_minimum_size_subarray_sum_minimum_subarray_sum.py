import pytest
from dynamic_programming.minimum_size_subarray_sum import *


import pytest


def test_minimum_subarray_sum_no_errors():
    assert minimum_subarray_sum(7, [2, 3, 1, 2, 4, 3]) is not None


def test_minimum_subarray_sum_value():
    assert minimum_subarray_sum(7, [2, 3, 1, 2, 4, 3]) == 2


def test_minimum_subarray_sum_negative_values():
    assert minimum_subarray_sum(7, [2, 3, -1, 2, 4, -3]) == 4


def test_minimum_subarray_sum_no_subarray():
    assert minimum_subarray_sum(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0


def test_minimum_subarray_sum_small_subarray():
    assert minimum_subarray_sum(10, [1, 2, 3, 4, 5, 6, 7]) == 2


def test_minimum_subarray_sum_exact_target():
    assert minimum_subarray_sum(5, [1, 1, 1, 1, 1, 5]) == 1


def test_minimum_subarray_sum_empty_list():
    assert minimum_subarray_sum(0, []) == 0


def test_minimum_subarray_sum_zero_target():
    assert minimum_subarray_sum(0, [1, 2, 3]) == 1


def test_minimum_subarray_sum_single_element_subarray():
    assert minimum_subarray_sum(10, [10, 20, 30]) == 1


def test_minimum_subarray_sum_invalid_input():
    with pytest.raises(ValueError):
        minimum_subarray_sum(2, "ABC")


def test_minimum_subarray_sum_none_input():
    assert minimum_subarray_sum(8, None) == 0
