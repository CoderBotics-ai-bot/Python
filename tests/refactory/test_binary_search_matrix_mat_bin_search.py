import pytest
from matrix.binary_search_matrix import *


def test_mat_bin_search_no_errors():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 15
    assert mat_bin_search(target, matrix) is not None


def test_mat_bin_search_non_existing_element():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 34
    assert mat_bin_search(target, matrix) == [-1, -1]


def test_mat_bin_search_on_single_element_list():
    matrix = [[15]]
    target = 15
    assert mat_bin_search(target, matrix) == [0, 0]
