from searches.binary_search import *
import pytest


def test_bisect_left_no_errors():
    assert bisect_left([0, 5, 7, 10, 15], 0) is not None
    assert bisect_left([0, 5, 7, 10, 15], 6) is not None
    assert bisect_left([0, 5, 7, 10, 15], 20) is not None
    assert bisect_left([0, 5, 7, 10, 15], 15, 1, 3) is not None
    assert bisect_left([0, 5, 7, 10, 15], 6, 2) is not None
    assert bisect_left([], 0) is not None


def test_bisect_left_expected_output():
    assert bisect_left([0, 5, 7, 10, 15], 0) == 0
    assert bisect_left([0, 5, 7, 10, 15], 6) == 2
    assert bisect_left([0, 5, 7, 10, 15], 20) == 5
    assert bisect_left([0, 5, 7, 10, 15], 15, 1, 3) == 3
    assert bisect_left([0, 5, 7, 10, 15], 6, 2) == 2
    assert bisect_left([], 0) == 0


def test_bisect_left_large_input():
    large_sorted_list = list(range(1000000))
    assert bisect_left(large_sorted_list, 500000) == 500000
    assert bisect_left(large_sorted_list, 1000000) == 1000000
    assert bisect_left(large_sorted_list, 0) == 0
