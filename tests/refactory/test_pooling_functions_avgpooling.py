from computer_vision.pooling_functions import *
import pytest


import numpy as np


def test_avgpooling_no_errors():
    """Test avgpooling function, that it's not throwing any exceptions"""
    input_matrix = np.array(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    )
    size = 2
    stride = 2
    res = None

    try:
        res = avgpooling(input_matrix, size, stride)
    except Exception as e:
        pytest.fail(f"avgpooling function raised exception {e}")

    assert res is not None


def test_avgpooling_square_matrix():
    """Test avgpooling function with a non-square input matrix"""
    input_matrix = np.array([[1, 2, 3], [4, 5, 6]])
    size = 2
    stride = 1

    with pytest.raises(ValueError):
        avgpooling(input_matrix, size, stride)


def test_avgpooling_output_shape():
    """Test avgpooling function to check that the output shape is correct"""
    input_matrix = np.array(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    )
    size = 2
    stride = 2
    expected_shape = (
        (input_matrix.shape[0] - size) // stride + 1,
        (input_matrix.shape[1] - size) // stride + 1,
    )

    res = avgpooling(input_matrix, size, stride)

    assert res.shape == expected_shape


def test_avgpooling_negative_stride():
    """Test avgpooling function with negative stride"""
    input_matrix = np.array(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    )
    size = 2
    stride = -1

    with pytest.raises(ValueError):
        avgpooling(input_matrix, size, stride)
