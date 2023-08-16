import pytest


import pytest
from graphs.basic_graphs import *


def test_dijk_regular_graph(capsys):
    """Test the dijk function with a regular graph."""
    graph_data = {"a": [("b", 1), ("c", 2)], "b": [], "c": []}
    dijk(graph_data, "a")
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n"


def test_dijk_single_node_graph(capsys):
    """Test the dijk function with a graph with single node."""
    single_node_graph = {"a": []}
    dijk(single_node_graph, "a")
    captured = capsys.readouterr()
    assert captured.out == ""


def test_dijk_no_start_node():
    """Test the dijk function with a graph and start node not in graph."""
    graph_data = {"a": [("b", 1), ("c", 2)], "b": [], "c": []}
    with pytest.raises(KeyError):
        dijk(graph_data, "z")


def test_dijk_empty_graph(capsys):
    """Test the dijk function with an empty graph."""
    empty_graph = {}
    with pytest.raises(KeyError):
        dijk(empty_graph, "a")
