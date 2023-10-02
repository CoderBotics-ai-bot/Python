from graphs.eulerian_path_and_circuit_for_undirected_graph import *
import pytest


def test_check_circuit_or_path_no_errors():
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    max_node = 3
    assert check_circuit_or_path(graph, max_node) is not None


def test_check_circuit_or_path_single_node_graph():
    graph = {0: []}
    max_node = 1
    result = check_circuit_or_path(graph, max_node)
    assert result is not None
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)


def test_check_circuit_or_path_cyclic_three_node_graph():
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    max_node = 3
    result = check_circuit_or_path(graph, max_node)
    assert result is not None
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)


def test_check_circuit_or_path_cyclic_odd_even_node_count():
    graph = {0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4], 3: [1, 2, 4], 4: [1, 2, 3]}
    max_node = 5
    result = check_circuit_or_path(graph, max_node)
    assert result is not None
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)
