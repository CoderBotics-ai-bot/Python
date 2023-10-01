import numpy as np
from computer_vision.pooling_functions import *
import pytest


import numpy as np


def test_maxpooling_no_errors():
    """Test the function maxpooling to ensure no errors occur during execution."""
    try:
        array = np.array(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        )
        size = 2
        stride = 2
        result = maxpooling(array, size, stride)
        assert result is not None
    except Exception as e:
        pytest.fail(f"maxpooling function raised {type(e).__name__} unexpectedly!")


def test_maxpooling_result():
    """Test if the maxpooling function returns the correct result."""
    array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    size = 2
    stride = 2
    result = maxpooling(array, size, stride)
    expected = np.array([[6.0, 8.0], [14.0, 16.0]])
    assert np.array_equal(result, expected), "The output is incorrect for maxpooling"


def test_maxpooling_not_square_matrix():
    """Test that the maxpooling function raises an error when given a non-square matrix."""
    array = np.array([[1, 2, 3], [4, 5, 6]])
    size = 2
    stride = 2
    with pytest.raises(ValueError):
        maxpooling(array, size, stride)


def test_maxpooling_non_int_stride():
    """Test that the maxpooling function raises an error when stride is not an integer."""
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    size = 2
    stride = "a"
    with pytest.raises(TypeError):
        maxpooling(array, size, stride)
