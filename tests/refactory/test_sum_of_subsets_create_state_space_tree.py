import pytest
from backtracking.sum_of_subsets import *


import pytest


def test_create_state_space_tree_no_errors():
    nums = [3, 1, 4, 2, 2]
    max_sum = 5
    num_index = 0
    path = []
    result = []
    remaining_nums_sum = sum(nums)

    # we are testing if the function throws an error
    try:
        create_state_space_tree(
            nums, max_sum, num_index, path, result, remaining_nums_sum
        )
    except Exception as e:
        pytest.fail(f"create_state_space_tree() raised {e} unexpectedly!")

    assert True


def test_create_state_space_tree_result_not_none():
    nums = [3, 1, 4, 2, 2]
    max_sum = 5
    num_index = 0
    path = []
    result = []
    remaining_nums_sum = sum(nums)

    create_state_space_tree(nums, max_sum, num_index, path, result, remaining_nums_sum)

    assert result is not None


def test_create_state_space_tree_empty_nums():
    nums = []
    max_sum = 5
    num_index = 0
    path = []
    result = []
    remaining_nums_sum = sum(nums)

    create_state_space_tree(nums, max_sum, num_index, path, result, remaining_nums_sum)

    assert len(result) == 0
