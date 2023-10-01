from matrix.matrix_operation import *


import pytest
import pytest


def test_add():
    # Test to check if function runs without error
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]

    result = add(matrix1, matrix2)
    assert result is not None


def test_add_integer_type_error():
    # Test to check for TypeError when non-matrix input is given
    with pytest.raises(TypeError):
        add([1, 2], [3])


def test_add_matrices_different_size():
    # Test to check for ValueError when matrices of different sizes are given
    with pytest.raises(ValueError):
        add([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]])


def test_add_multiple_matrices():
    # Test to check if function correctly adds multiple matrices
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    matrix3 = [[9, 10], [11, 12]]

    result = add(matrix1, matrix2, matrix3)
    # The result should be the sum of all input matrices
    expected = [[15, 18], [21, 24]]

    assert result == expected
