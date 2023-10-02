
import pytest
from typing import Dict, List
from graphs.eulerian_path_and_circuit_for_undirected_graph import *


def test_check_euler_no_errors():
    graph = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1]}
    max_node = 4
    try:
        check_euler(graph, max_node)
    except Exception as e:
        pytest.fail(f"Test failed with error: {e}")


def test_check_euler_single_node_graph():
    graph = {1: []}
    max_node = 1
    try:
        check_euler(graph, max_node)
    except Exception as e:
        pytest.fail(f"Test failed with error: {e}")


def test_check_euler_two_node_graph():
    graph = {1: [2], 2: [1]}
    max_node = 2
    try:
        check_euler(graph, max_node)
    except Exception as e:
        pytest.fail(f"Test failed with error: {e}")


def test_check_euler_cyclic_even_node_graph():
    graph = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 1]}
    max_node = 4
    try:
        check_euler(graph, max_node)
    except Exception as e:
        pytest.fail(f"Test failed with error: {e}")


def test_check_euler_cyclic_odd_node_graph():
    graph = {1: [2], 2: [1, 3], 3: [2, 4, 5], 4: [3, 5], 5: [4, 3]}
    max_node = 5
    try:
        check_euler(graph, max_node)
    except Exception as e:
        pytest.fail(f"Test failed with error: {e}")
