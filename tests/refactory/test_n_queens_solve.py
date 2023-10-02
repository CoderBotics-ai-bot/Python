from backtracking.n_queens import *
import pytest


import pytest


def test_solve_no_errors(filled_board):
    # We just want to check if function solve runs without throwing any errors
    assert solve(filled_board, 0) is not None


def test_solve_check_for_false(empty_board):
    # For an empty board the function should return false, as there is no solution
    assert not solve(empty_board, 0)


def test_solve_with_no_valid_position(empty_board):
    # The board is empty, but the row parameter is equal to len(board), so the function should return true
    assert solve(empty_board, len(empty_board))


@pytest.fixture
def empty_board():
    return [[0 for _ in range(8)] for _ in range(8)]


@pytest.fixture
def filled_board():
    board = [[0 for _ in range(8)] for _ in range(8)]
    board[0][0] = board[1][3] = board[2][6] = board[3][2] = board[4][5] = board[5][
        1
    ] = board[6][4] = board[7][7] = 1
    return board
