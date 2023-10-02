import pytest
from sorts.bucket_sort import *


def test_bucket_sort():
    # Testing if the function works without throwing an error and returns a result
    assert bucket_sort([3, 2, 1]) is not None


def test_bucket_sort_empty_list():
    # Testing if the function successfully returns an empty list when an empty list is provided as input
    assert bucket_sort([]) == []


def test_bucket_sort_single_value():
    # Testing if the function successfully sorts a list with a single value
    assert bucket_sort([5]) == [5]


def test_bucket_sort_negative_values():
    # Testing if the function successfully sorts a list with negative values
    assert bucket_sort([-3, -2, -1]) == [-3, -2, -1]


def test_bucket_sort_mixed_negative_and_positive_values():
    # Testing if the function successfully sorts a list containing both positive and negative values
    assert bucket_sort([-3, 4, 1, -1, 3]) == [-3, -1, 1, 3, 4]


def test_bucket_sort_mixed_float_and_int_values():
    # Testing if the function successfully sorts a list containing a mix of integer and floating point numbers
    assert bucket_sort([-3, 4.2, 1, -1.5, 3]) == [-3, -1.5, 1, 3, 4.2]
