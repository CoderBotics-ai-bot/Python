from machine_learning.forecasting.run import *
import pytest


def test_data_safety_checker_no_errors():
    """Test whether the data_safety_checker function execute without errors."""
    result = data_safety_checker([2, 3, 4], 5.0)
    assert result is not None, "The function should not return None"


def test_data_safety_checker_with_string_input():
    """Test whether TypeError is raised when actual_result is not a float."""
    with pytest.raises(TypeError):
        data_safety_checker([2, 3, 4], "5.0")


def test_data_safety_checker_with_equal_float_input():
    """Test when all votes are the same and equal to the actual_result."""
    result = data_safety_checker([5.0, 5.0, 5.0], 5.0)
    assert result == True, "The function should return True"


def test_data_safety_checker_with_all_votes_greater():
    """Test when all votes are greater than the actual_result."""
    result = data_safety_checker([6, 6, 6], 5.0)
    assert result == True, "The function should return True"


def test_data_safety_checker_with_all_votes_smaller():
    """Test when all votes are smaller than the actual_result."""
    result = data_safety_checker([2, 2, 2], 5.0)
    assert result == False, "The function should return False"
