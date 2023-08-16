import pytest


import pytest
from dynamic_programming.knapsack import *


def test_knapsack_with_example_solution_success():
    # Test cases where the inputs are correct and returns expected results

    w, wt, val = 10, [1, 3, 5, 2], [10, 20, 100, 22]
    expected_output = (142, {2, 3, 4})
    assert knapsack_with_example_solution(w, wt, val) == expected_output

    w, wt, val = 6, [4, 3, 2, 3], [3, 2, 4, 4]
    expected_output = (8, {3, 4})
    assert knapsack_with_example_solution(w, wt, val) == expected_output


def test_knapsack_with_example_solution_weights_values_count_mismatch():
    # Test case where the counts of weights and values do not match

    w, wt, val = 6, [4, 3, 2, 3], [3, 2, 4]
    with pytest.raises(ValueError) as e:
        knapsack_with_example_solution(w, wt, val)
    assert (
        str(e.value)
        == "The number of weights must be the same as the number of values.\nBut got 4 weights and 3 values"
    )


def test_knapsack_with_example_solution_non_int_weight():
    # Test case where one of the weights is not an integer

    w, wt, val = 10, [1, 3, "5", 2], [10, 20, 100, 22]
    with pytest.raises(TypeError) as e:
        knapsack_with_example_solution(w, wt, val)
    assert (
        str(e.value)
        == "All weights must be integers but got weight of type <class 'str'> at index 2"
    )


def test_knapsack_with_example_solution_non_list_or_tuple_weights_values():
    # Test case where the weights or values are not a list or tuple

    w, wt, val = 10, set([1, 3, 5, 2]), [10, 20, 100, 22]
    with pytest.raises(ValueError) as e:
        knapsack_with_example_solution(w, wt, val)
    assert (
        str(e.value)
        == "Both the weights and values vectors must be either lists or tuples"
    )
