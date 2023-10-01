from matrix.max_area_of_island import *
import pytest


@pytest.fixture
def matrix():
    return [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]


def test_find_max_area_does_not_throw_error(matrix):
    assert find_max_area(matrix) is not None


def test_find_max_area_with_empty_matrix():
    matrix = []
    assert find_max_area(matrix) == 0


def test_find_max_area_with_zero_islands():
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert find_max_area(matrix) == 0


def test_find_max_area_with_single_island():
    matrix = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    assert find_max_area(matrix) == 3


def test_find_max_area_with_two_equal_islands():
    matrix = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
    assert find_max_area(matrix) == 4
