from matrix.largest_square_area_in_matrix import *
import pytest


def test_largest_square_area_in_matrix_bottom_up_does_not_crash():
    result = largest_square_area_in_matrix_bottom_up(2, 2, [[1, 1], [1, 1]])
    assert result is not None


def test_largest_square_area_in_matrix_bottom_up_edge_case_empty_matrix():
    result = largest_square_area_in_matrix_bottom_up(0, 0, [])
    assert result == 0


def test_largest_square_area_in_matrix_bottom_up_edge_case_single_row_matrix():
    result = largest_square_area_in_matrix_bottom_up(1, 3, [[1, 1, 0]])
    assert result == 1


def test_largest_square_area_in_matrix_bottom_up_edge_case_single_column_matrix():
    result = largest_square_area_in_matrix_bottom_up(3, 1, [[1], [1], [0]])
    assert result == 1


def test_largest_square_area_in_matrix_bottom_up_edge_case_all_zero_matrix():
    result = largest_square_area_in_matrix_bottom_up(2, 2, [[0, 0], [0, 0]])
    assert result == 0


def test_largest_square_area_in_matrix_bottom_up_edge_case_max_square_matrix():
    result = largest_square_area_in_matrix_bottom_up(
        3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    )
    assert result == 3


def test_largest_square_area_in_matrix_bottom_up_edge_case_large_matrix():
    large_matrix = [[1] * 1000] * 1000
    result = largest_square_area_in_matrix_bottom_up(1000, 1000, large_matrix)
    assert result == 1000
