from matrix.largest_square_area_in_matrix import *
import pytest


def test_largest_square_area_in_matrix_bottom_up_space_optimization():
    # Test case 1
    assert (
        largest_square_area_in_matrix_bottom_up_space_optimization(
            4, 4, [[0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]]
        )
        != None
    )

    # Test case 2
    assert (
        largest_square_area_in_matrix_bottom_up_space_optimization(1, 1, [[1]]) != None
    )

    # Test case 3
    assert (
        largest_square_area_in_matrix_bottom_up_space_optimization(
            3, 3, [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
        )
        != None
    )

    # Test case 4
    assert (
        largest_square_area_in_matrix_bottom_up_space_optimization(
            2, 2, [[1, 0], [1, 1]]
        )
        != None
    )

    # Test case 5
    assert (
        largest_square_area_in_matrix_bottom_up_space_optimization(
            2, 2, [[1, 1], [1, 1]]
        )
        != None
    )

    # Test case 6
    assert largest_square_area_in_matrix_bottom_up_space_optimization(0, 0, []) != None
