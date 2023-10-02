from graphs.minimum_path_sum import *
import pytest


import pytest


def test_min_path_sum_no_error():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = min_path_sum(grid)
    assert result is not None


def test_min_path_sum_empty_grid():
    with pytest.raises(TypeError):
        min_path_sum(None)


def test_min_path_sum_empty_list():
    with pytest.raises(TypeError):
        min_path_sum([[]])


def test_min_path_sum_single_element():
    grid = [[5]]
    result = min_path_sum(grid)
    assert result == 5


def test_min_path_sum_single_row():
    grid = [[1, 2, 3, 4, 5]]
    result = min_path_sum(grid)
    assert result == 15


def test_min_path_sum_single_column():
    grid = [[1], [2], [3], [4], [5]]
    result = min_path_sum(grid)
    assert result == 15
