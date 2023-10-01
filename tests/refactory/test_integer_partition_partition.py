from dynamic_programming.integer_partition import *
import pytest


def test_partition_no_errors():
    # This test verifies that the function doesn't throw any exceptions and produces a result when provided with valid input
    assert partition(5) is not None


def test_partition_negative_input_error():
    # This test asserts that an IndexError is raised when a negative number is passed to the function
    with pytest.raises(IndexError):
        partition(-1)


def test_partition_large_input_no_errors():
    # This test asserts that the function can handle larger inputs without errors
    assert isinstance(partition(500), int)


def test_partition_result_type():
    # This test verifies that the result type of the function is integer as expected
    assert isinstance(partition(10), int)
