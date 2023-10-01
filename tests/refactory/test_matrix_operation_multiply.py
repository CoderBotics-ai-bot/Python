import pytest
from matrix.matrix_operation import *


def test_multiply_no_error():
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 5], [7, 5]]
    result = multiply(matrix_a, matrix_b)
    assert result is not None


def test_multiply_with_floats_no_error():
    matrix_a = [[1, 2.5], [3, 4.5]]
    matrix_b = [[5, 5], [7, 5]]
    result = multiply(matrix_a, matrix_b)
    assert result is not None


def test_multiply_invalid_dimensions_error():
    with pytest.raises(ValueError):
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 5, 6], [7, 5, 7]]
        multiply(matrix_a, matrix_b)


def test_multiply_multiple_rows_and_columns():
    matrix_a = [[1, 2, 3]]
    matrix_b = [[4], [5], [6]]
    result = multiply(matrix_a, matrix_b)
    assert result is not None
