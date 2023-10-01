
import pytest
from typing import List
from networking_flow.minimum_cut import *

# There is no need to import bfs function as it's already accessible and there is no need to redefine it in tests.


def test_bfs():
    # Graph should be a list of lists of integers
    graph = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 0],
    ]
    # Parent should be a list of integers with the same length as graph
    parent = [-1] * len(graph)

    result = bfs(graph, 0, 5, parent)
    assert result is not None


def test_bfs_visited_node():
    graph = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 0],
    ]

    parent = [-1] * len(graph)

    bfs(graph, 0, 5, parent)
    # 5th node should be visited if the graph is traceable
    assert parent[5] != -1
