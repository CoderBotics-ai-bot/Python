from sorts.quick_sort import *
import pytest


import pytest


def test_quick_sort_no_error():
    try:
        result = quick_sort([5, 2, 4, 1, 3])
    except Exception as e:
        pytest.fail(f"Quick sort raised an error unexpectedly: {str(e)}")
    assert result is not None, "Function returned None type"


def test_quick_sort_empty_input():
    result = quick_sort([])
    assert result is not None, "Function returned None type on empty input"
    assert len(result) == 0, "Function did not return an empty list on empty input"


def test_quick_sort_single_element_input():
    result = quick_sort([5])
    assert result is not None, "Function returned None type on single element input"
    assert (
        len(result) == 1
    ), "Function did not return a list with one element on single element input"
    assert result[0] == 5, "Incorrectly sorted single element input"


def test_quick_sort_two_element_input():
    result = quick_sort([5, 3])
    assert result is not None, "Function returned None type on two element input"
    assert (
        len(result) == 2
    ), "Function did not return a list with two elements on two element input"
    assert result[0] <= result[1], "Did not correctly sort two element input"


def test_quick_sort_negative_numbers():
    result = quick_sort([-5, -3, -1])
    assert result is not None, "Function returned None type on negative numbers input"
    assert (
        len(result) == 3
    ), "Function did not return a list with three elements on three element input"
    assert result == sorted(
        [-5, -3, -1]
    ), "Did not correctly sort negative numbers list"
