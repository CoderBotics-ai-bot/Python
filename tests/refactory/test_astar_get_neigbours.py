
import numpy as np
import pytest
from machine_learning.astar import *
from typing import Tuple


from typing import Tuple


@pytest.fixture
def cell():
    c = Cell()
    c.position = (2, 2)
    return c


@pytest.fixture
def gridworld():
    return Gridworld((5, 5))


def test_get_neighbours_no_errors(cell, gridworld):
    result = gridworld.get_neigbours(cell)
    assert result is not None


def test_get_neighbours_return_list(cell, gridworld):
    neighbours = gridworld.get_neigbours(cell)
    assert isinstance(neighbours, list)


def test_get_neighbour_positions(cell, gridworld):
    neighbours = gridworld.get_neigbours(cell)
    positions = [neighbour.position for neighbour in neighbours]
    assert (1, 1) in positions
    assert (1, 2) in positions
    assert (3, 3) in positions
    assert (2, 3) in positions
    assert (2, 1) in positions


def test_get_neighbours_within_bounds(cell, gridworld):
    neighbours = gridworld.get_neigbours(cell)
    for neighbour in neighbours:
        assert 0 <= neighbour.position[0] < gridworld.world_x_limit
        assert 0 <= neighbour.position[1] < gridworld.world_y_limit
