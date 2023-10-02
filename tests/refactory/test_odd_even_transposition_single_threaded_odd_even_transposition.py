from sorts.odd_even_transposition_single_threaded import *
import pytest


def test_odd_even_transposition():
    result = odd_even_transposition([5, 4, 3, 2, 1])
    assert result is not None


def test_odd_even_transposition_with_positive_numbers():
    result = odd_even_transposition([13, 11, 18, 0, -1])
    assert result == [-1, 0, 11, 13, 18]


def test_odd_even_transposition_with_negative_numbers():
    result = odd_even_transposition([-0.1, 1.1, 0.1, -2.9])
    assert result == [-2.9, -0.1, 0.1, 1.1]


def test_odd_even_transposition_with_empty_list():
    result = odd_even_transposition([])
    assert result == []


def test_odd_even_transposition_with_single_element():
    result = odd_even_transposition([5])
    assert result == [5]
