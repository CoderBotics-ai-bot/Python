from sorts.recursive_bubble_sort import *
import pytest


def test_bubble_sort_no_error():
    """
    Tests bubble_sort Function to see if it runs without throwing errors and doesn't return Nonetype
    """
    result = bubble_sort([3, 2, 1])
    assert result is not None, "Result Should not be Nonetype"


def test_bubble_sort_positive_numbers():
    """
    Tests bubble_sort function with positive integers
    """
    result = bubble_sort([3, 2, 1, 4, 5])
    assert result == [1, 2, 3, 4, 5], "Result is not Correct"


def test_bubble_sort_negative_numbers():
    """
    Tests bubble_sort function with negative numbers
    """
    result = bubble_sort([-3, -1, -2])
    assert result == [-3, -2, -1], "Result is not Correct"


def test_bubble_sort_mixed_numbers():
    """
    Tests bubble_sort function with mixed positive and negative numbers
    """
    result = bubble_sort([3, -1, 2])
    assert result == [-1, 2, 3], "Result is not correct"


def test_bubble_sort_alphabetical_order():
    """
    Tests bubble_sort function with alphabets
    """
    result = bubble_sort(["z", "a", "y", "b", "x", "c"])
    assert result == ["a", "b", "c", "x", "y", "z"], "Result is not correct"


def test_bubble_sort_empty_list():
    """
    Tests bubble_sort function with an empty list
    """
    result = bubble_sort([])
    assert result == [], "Result should be an empty list"


def test_bubble_sort_single_element():
    """
    Tests bubble_sort function with a list of single element
    """
    result = bubble_sort([-1])
    assert result == [-1], "Result should be a list with the single element"


def test_bubble_sort_already_sorted():
    """
    Tests bubble_sort function with an already sorted list
    """
    result = bubble_sort([1, 2, 3, 4])
    assert result == [1, 2, 3, 4], "Result should be the same as input"
