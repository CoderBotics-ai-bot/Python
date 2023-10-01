from networking_flow.ford_fulkerson import bfs

import pytest
from networking_flow.ford_fulkerson import *
from typing import List


def test_bfs():
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0],
    ]
    s = 0
    t = 5
    parent = [-1] * len(graph)
    assert bfs(graph, s, t, parent) is not None


def test_bfs_empty_graph():
    graph: List[List[int]] = []
    s = 0
    t = 0
    parent = []
    with pytest.raises(IndexError):
        bfs(graph, s, t, parent)


def test_bfs_single_node():
    graph = [[0]]
    s = 0
    t = 0
    parent = [-1] * len(graph)
    assert bfs(graph, s, t, parent) is True


def test_bfs_negative_weights():
    graph = [
        [0, -16, -13, 0, 0, 0],
        [0, 0, -10, -12, 0, 0],
        [0, -4, 0, 0, -14, 0],
        [0, 0, -9, 0, 0, 20],
        [0, 0, 0, 7, 0, -4],
        [0, 0, 0, 0, 0, 0],
    ]
    s = 0
    t = 5
    parent = [-1] * len(graph)
    assert bfs(graph, s, t, parent) is False
