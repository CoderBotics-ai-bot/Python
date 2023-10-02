import pytest
from backtracking.word_search import *


def test_exits_word_responds_correctly():
    board = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    word = "HDI"
    row = 2
    column = 1
    word_index = 0
    visited_points_set = set()
    result = exits_word(board, word, row, column, word_index, visited_points_set)
    assert result is not None


def test_exits_word_handles_empty_board():
    board = []
    word = "ABC"
    row = 0
    column = 0
    word_index = 0
    visited_points_set = set()
    with pytest.raises(IndexError):
        exits_word(board, word, row, column, word_index, visited_points_set)


def test_exits_word_handles_invalid_position():
    board = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    word = "ABC"
    row = 5
    column = 5
    word_index = 0
    visited_points_set = set()
    with pytest.raises(IndexError):
        exits_word(board, word, row, column, word_index, visited_points_set)


def test_exits_word_when_key_already_visited():
    board = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    word = "HDI"
    row = 2
    column = 1
    word_index = 0
    visited_points_set = {17}
    result = exits_word(board, word, row, column, word_index, visited_points_set)
    assert result is False
