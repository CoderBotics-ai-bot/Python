import pytest
from dynamic_programming.matrix_chain_order import *


def test_matrix_chain_order_no_errors():
    array = [1, 2, 3, 4, 5]
    matrix, sol = matrix_chain_order(array)
    assert matrix is not None
    assert sol is not None


def test_matrix_chain_order_length():
    array = [1, 2, 3, 4, 5]
    matrix, sol = matrix_chain_order(array)
    assert len(matrix) == len(array)
    assert len(sol) == len(array)


def test_matrix_chain_order_single_element_array():
    array = [1]
    matrix, sol = matrix_chain_order(array)
    assert matrix[0][0] == 0
    assert sol[0][0] == 0


def test_matrix_chain_order_negative_values_array():
    array = [-1, -2, -3, -4, -5]
    matrix, sol = matrix_chain_order(array)
    assert matrix is not None
    assert sol is not None
