import os

import pytest
from compression.lempel_ziv_decompress import *


def test_write_file_binary_no_errors():
    test_file_path = "test_data.bin"
    test_string = "0110100001100101011011000110110001101111"
    write_file_binary(test_file_path, test_string)
    assert os.path.exists(test_file_path)
    os.remove(test_file_path)


def test_write_file_binary_large_string():
    test_file_path = "test_data.bin"
    test_string = "1" * 8096
    write_file_binary(test_file_path, test_string)
    assert os.path.exists(test_file_path)
    os.remove(test_file_path)


def test_write_file_binary_invalid_path():
    test_file_path = "/invalid/path/to/test_data.bin"
    test_string = "0110100001100101011011000110110001101111"
    with pytest.raises(SystemExit):
        write_file_binary(test_file_path, test_string)
