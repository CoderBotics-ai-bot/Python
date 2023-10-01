
import pytest


import tempfile
from unittest.mock import patch
import tempfile
from compression.huffman import *
from typing import Any


def test_huffman_no_errors() -> None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"a")
        temp_file.seek(0)
        file_path = temp_file.name
    with patch("builtins.print"):
        huffman(file_path)
    assert True


def test_huffman_single_character() -> None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"a")
        temp_file.seek(0)
        file_path = temp_file.name
    with patch("builtins.print"):
        huffman(file_path)
    assert True


def test_huffman_multiple_same_characters() -> None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"aaaaa")
        temp_file.seek(0)
        file_path = temp_file.name
    with patch("builtins.print"):
        huffman(file_path)
    assert True


def test_huffman_multiple_different_characters() -> None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"abcde")
        temp_file.seek(0)
        file_path = temp_file.name
    with patch("builtins.print"):
        huffman(file_path)
    assert True
