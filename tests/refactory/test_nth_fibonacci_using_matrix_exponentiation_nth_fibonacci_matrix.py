from matrix.nth_fibonacci_using_matrix_exponentiation import *
import pytest


def test_nth_fibonacci_matrix_no_error():
    """
    Test to ensure that nth_fibonacci_matrix function doesn't throw any errors when it's executed
    """
    assert nth_fibonacci_matrix(5) is not None


def test_nth_fibonacci_matrix_zero():
    """
    Test to ensure nth_fibonacci_matrix function returns zero for input zero (one of the base case)
    """
    assert nth_fibonacci_matrix(0) == 0


def test_nth_fibonacci_matrix_one():
    """
    Test to ensure nth_fibonacci_matrix function returns one for input one (one of the base case)
    """
    assert nth_fibonacci_matrix(1) == 1


def test_nth_fibonacci_matrix_15():
    """
    Test to ensure nth_fibonacci_matrix function returns correct fibonacci sequence number for input 15
    The 15th Fibonacci number is 610.
    """
    assert nth_fibonacci_matrix(15) == 610


def test_nth_fibonacci_matrix_negative():
    """
    Test to ensure nth_fibonacci_matrix function returns the negative input as is for negative input value
    """
    assert nth_fibonacci_matrix(-5) == -5
