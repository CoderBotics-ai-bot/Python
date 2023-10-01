
import pytest
from dynamic_programming.word_break import *
from typing import List


def test_word_break_no_error():
    assert word_break("applepenapple", ["apple", "pen"]) is not None
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is not None
    assert word_break("cars", ["car", "ca", "rs"]) is not None


@pytest.fixture(scope="module")
def string_fixture() -> str:
    return "applepenapple"


@pytest.fixture(scope="module")
def words_fixture() -> List[str]:
    return ["apple", "pen"]


def test_word_break_positive(string_fixture, words_fixture):
    assert word_break(string_fixture, words_fixture)


def test_word_break_negative_empty_str():
    with pytest.raises(ValueError):
        word_break("", ["a"])


def test_word_break_negative_non_str_input():
    with pytest.raises(ValueError):
        word_break(123, ["a"])


@pytest.fixture(scope="module")
def invalid_words_fixture() -> List[Any]:
    return ["a", 123]


def test_word_break_with_invalid_words(string_fixture, invalid_words_fixture):
    with pytest.raises(ValueError):
        word_break(string_fixture, invalid_words_fixture)
