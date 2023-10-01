from other.maximum_subsequence import *
import pytest


def test_max_subsequence_sum_no_errors():
    result = max_subsequence_sum([1, 2, 3, 4, -2])
    assert result is not None


def test_max_subsequence_sum_expected_result():
    result = max_subsequence_sum([1, 2, 3, 4, -2])
    assert result == 10


def test_max_subsequence_sum_negative_values():
    result = max_subsequence_sum([-2, -3, -1, -4, -6])
    assert result == -1


def test_max_subsequence_sum_empty_input():
    with pytest.raises(ValueError):
        max_subsequence_sum([])


def test_max_subsequence_sum_none_input():
    with pytest.raises(ValueError):
        max_subsequence_sum(None)


def test_max_subsequence_sum_single_element_input():
    result = max_subsequence_sum([100])
    assert result == 100
