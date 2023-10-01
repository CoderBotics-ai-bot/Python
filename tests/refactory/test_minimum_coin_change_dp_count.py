from dynamic_programming.minimum_coin_change import *
import pytest


def test_dp_count():
    assert dp_count([1, 2, 3], 4) is not None
    assert dp_count([1, 2, 3], 7) is not None
    assert dp_count([2, 5, 3, 6], 10) is not None
    assert dp_count([10], 99) is not None
    assert dp_count([4, 5, 6], 0) is not None
    assert dp_count([1, 2, 3], -5) is not None
    assert dp_count([], 10) is not None


def test_dp_count_edge():
    assert dp_count([0], 10) == 0
    assert dp_count([1, 2, 3], 0) == 1
    assert dp_count([1, 2, 3], -10) == 0
    assert dp_count([1, 2, 3], 10**6) > 0
