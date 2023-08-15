import pytest
from maths.average_mode import *


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([2, 3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 2, 2, 2], [2]),
        ([3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 2, 2, 2], [2]),
        ([3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 4, 2, 2, 4, 2], [2, 4]),
        (["x", "y", "y", "z"], ["y"]),
        (["x", "x", "y", "y", "z"], ["x", "y"]),
    ],
)
def test_mode(input_list, expected):
    """Test the mode function with various lists of integers and strings"""
    assert mode(input_list) == expected


def test_empty_input():
    """Test the mode function with an empty list"""
    assert mode([]) == []


def test_single_element():
    """Test the mode function with a list containing a single element"""
    assert mode([5]) == [5]


def test_no_mode():
    """Test the mode function with a list where all elements occur only once"""
    assert mode([1, 2, 3, 4]) == [1, 2, 3, 4]
