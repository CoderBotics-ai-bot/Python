from arithmetic_analysis.lu_decomposition import *
import numpy as np
import pytest


def test_lower_upper_decomposition():
    matrix = np.array([[2, -2, 1], [0, 1, 2], [5, 3, 1]])
    lower_matrix, upper_matrix = lower_upper_decomposition(matrix)

    assert lower_matrix is not None
    assert upper_matrix is not None


def test_lower_upper_decomposition_with_not_square_matrix():
    matrix = np.array([[2, -2, 1], [0, 1, 2]])
    with pytest.raises(ValueError):
        lower_upper_decomposition(matrix)


def test_lower_upper_decomposition_non_invertible_matrix():
    matrix = np.array([[0, 1], [1, 0]])
    with pytest.raises(ArithmeticError):
        lower_upper_decomposition(matrix)


def test_lower_upper_decomposition_singular_matrix():
    matrix = np.array([[1, 0], [1, 0]])
    lower_matrix, upper_matrix = lower_upper_decomposition(matrix)

    assert lower_matrix is not None
    assert upper_matrix is not None


def test_lower_upper_decomposition_singular_zero_matrix():
    matrix = np.array([[0, 1], [0, 1]])
    with pytest.raises(ArithmeticError):
        lower_upper_decomposition(matrix)
