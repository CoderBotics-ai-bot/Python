from dynamic_programming.all_construct import *
import pytest


def test_all_construct_no_error():
    assert all_construct("hello", ["he", "l", "o"]) is not None


def test_all_construct_no_construct():
    result = all_construct("hello", ["world"])
    expected = []
    assert result == expected


def test_all_construct_empty_target():
    result = all_construct("", ["a", "b", "c"])
    expected = [[]]
    assert result == expected


def test_all_construct_empty_word_bank():
    result = all_construct("target", [])
    expected = []
    assert result == expected


def test_all_construct_word_bank_none():
    result = all_construct("target", None)
    expected = []
    assert result == expected


def test_all_construct_large_target():
    result = all_construct("abcdef", ["a", "b", "c"])
    expected = []
    assert result == expected
