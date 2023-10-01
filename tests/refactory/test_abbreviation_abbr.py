from dynamic_programming.abbreviation import *
import pytest


def test_abbr_no_error():
    result = abbr("daBcd", "ABC")
    assert result is not None


def test_abbr_valid_strings():
    result = abbr("daBcd", "ABC")
    assert result == True


def test_abbr_invalid_strings():
    result = abbr("dBcd", "ABC")
    assert result == False


def test_abbr_empty_strings():
    result = abbr("", "")
    assert result == True


def test_abbr_empty_first_string():
    result = abbr("", "ABC")
    assert result == False


def test_abbr_same_case_sensitive_comparision():
    result = abbr("ABC", "ABC")
    assert result == True


def test_abbr_uppercase_mismatch():
    result = abbr("ABC", "ABD")
    assert result == False


def test_abbr_lowercase_mismatch():
    result = abbr("abc", "abd")
    assert result == False
