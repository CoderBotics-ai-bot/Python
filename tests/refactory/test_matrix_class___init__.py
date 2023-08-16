from matrix.matrix_class import *
from typing import List

import pytest


def test_valid_matrix_initialization():
    """
    This test case verifies that a matrix can be initialized with valid input.
    """
    matrix_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = Matrix(matrix_array)
    assert matrix.rows == matrix_array


def test_empty_matrix_initialization():
    """
    This test case verifies that an empty matrix can be initialized.
    """
    matrix_array = []
    matrix = Matrix(matrix_array)
    assert matrix.rows == matrix_array


def test_invalid_matrix_initialization():
    """
    This test case verifies that initializing a matrix with arrays of unequal lengths raises an error.
    """
    matrix_array = [[1, 2, 3], [4, 5], [7, 8, 9]]
    with pytest.raises(TypeError):
        Matrix(matrix_array)


def test_nonnumeric_matrix_initialization():
    """
    This test case verifies that initializing a matrix with non-numeric values raises an error.
    """
    matrix_array = [[1, "two", 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(TypeError):
        Matrix(matrix_array)


def test_incorrectly_nested_matrix_initialization():
    """
    This test case verifies that initializing a matrix incorrectly (not nested) raises an error.
    """
    matrix_array = [1, 2, 3, 4, 5]
    with pytest.raises(TypeError):
        Matrix(matrix_array)
