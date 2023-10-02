from backtracking.knight_tour import *
import pytest


def test_get_valid_pos_no_error():
    assert get_valid_pos((1, 1), 3) is not None


def test_get_valid_pos_correct_type():
    assert type(get_valid_pos((1, 1), 3)) == list


def test_get_valid_pos_boundary_check():
    valid_pos = get_valid_pos((0, 0), 3)
    assert all(0 <= pos[0] < 3 and 0 <= pos[1] < 3 for pos in valid_pos)
