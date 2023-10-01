from matrix.count_negative_numbers_in_sorted_matrix import *
import pytest


def test_find_negative_index_no_errors():
    """This test checks if the function doesn't throw any errors"""
    array = [0, 1, -1, -2]
    result = find_negative_index(array)
    assert result is not None


def test_find_negative_index_all_positive():
    """This test validates the function behaviour when all elements of the array are positive"""
    assert find_negative_index([1, 2, 3, 4, 5]) == 5


def test_find_negative_index_all_negative():
    """This test validates the function behaviour when all elements of the array are negative"""
    assert find_negative_index([-5, -4, -3, -2, -1]) == 0


def test_find_negative_index_mixed_elements():
    """This test validates the function behaviour when the array contains both positive and negative elements"""
    assert find_negative_index([1, 2, -3, -4]) == 2


def test_find_negative_index_multiple_negative_elements():
    """This test validates the function behaviour when the array contains multiple negative elements"""
    assert find_negative_index([1, 2, 3, -1, -2, -3]) == 3


def test_find_negative_index_no_elements():
    """This test validates the function behaviour when the array is empty"""
    assert find_negative_index([]) == 0
