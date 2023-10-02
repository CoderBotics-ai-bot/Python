import pytest
from backtracking.word_search import *


def test_word_exists_runs_without_error():
    board = [["A", "B"], ["C", "D"]]
    word = "BC"
    assert word_exists(board, word) is not None


def test_word_exists_with_empty_board():
    board = []
    word = "BC"
    with pytest.raises(
        ValueError,
        match="The board should be a non empty matrix of single chars strings.",
    ):
        word_exists(board, word)


def test_word_exists_with_word_not_present():
    board = [["A", "B", "C"], ["A", "A", "B"], ["D", "D", "D"]]
    word = "E"
    assert not word_exists(board, word)


def test_word_exists_with_non_string_elements_in_board():
    board = [["A", 21], ["C", "D"]]
    word = "BC"
    with pytest.raises(
        ValueError,
        match="The board should be a non empty matrix of single chars strings.",
    ):
        word_exists(board, word)


def test_word_exists_with_empty_word():
    board = [["A", "B"], ["C", "D"]]
    word = ""
    with pytest.raises(
        ValueError,
        match="The word parameter should be a string of length greater than 0.",
    ):
        word_exists(board, word)
