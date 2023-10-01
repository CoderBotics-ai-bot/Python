import pytest
from matrix.matrix_operation import *


def test_subtract_matrix_no_error() -> None:
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[2, 3], [4, 5]]
    assert subtract(matrix_a, matrix_b) is not None


def test_subtract_matrix_with_floats_no_error() -> None:
    matrix_a = [[1, 2.5], [3, 4]]
    matrix_b = [[2, 3], [4, 5.5]]
    assert subtract(matrix_a, matrix_b) is not None


def test_subtract_matrix_with_invalid_type_error() -> None:
    matrix_a = 4
    matrix_b = 5
    with pytest.raises(TypeError):
        subtract(matrix_a, matrix_b)


def test_subtract_matrix_with_list_item_error() -> None:
    matrix_a = [1, 2, 3]
    matrix_b = [4, 5, 6]
    with pytest.raises(TypeError):
        subtract(matrix_a, matrix_b)
