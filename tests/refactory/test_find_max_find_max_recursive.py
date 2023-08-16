from maths.find_max import *
import pytest


def test_find_max_recursive():
    # Test standard positive numbers
    assert find_max_recursive([1, 2, 3, 4, 5], 0, 4) == 5
    # Test negative numbers
    assert find_max_recursive([-1, -2, -3, -4, -5], 0, 4) == -1
    # Test with mix of positive and negative numbers
    assert find_max_recursive([1, 2, -3, -4, 5], 0, 4) == 5
    # Test large numbers
    assert find_max_recursive([1, 2, 300000, -400000, 500000], 0, 4) == 500000
    # Test single element
    assert find_max_recursive([1], 0, 0) == 1
    # Test with floating numbers
    assert find_max_recursive([1.2, 2.3, 3.4, 4.5, 5.6], 0, 4) == 5.6


def test_find_max_recursive_exceptions():
    # Test empty list
    with pytest.raises(ValueError):
        find_max_recursive([], 0, 0)
    # Test index out of range
    with pytest.raises(IndexError):
        find_max_recursive([1, 2, 3, 4, 5], 0, 5)
    # Test index out of negative range
    with pytest.raises(IndexError):
        find_max_recursive([1, 2, 3, 4, 5], -6, -1)
