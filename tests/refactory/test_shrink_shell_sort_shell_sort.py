from sorts.shrink_shell_sort import *
import pytest


@pytest.mark.parametrize(
    "collection, expected",
    [
        ([3, 2, 1], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([9, 3, 5, 1, 2], [1, 2, 3, 5, 9]),  # Multiple numbers
        ([3] * 10, [3] * 10),  # All same number
    ],
)
def test_shell_sort(collection, expected):
    result = shell_sort(collection)
    assert result is not None
    assert result == expected


@pytest.mark.parametrize(
    "collection, expected",
    [
        ([3, 2, 1], [1, 3, 2]),
        ([9, 3, 5, 1, 2], [1, 3, 2, 5, 9]),
    ],
)
def test_shell_sort_failed(collection, expected):
    result = shell_sort(collection)
    assert result is not None
    assert result != expected
