import pytest
from sorts.patience_sort import *


def test_patience_sort_no_errors():
    """Test that the function runs without errors for different inputs."""
    patience_sort([1, 2, 3, 4])
    patience_sort([-4, -3, -2, -1])
    patience_sort([])
    patience_sort(list("python"))


def test_patience_sort_returns_list():
    """Test that the function returns a list."""
    assert isinstance(patience_sort([1, 2, 3, 4]), list)


def test_patience_sort_length():
    """Test that the length of the returned list is the same as input list."""
    input_list = [1, 2, 3, 4, 5]
    assert len(input_list) == len(patience_sort(input_list))


def test_patience_sort_empty_list():
    """Test that the function returns an empty list for empty input."""
    assert patience_sort([]) == []


@pytest.mark.parametrize(
    "input_list,expected",
    [
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        (list("python"), list("hnopty")),
    ],
)
def test_patience_sort_sorted(input_list, expected):
    """Test that the function correctly sorts the input list."""
    assert patience_sort(input_list) == expected
