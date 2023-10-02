from graphs.check_bipartite_graph_dfs import *
import pytest


def test_check_bipartite_dfs_exist():
    graph = [[], [2, 3], [1, 3], [1, 2]]
    assert check_bipartite_dfs(graph) is not None


def test_check_bipartite_dfs_bipartite():
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert check_bipartite_dfs(graph) is True


def test_check_bipartite_dfs_not_bipartite():
    graph = [[1, 2, 3], [0, 2], [0, 1], [0, 4], [3]]
    assert check_bipartite_dfs(graph) is False


def test_check_bipartite_dfs_empty_graph():
    graph = []
    assert check_bipartite_dfs(graph) is True


def test_check_bipartite_dfs_single_node():
    graph = [[]]
    assert check_bipartite_dfs(graph) is True


def test_check_bipartite_dfs_single_edge():
    graph = [[1], []]
    assert check_bipartite_dfs(graph) is True
