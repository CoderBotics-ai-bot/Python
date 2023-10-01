from dynamic_programming.subset_generation import *
import pytest


def test_combination_util_does_not_throw_errors():
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    r = 3
    data = [0] * r
    index = 0
    i = 0
    result = combination_util(arr, n, r, index, data, i)
    assert result is None


def test_combination_util_larger_r_does_not_throw_errors():
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    r = 10  # r is larger than n
    data = [0] * r
    index = 0
    i = 0
    result = combination_util(arr, n, r, index, data, i)
    assert result is None
