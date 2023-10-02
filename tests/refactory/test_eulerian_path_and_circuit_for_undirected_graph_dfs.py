from graphs.eulerian_path_and_circuit_for_undirected_graph import *
import pytest


def test_dfs_no_errors():
    graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    visited_edge = {
        1: {2: False, 3: False},
        2: {1: False, 3: False},
        3: {1: False, 2: False},
    }
    assert dfs(1, graph, visited_edge) is not None


def test_dfs_single_node_graph():
    graph = {1: []}
    visited_edge = {1: {}}
    assert dfs(1, graph, visited_edge) == [1]


def test_dfs_two_node_graph():
    graph = {1: [2], 2: [1]}
    visited_edge = {1: {2: False}, 2: {1: False}}
    assert set(dfs(1, graph, visited_edge)) == set([1, 2])


def test_dfs_cyclic_three_node_graph():
    graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    visited_edge = {
        1: {2: False, 3: False},
        2: {1: False, 3: False},
        3: {1: False, 2: False},
    }
    assert set(dfs(1, graph, visited_edge)) == set([1, 2, 3])
