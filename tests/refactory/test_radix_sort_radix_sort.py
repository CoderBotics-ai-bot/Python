from sorts.radix_sort import *
import pytest


def test_radix_sort_no_errors():
    # This test checks if the function executes without any errors for a valid input
    try:
        radix_sort([4, 2, 3, 1])
    except Exception:
        pytest.fail("The function crashed with an exception")


def test_radix_sort_not_empty():
    # This test ensures that the function does not return a None value
    result = radix_sort([2, 1, 3, 4])
    assert result is not None


def test_radix_sort_sorted_sequence():
    # This test verifies that the function returns a correctly sorted list
    sequence = [5, 1, 4, 2, 8]
    assert radix_sort(sequence) == sorted(sequence)


def test_radix_sort_reverse_sorted():
    # This test verifies that the function can correctly sort a list that is sorted in reverse order
    sequence = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert radix_sort(sequence) == sorted(sequence)


def test_radix_sort_single_element():
    # This test checks whether the function can handle a list with a single element
    sequence = [1]
    assert radix_sort(sequence) == [1]


def test_radix_sort_duplicates():
    # This test checks whether the function can handle a list with duplicate elements correctly
    sequence = [2, 2, 1, 1, 3, 3]
    assert radix_sort(sequence) == sorted(sequence)
