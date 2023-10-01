from dynamic_programming.knapsack import *
import pytest


def test_knapsack():
    w = 10
    wt = [1, 2, 3, 4, 5]
    val = [10, 20, 30, 40, 50]
    n = 5

    result, _ = knapsack(w, wt, val, n)
    assert result is not None


def test_knapsack_zero_value():
    w = 10
    wt = [1, 2, 3, 4, 5]
    val = [0, 0, 0, 0, 0]
    n = 5

    result, _ = knapsack(w, wt, val, n)
    assert result == 0


def test_knapsack_negative_weight():
    w = -10
    wt = [1, 2, 3, 4, 5]
    val = [10, 20, 30, 40, 50]
    n = 5

    with pytest.raises(Exception):
        knapsack(w, wt, val, n)


def test_knapsack_negative_item_weights():
    w = 10
    wt = [-1, -2, -3, -4, -5]
    val = [10, 20, 30, 40, 50]
    n = 5

    with pytest.raises(Exception):
        knapsack(w, wt, val, n)
