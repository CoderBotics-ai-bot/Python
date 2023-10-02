import pytest
from sorts.double_sort import *


def test_double_sort():
    assert double_sort([3, 2, 1]) is not None
    assert double_sort([-3, 10, 16, -42, 29]) is not None
    assert double_sort([]) is not None


def test_double_sort_values():
    assert double_sort([3, 2, 1]) == [1, 2, 3]
    assert double_sort([1, 2, 3]) == [1, 2, 3]
    assert double_sort([-3, 10, 16, -42, 29]) == [-42, -3, 10, 16, 29]
    assert double_sort([]) == []


def test_double_sort_negative_values():
    assert double_sort([-30, -20, -10]) == [-30, -20, -10]


def test_double_sort_letter_number_mix():
    with pytest.raises(TypeError):
        double_sort(["c", "b", "a", 3, 2, 1])
