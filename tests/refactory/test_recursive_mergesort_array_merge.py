from sorts.recursive_mergesort_array import *
import pytest


def test_merge_no_error():
    # The first test shouldn't check for any value, just if the function throws any error
    assert merge([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) is not None


def test_merge_empty_list():
    # Edge case: it should return an empty list when the input is an empty list
    assert merge([]) == []


def test_merge_one_element():
    # Edge case: it should return the same list when the list contains one element
    assert merge([5]) == [5]


def test_merge_already_sorted():
    # It should return the same list when the list is already sorted
    assert merge([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_merge_reversed_sorted():
    # It should return a sorted list when the input list is sorted in reversed order
    assert merge([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_merge_unsorted():
    # It should return a sorted list when the input list is unsorted
    assert merge([10, 22, 1, 2, 3, 9, 15, 23]) == [1, 2, 3, 9, 10, 15, 22, 23]


def test_merge_negative_numbers():
    # It should sort negative numbers correctly
    assert merge([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]


def test_merge_mix_numbers():
    # It should sort a list with both positive and negative numbers correctly
    assert merge([3, -2, -1, 0, 1]) == [-2, -1, 0, 1, 3]
