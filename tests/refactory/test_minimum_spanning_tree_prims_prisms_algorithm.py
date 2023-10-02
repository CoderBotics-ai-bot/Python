import pytest
from graphs.minimum_spanning_tree_prims import *


def test_prisms_algorithm():
    """
    Test for the function prisms_algorithm(adjacency_list).

    Test to check if the function prisms_algorithm(adjacency_list) runs without errors when appropriate inputs are given.
    """
    adjacency_list = {
        0: [[1, 1], [3, 3]],
        1: [[0, 1], [2, 6], [3, 5], [4, 1]],
        2: [[1, 6], [4, 5], [5, 2]],
        3: [[0, 3], [1, 5], [4, 1]],
        4: [[1, 1], [2, 5], [3, 1], [5, 4]],
        5: [[2, 2], [4, 4]],
    }
    assert prisms_algorithm(adjacency_list) is not None


def test_prisms_algorithm_single_vertex():
    """
    Test for the function prisms_algorithm(adjacency_list).

    Test to check if the function prisms_algorithm(adjacency_list) runs without errors and returns the expected output
    when an adjacency list with a single vertex is given as input.
    """
    adjacency_list = {0: []}
    assert prisms_algorithm(adjacency_list) == []


def test_prisms_algorithm_self_loops():
    """
    Test for the function prisms_algorithm(adjacency_list).

    Test to check if the function prisms_algorithm(adjacency_list) runs without errors when the adjacency list contains self loops.
    """
    adjacency_list = {0: [[0, 1], [1, 1]], 1: [[0, 1], [1, 1]]}
    assert prisms_algorithm(adjacency_list) is not None
