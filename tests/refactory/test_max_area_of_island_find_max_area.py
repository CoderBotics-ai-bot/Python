from matrix.max_area_of_island import *
import pytest


@pytest.fixture
def matrix():
    return [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]


def test_find_max_area(matrix):
    result = find_max_area(matrix)
    assert result is not None


def test_find_max_area_empty_matrix():
    result = find_max_area([[]])
    assert result is 0


def test_find_max_area_single_element_matrix():
    result = find_max_area([[1]])
    assert result is 1
