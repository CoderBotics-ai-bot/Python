
import pytest
from typing import List
from matrix.sherman_morrison import *


def test_matrix_mul_scalar():
    mat1 = Matrix(2, 2, 3)
    mat2 = mat1 * 2
    expected_values = [[6, 6], [6, 6]]
    assert mat2.array == expected_values, "Scalar multiplier failed"


def test_matrix_mul_matrix():
    mat1 = Matrix(2, 2, 1)
    mat2 = Matrix(2, 2, 1)
    mat3 = mat1 * mat2
    expected_values = [[2, 2], [2, 2]]
    assert mat3.array == expected_values, "Matrix multiplier failed"


def test_matrix_mul_exception():
    mat1 = Matrix(2, 2, 1)
    with pytest.raises(TypeError):
        mat1 * "string"


def test_matrix_mul_unsupported_shape():
    mat1 = Matrix(2, 2)
    mat2 = Matrix(3, 3)
    with pytest.raises(AssertionError):
        mat1 * mat2
