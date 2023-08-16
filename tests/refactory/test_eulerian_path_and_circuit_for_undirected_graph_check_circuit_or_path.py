from graphs.eulerian_path_and_circuit_for_undirected_graph import *
import pytest


def test_check_circuit_or_path_no_odd_degree_nodes():
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    max_node = 3
    rc, node = check_circuit_or_path(graph, max_node)
    assert rc == 1
    assert node == -1


def test_check_circuit_or_path_two_odd_degree_nodes():
    graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1], 3: [0]}
    max_node = 4
    rc, node = check_circuit_or_path(graph, max_node)
    assert rc == 2
    assert node == 3  # here is the last odd node encountered


def test_check_circuit_or_path_more_than_two_odd_degree_nodes():
    graph = {0: [1, 2, 3], 1: [0, 2, 4], 2: [0, 1], 3: [0], 4: [1]}
    max_node = 5
    rc, node = check_circuit_or_path(graph, max_node)
    assert rc == 3
    assert node == 4  # here is the last odd node encountered


def test_check_circuit_or_path_empty_graph():
    graph = {}
    max_node = 0
    rc, node = check_circuit_or_path(graph, max_node)
    assert rc == 1
    assert node == -1
