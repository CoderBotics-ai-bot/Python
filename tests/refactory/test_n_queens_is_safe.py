from backtracking.n_queens import *
import pytest


@pytest.fixture
def setup_board():
    return [[0 for _ in range(8)] for _ in range(8)]


def test_is_safe_no_errors(setup_board):
    result = is_safe(setup_board, 0, 0)
    assert result is not None


def test_is_safe_check_for_true(setup_board):
    result = is_safe(setup_board, 0, 0)
    assert result is True


def test_is_safe_check_for_false(setup_board):
    setup_board[0][0] = 1
    result = is_safe(setup_board, 1, 0)
    assert result is False


def test_is_safe_with_queen_in_same_row(setup_board):
    setup_board[0][1] = 1
    result = is_safe(setup_board, 0, 0)
    assert result is False


def test_is_safe_with_queen_in_same_column(setup_board):
    setup_board[1][0] = 1
    result = is_safe(setup_board, 0, 0)
    assert result is False


def test_is_safe_with_queen_in_diagonal(setup_board):
    setup_board[1][1] = 1
    result = is_safe(setup_board, 2, 2)
    assert result is False
