
import pytest
from compression.lempel_ziv_decompress import *
from typing import Tuple


def test_decompress_data_no_errors():
    """
    This test checks if the decompress_data function doesn't throw errors when it's executed.
    """
    result = decompress_data("011001011")
    assert result is not None


def test_decompress_data_empty_string():
    """
    This test checks the behaviour of the function when passing an empty string as an argument
    """
    result = decompress_data("")
    assert result == ""


def test_decompress_data_normal_string():
    """
    This test checks the behaviour of the function when passing a normal string as an argument
    """
    result = decompress_data("01010101")
    assert result is not None


def test_decompress_data_large_input():
    """
    This test checks the function’s behaviour with large input.
    """
    large_input_string = "1" * 100000
    result = decompress_data(large_input_string)
    assert result is not None
