import pytest
from networking_flow.minimum_cut import *


import pytest


def test_bfs():
    graph = [
        [0, 3, 2, 0, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 1, 0, 4, 2, 0],
        [0, 0, 0, 0, 0, 2],
        [0, 0, 0, 3, 0, 2],
        [0, 0, 0, 0, 0, 0],
    ]
    s = 0
    t = 5
    parent = [-1 for _ in range(len(graph))]

    assert bfs(graph, s, t, parent) == True


def test_bfs_no_path():
    graph = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    s = 0
    t = 5
    parent = [-1 for _ in range(len(graph))]

    assert bfs(graph, s, t, parent) == False


def test_bfs_empty_graph():
    graph = []
    s = 0
    t = 5
    parent = [-1 for _ in range(len(graph))]

    with pytest.raises(IndexError):
        bfs(graph, s, t, parent)
