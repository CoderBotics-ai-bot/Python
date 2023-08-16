from matrix.count_paths import *
import pytest


@pytest.fixture
def grid_2_paths():
    return [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]


@pytest.fixture
def grid_no_paths():
    return [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]


def test_depth_first_search(grid_2_paths, grid_no_paths):
    # Test case where there are 2 possible paths
    assert depth_first_search(grid_2_paths, 0, 0, set()) == 2
    # Test case where there are no possible paths
    assert depth_first_search(grid_no_paths, 0, 0, set()) == 0
