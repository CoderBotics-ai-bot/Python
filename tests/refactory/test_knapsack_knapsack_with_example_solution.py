from dynamic_programming.knapsack import *
import pytest


def test_knapsack_with_example_solution_do_not_throw_on_valid_input():
    wt = [1, 3, 5, 2]
    val = [10, 20, 100, 22]
    w = 10
    result = knapsack_with_example_solution(w, wt, val)
    assert result is not None


def test_knapsack_with_example_solution_throw_on_invalid_weight_type():
    wt = [1, 3, "a", 2]
    val = [10, 20, 100, 22]
    w = 10
    with pytest.raises(TypeError):
        knapsack_with_example_solution(w, wt, val)


def test_knapsack_with_example_solution_throw_on_different_size_lists():
    wt = [1, 3, 5]
    val = [10, 20, 100, 22]
    w = 10
    with pytest.raises(ValueError):
        knapsack_with_example_solution(w, wt, val)


def test_knapsack_with_example_solution_throw_on_non_list_parameters():
    wt = 1
    val = [10, 20, 100, 22]
    w = 10
    with pytest.raises(ValueError):
        knapsack_with_example_solution(w, wt, val)
