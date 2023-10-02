from sorts.slowsort import *
import pytest


import pytest


def test_slowsort_no_exception():
    """
    Test the slowsort function with some typical inputs to ensure that it runs
    without throwing any exceptions.
    """
    sequence = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    try:
        slowsort(sequence)
    except Exception:
        pytest.fail("slowsort() raised an Exception unexpectedly!")


def test_slowsort_empty_sequence():
    """
    Test the slowsort function with an empty input sequence.
    """
    sequence = []
    slowsort(sequence)
    assert sequence == []


def test_single_element_sequence():
    """
    Test the slowsort function with a single-element input sequence.
    """
    sequence = [3]
    slowsort(sequence)
    assert sequence == [3]


def test_ordered_sequence():
    """
    Test the slowsort function with an already ordered input sequence.
    """
    sequence = [1, 2, 3, 4, 5]
    slowsort(sequence)
    assert sequence == [1, 2, 3, 4, 5]


def test_reversed_sequence():
    """
    Test the slowsort function with a reversed input sequence.
    """
    sequence = [5, 4, 3, 2, 1]
    slowsort(sequence)
    assert sequence == [1, 2, 3, 4, 5]


def test_none_start_end():
    """
    Test the slowsort function with None start and end indices.
    """
    sequence = [5, 4, 3, 2, 1]
    slowsort(sequence, start=None, end=None)
    assert sequence == [1, 2, 3, 4, 5]
