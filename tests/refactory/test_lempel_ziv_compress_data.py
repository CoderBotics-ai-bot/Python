import pytest
from compression.lempel_ziv import *


def test_compress_data_no_errors():
    data_bits = "01100101"
    result = compress_data(data_bits)
    assert result is not None


def test_compress_data_return_type():
    data_bits = "01100101"
    result = compress_data(data_bits)
    assert isinstance(result, str)


def test_compress_data_empty_string():
    data_bits = ""
    result = compress_data(data_bits)
    assert result == ""


def test_compress_data_single_character():
    data_bits = "0"
    result = compress_data(data_bits)
    assert result == "0"
    data_bits = "1"
    result = compress_data(data_bits)
    assert result == "1"


# No imports need to be provided as the function is already available in the context and the Python built-in functions are used.
