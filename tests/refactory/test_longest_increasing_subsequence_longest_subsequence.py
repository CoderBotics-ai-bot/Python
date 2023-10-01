from dynamic_programming.longest_increasing_subsequence import *
import pytest


def test_longest_subsequence_no_error():
    # Generating the test data
    array = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    # Checking if the function runs
    result = longest_subsequence(array)
    assert result is not None


def test_longest_subsequence_empty_array():
    # Testing the function with an empty array
    assert longest_subsequence([]) == []


def test_longest_subsequence_single_element():
    # Testing the function with an array containing a single element
    assert longest_subsequence([1]) == [1]


def test_longest_subsequence_three_elements():
    # Testing the function with a descending sequence of three elements
    assert longest_subsequence([3, 2, 1]) == [2]


def test_longest_subsequence_all_identical():
    # Testing the function with an array where all elements are the same
    assert longest_subsequence([1, 1, 1]) == [1, 1, 1]
