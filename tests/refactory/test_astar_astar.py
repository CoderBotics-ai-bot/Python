from pytest import fixture
from machine_learning.astar import *
import pytest


@pytest.fixture
def grid():
    return Gridworld()


@pytest.fixture
def start():
    start_cell = Cell()
    start_cell.position = (0, 0)
    return start_cell


@pytest.fixture
def goal():
    goal_cell = Cell()
    goal_cell.position = (4, 4)
    return goal_cell


def test_astar_no_errors(grid, start, goal):
    result = astar(grid, start, goal)
    assert result is not None


def test_astar_start_equals_goal(grid, goal):
    result = astar(grid, goal, goal)
    assert result == [goal.position]


def test_astar_path(grid, start, goal):
    result = astar(grid, start, goal)
    assert isinstance(result, list)
    assert all(isinstance(pos, tuple) for pos in result)
