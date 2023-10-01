from matrix.spiral_print import *
import pytest


def test_check_matrix_no_error():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    try:
        assert check_matrix(matrix) is not None
    except Exception:
        pytest.fail("check_matrix() raised an exception.")


def test_check_matrix_regular():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert check_matrix(matrix)


def test_check_matrix_irregular():
    matrix = [[1, 2, 3], [4, 5], [7, 8, 9, 10]]
    assert not check_matrix(matrix)


def test_check_matrix_empty():
    matrix = []
    assert not check_matrix(matrix)


def test_check_matrix_with_empty_list():
    matrix = [[]]
    assert check_matrix(matrix)


def test_check_matrix_with_empty_lists():
    matrix = [[], [], []]
    assert check_matrix(matrix)
