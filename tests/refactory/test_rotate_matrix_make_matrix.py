import pytest
from matrix.rotate_matrix import *


def test_make_matrix_no_errors():
    assert make_matrix() is not None
    assert make_matrix(1) is not None
    assert make_matrix(-2) is not None
    assert make_matrix(3) is not None


def test_make_matrix_type():
    assert isinstance(make_matrix(), list)
    assert isinstance(make_matrix(1), list)
    assert isinstance(make_matrix(-2), list)
    assert isinstance(make_matrix(3), list)


def test_make_matrix_value():
    assert make_matrix(1) == [[1]]
    assert make_matrix(-2) == [[1, 2], [3, 4]]
    assert make_matrix(3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert make_matrix() == [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    assert make_matrix() == make_matrix(4)


def test_make_matrix_row_size():
    assert len(make_matrix(6)) == 6
    assert len(make_matrix(-4)) == 4
    for i in range(1, 10):
        assert len(make_matrix(i)) == i
