from backtracking.n_queens_math import *
import pytest


def test_depth_first_search_does_not_throw():
    """Test if the function runs without throwing an error when provided with 4 queens"""
    boards = []
    try:
        depth_first_search([], [], [], boards, 4)
        assert True
    except:
        assert False


def test_depth_first_search_returns_not_none():
    """Test if the function returns a non-None result"""
    boards = []
    depth_first_search([], [], [], boards, 4)
    assert boards is not None


def test_depth_first_search_returns_correct_length():
    """Test if the function returns the correct number of unique solutions for 4 queens"""
    boards = []
    depth_first_search([], [], [], boards, 4)
    assert len(boards) == 2


def test_depth_first_search_returns_correct_length_for_5_queens():
    """Test if the function returns the correct number of unique solutions for 5 queens"""
    boards = []
    depth_first_search([], [], [], boards, 5)
    assert len(boards) == 10


def test_depth_first_search_returns_correct_length_for_6_queens():
    """Test if the function returns the correct number of unique solutions for 6 queens"""
    boards = []
    depth_first_search([], [], [], boards, 6)
    assert len(boards) == 4


def test_depth_first_search_returns_correct_length_for_8_queens():
    """Test if the function returns the correct number of unique solutions for 8 queens"""
    boards = []
    depth_first_search([], [], [], boards, 8)
    assert len(boards) == 92
