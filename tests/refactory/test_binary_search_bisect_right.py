from searches.binary_search import *
import pytest


def test_bisect_right_no_errors():
    assert bisect_right([0, 1, 2, 3, 4, 5], 2) is not None


def test_bisect_right_expected_output():
    assert bisect_right([0, 1, 2, 3, 4, 5], 2) == 3
    assert bisect_right([0, 1, 2, 3, 4, 5], 5) == 6
    assert bisect_right([0, 1, 2, 3, 4, 5], 0) == 1
    assert bisect_right([0, 1, 2, 3, 4, 5], -1) == 0


def test_bisect_right_with_lo_hi_parameters():
    assert bisect_right([0, 1, 2, 3, 4, 5], 2, 1, 4) == 3
    assert bisect_right([0, 1, 2, 3, 4, 5], 5, 2, 5) == 5
    assert bisect_right([0, 1, 2, 3, 4, 5], 0, 0, 3) == 1
    assert bisect_right([0, 1, 2, 3, 4, 5], -1, 2, 4) == 2


def test_bisect_right_edge_cases():
    assert bisect_right([], 2) == 0  # empty list
    assert bisect_right([2], 2) == 1  # single element equal to item
    assert bisect_right([1], 2) == 1  # single element less than item
    assert bisect_right([3], 2) == 0  # single element greater than item
