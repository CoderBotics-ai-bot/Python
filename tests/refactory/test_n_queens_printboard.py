from backtracking.n_queens import *
import pytest


import pytest


def test_printboard_no_errors(capfd):
    board = [[1, 0], [0, 1]]
    printboard(board)
    out, err = capfd.readouterr()
    assert not err


def test_printboard_output(capfd):
    board = [[1, 0], [0, 1]]
    printboard(board)
    out, err = capfd.readouterr()
    expected_output = "Q . \n. Q \n"
    assert out == expected_output
