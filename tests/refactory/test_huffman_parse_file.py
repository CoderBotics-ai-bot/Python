import pytest


import pytest
from compression.huffman import *


def test_parse_file_no_errors(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("hello world")

    result = parse_file(p)

    assert result is not None


def test_parse_file_empty_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "empty.txt"
    p.write_text("")

    result = parse_file(p)

    assert not result


def test_parse_file_single_character(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "a.txt"
    p.write_text("a")

    result = parse_file(p)

    assert result and len(result) == 1


def test_parse_file_multiple_same_characters(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "aaa.txt"
    p.write_text("aaa")

    result = parse_file(p)

    assert result and len(result) == 1 and result[0].freq == 3
