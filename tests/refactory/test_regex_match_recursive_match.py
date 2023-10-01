from dynamic_programming.regex_match import *

import pytest
from typing import Tuple


@pytest.fixture
def matching_cases() -> Tuple[str, str]:
    return [("abc", "a.c"), ("abc", "af*.c"), ("abc", "a.c*"), ("aa", ".*")]


@pytest.fixture
def nonmatching_cases() -> Tuple[str, str]:
    return [("abc", "a.c*d"), ("ab", ".*c")]


def test_recursive_match_positive(matching_cases):
    for text, pattern in matching_cases:
        result = recursive_match(text, pattern)
        assert result is not None
        assert isinstance(result, bool)
        assert result


def test_recursive_match_negative(nonmatching_cases):
    for text, pattern in nonmatching_cases:
        result = recursive_match(text, pattern)
        assert result is not None
        assert isinstance(result, bool)
        assert not result


def test_recursive_match_with_empty_text():
    text = ""
    pattern = "*"
    result = recursive_match(text, pattern)
    assert result is not None
    assert isinstance(result, bool)
    assert result


def test_recursive_match_with_empty_pattern():
    text = "ab"
    pattern = ""
    result = recursive_match(text, pattern)
    assert result is not None
    assert isinstance(result, bool)
    assert not result
