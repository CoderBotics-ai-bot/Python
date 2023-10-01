import pytest
from compression.lempel_ziv import *


def test_write_file_binary_no_errors(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    write_file_binary(str(p), "10101010")
    assert os.path.isfile(p)


def test_write_file_binary_special_chars(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    with pytest.raises(ValueError):
        write_file_binary(str(p), "@#$%&*()")


def test_write_file_binary_file_already_exists(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("content")
    write_file_binary(str(p), "10101010")
    assert os.path.isfile(p)
