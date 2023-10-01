from dynamic_programming.minimum_cost_path import *
import pytest


@pytest.fixture
def sample_matrix_1():
    return [[2, 1], [3, 1], [4, 2]]


@pytest.fixture
def sample_matrix_2():
    return [[2, 1, 4], [2, 1, 3], [3, 2, 1]]


@pytest.fixture
def sample_matrix_empty():
    return []


def test_minimum_cost_path_no_errors(sample_matrix_1):
    try:
        minimum_cost_path(sample_matrix_1)
    except Exception as e:
        pytest.fail(f"minimum_cost_path() raised {e} unexpectedly!")


def test_minimum_cost_path_not_none(sample_matrix_1):
    assert minimum_cost_path(sample_matrix_1) is not None


def test_minimum_cost_path_expected_result(sample_matrix_1, sample_matrix_2):
    assert minimum_cost_path(sample_matrix_1) == 6
    assert minimum_cost_path(sample_matrix_2) == 7


def test_minimum_cost_path_with_empty_matrix(sample_matrix_empty):
    with pytest.raises(IndexError):
        minimum_cost_path(sample_matrix_empty)


def test_minimum_cost_path_with_single_value_matrix():
    matrix = [[2]]
    assert minimum_cost_path(matrix) == 2
