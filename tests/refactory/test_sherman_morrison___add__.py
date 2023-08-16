from matrix.sherman_morrison import *
import pytest


def test_matrix_addition():
    # Creating two matrix with default value = 5 of size 2,2
    matrix1 = Matrix(2, 2, 5)
    matrix2 = Matrix(2, 2, 5)
    result_matrix = matrix1 + matrix2

    # The result matrix will be of size 2,2 with each element = 10
    assert result_matrix.array == [[10, 10], [10, 10]]

    # Edge Case: Adding matrix of different sizes should raise AssertionError
    matrix3 = Matrix(1, 1, 5)
    try:
        _ = matrix1 + matrix3
        assert False, "Matrix size Assertion Error expected, but not received"
    except AssertionError:
        pass
