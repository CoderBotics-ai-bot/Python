from backtracking.knight_tour import *

import pytest
from typing import List, Tuple


@pytest.fixture
def board_filled() -> List[List[int]]:
    """Returns a filled 5x5 board"""
    return [[1 for _ in range(5)] for _ in range(5)]


@pytest.fixture
def board_empty() -> List[List[int]]:
    """Returns an empty 5x5 board"""
    return [[0 for _ in range(5)] for _ in range(5)]


@pytest.fixture
def pos() -> Tuple[int, int]:
    """Returns a position tuple"""
    return (0, 0)


def test_open_knight_tour_helper_no_error(
    board_filled: List[List[int]], pos: Tuple[int, int]
):
    """Tests if function runs without errors and returns any value"""
    result = open_knight_tour_helper(board_filled, pos, curr=1)
    assert result is not None


def test_open_knight_tour_helper_tour_complete(
    board_filled: List[List[int]], pos: Tuple[int, int]
):
    """Tests if function return True for a board that is already complete"""
    result = open_knight_tour_helper(board_filled, pos, curr=25)
    assert result


def test_open_knight_tour_helper_tour_incomplete(
    board_empty: List[List[int]], pos: Tuple[int, int]
):
    """Tests if function return False for a board that is not complete"""
    result = open_knight_tour_helper(board_empty, pos, curr=1)
    assert not result
