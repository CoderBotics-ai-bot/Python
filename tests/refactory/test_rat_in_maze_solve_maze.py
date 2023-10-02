from backtracking.rat_in_maze import *
import pytest


def test_solve_maze_no_error():
    maze = [
        [0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    result = solve_maze(maze)
    assert result is not None


def test_solve_maze_no_solution_no_error():
    maze = [[0, 1, 0], [0, 1, 0], [1, 0, 0]]
    result = solve_maze(maze)
    assert result is not None


def test_solve_maze_empty_input_no_error():
    maze = []
    result = solve_maze(maze)
    assert result is not None
