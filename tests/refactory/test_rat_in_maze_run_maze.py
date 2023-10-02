from backtracking.rat_in_maze import *
import pytest


def test_run_maze_no_errors():
    # This test checks if the function run_maze throws no errors, but do not test any specific return values
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
    solutions = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert run_maze(maze, 0, 0, solutions) is not None


def test_run_maze_no_solution():
    # This test checks if the function run_maze correctly identifies when there is no path through the maze
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 0, 1]]
    solutions = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert run_maze(maze, 0, 0, solutions) is False
