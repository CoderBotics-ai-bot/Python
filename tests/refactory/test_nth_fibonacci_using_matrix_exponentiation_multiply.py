from matrix.nth_fibonacci_using_matrix_exponentiation import *
import pytest


def test_multiply_no_error():
    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
    result = multiply(matrix_a, matrix_b)
    assert result is not None


def test_multiply_result_size():
    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
    result = multiply(matrix_a, matrix_b)
    assert len(result) == len(matrix_a)


def test_multiply_result_matrix_1_1():
    matrix_a = [[1]]
    matrix_b = [[1]]
    result = multiply(matrix_a, matrix_b)
    assert result == [[1]]


def test_multiply_with_zero_matrix():
    matrix_a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    matrix_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = multiply(matrix_a, matrix_b)
    assert result == matrix_a


def test_multiply_identical_matrices():
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = matrix_a
    result = multiply(matrix_a, matrix_b)
    assert result == [[7, 10], [15, 22]]
