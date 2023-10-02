import pytest
from backtracking.hamiltonian_cycle import *


def test_util_hamilton_cycle():
    graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ]
    path = [0, -1, -1, -1, -1, 0]
    curr_ind = 1
    result = util_hamilton_cycle(graph, path, curr_ind)
    assert result is not None


def test_util_hamilton_cycle_mid_calculation():
    graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ]
    path = [0, 1, 2, -1, -1, 0]
    curr_ind = 3
    result = util_hamilton_cycle(graph, path, curr_ind)
    assert result is not None
