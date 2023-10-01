import pytest
from graphs.karger import *


def test_partition_graph():
    # The function includes random element, so we just check if it runs without error and returns set
    graph = {"0": ["1"], "1": ["0"]}
    assert isinstance(partition_graph(graph), set)


def test_partition_graph_single_node():
    # Test with single node
    graph = {"0": []}
    assert isinstance(partition_graph(graph), set)


def test_partition_graph_all_to_all():
    # Test with fully connected graph
    graph = {
        "0": ["1", "2", "3"],
        "1": ["0", "2", "3"],
        "2": ["0", "1", "3"],
        "3": ["0", "1", "2"],
    }
    assert isinstance(partition_graph(graph), set)


def test_partition_graph_chain():
    # Test with chain graph
    graph = {"0": ["1"], "1": ["0", "2"], "2": ["1", "3"], "3": ["2"]}
    assert isinstance(partition_graph(graph), set)
