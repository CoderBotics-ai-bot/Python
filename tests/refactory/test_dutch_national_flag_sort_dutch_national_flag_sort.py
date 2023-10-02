import pytest
from sorts.dutch_national_flag_sort import *


import pytest


def test_dutch_national_flag_sort_no_errors():
    # Ensure dutch_national_flag_sort function does not raise...
    try:
        dutch_national_flag_sort([2, 0, 1, 0, 2, 1])
    except Exception as e:
        pytest.fail(f"Dutch national flag sort raised {type(e)} unexpectedly!")


def test_dutch_national_flag_sort_empty_input():
    # Test empty input
    result = dutch_national_flag_sort([])
    assert result == []


def test_dutch_national_flag_sort_single_item():
    # Test input sequence with single item
    result = dutch_national_flag_sort([1])
    assert result == [1]


def test_dutch_national_flag_sort_multitem_input():
    # Test input sequence with multiple items
    result = dutch_national_flag_sort([2, 0, 1, 0, 2, 1])
    assert result == [0, 0, 1, 1, 2, 2]


def test_dutch_national_flag_sort_invalid_type():
    # Test input sequence that contains non-integer items
    with pytest.raises(ValueError):
        dutch_national_flag_sort(["0", 1, 2])


def test_dutch_national_flag_sort_invalid_value():
    # Test input sequence that contains invalid integer values
    with pytest.raises(ValueError):
        dutch_national_flag_sort([0, 1, 3])
