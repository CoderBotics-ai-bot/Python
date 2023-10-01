from dynamic_programming.regex_match import *
import pytest


def test_dp_match_does_not_throw_errors_on_execution():
    assert dp_match("abc", "a.c") is not None


def test_dp_match_positive_cases():
    assert dp_match("abc", "a.c") == True
    assert dp_match("abc", "af*.c") == True
    assert dp_match("abc", "a.c*") == True
    assert dp_match("aa", ".*") == True


def test_dp_match_negative_cases():
    assert dp_match("abc", "a.c*d") == False


def test_dp_match_text_empty():
    assert dp_match("", "a") == False


def test_dp_match_pattern_empty():
    assert dp_match("abc", "") == False
