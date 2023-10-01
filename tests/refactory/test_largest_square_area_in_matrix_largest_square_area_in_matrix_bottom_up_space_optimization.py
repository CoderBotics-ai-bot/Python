from matrix.largest_square_area_in_matrix import *
import pytest


def test_largest_square_area_in_matrix_bottom_up_space_optimization_does_not_crash():
    # we are not trying to test if the logic of the function is correct
    # we only want to see if the function crashes or not
    try:
        largest_square_area_in_matrix_bottom_up_space_optimization(
            4, 4, [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        )
    except Exception as e:
        pytest.fail(f"Function crashed with {e}")


def test_largest_square_area_in_matrix_bottom_up_space_optimization_edge_case_empty_matrix():
    assert largest_square_area_in_matrix_bottom_up_space_optimization(0, 0, []) == 0


def test_largest_square_area_in_matrix_bottom_up_space_optimization_edge_case_single_row_matrix():
    assert (
        largest_square_area_in_matrix_bottom_up_space_optimization(1, 4, [[0, 1, 0, 1]])
        == 1
    )


def test_largest_square_area_in_matrix_bottom_up_space_optimization_edge_case_single_column_matrix():
    assert (
        largest_square_area_in_matrix_bottom_up_space_optimization(
            4, 1, [[0], [1], [0], [1]]
        )
        == 1
    )


def test_largest_square_area_in_matrix_bottom_up_space_optimization_edge_case_all_zero_matrix():
    assert (
        largest_square_area_in_matrix_bottom_up_space_optimization(
            3, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        )
        == 0
    )


def test_largest_square_area_in_matrix_bottom_up_space_optimization_edge_case_max_square_matrix():
    assert (
        largest_square_area_in_matrix_bottom_up_space_optimization(
            3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        )
        == 3
    )


def test_largest_square_area_in_matrix_bottom_up_space_optimization_edge_case_large_matrix():
    matrix = [[1] * 100 for _ in range(100)]
    assert (
        largest_square_area_in_matrix_bottom_up_space_optimization(100, 100, matrix)
        == 100
    )


# No new imports are required
