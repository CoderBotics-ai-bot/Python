from graphs.graph_list import *

import pytest
from typing import Dict, List


# define a fixture for common setup
@pytest.fixture
def graph_adjacency_list_object():
    graph_object = GraphAdjacencyList()
    yield graph_object
    del graph_object


def test_add_edge(graph_adjacency_list_object):
    # Test when both vertices are new for the graph (directed)
    graph_adjacency_list_object.add_edge(1, 2)
    expected_adj_list: Dict[int, List[int]] = {1: [2], 2: []}
    assert graph_adjacency_list_object.adj_list == expected_adj_list

    # Test when source vertex is already in the graph but destination is new (directed)
    graph_adjacency_list_object.add_edge(1, 3)
    expected_adj_list = {1: [2, 3], 2: [], 3: []}
    assert graph_adjacency_list_object.adj_list == expected_adj_list

    # Test when destination vertex is already in the graph but source is new (directed)
    graph_adjacency_list_object.add_edge(4, 2)
    expected_adj_list = {1: [2, 3], 2: [], 3: [], 4: [2]}
    assert graph_adjacency_list_object.adj_list == expected_adj_list

    # Test when both vertices are already in the graph (directed)
    graph_adjacency_list_object.add_edge(1, 2)
    expected_adj_list = {1: [2, 3, 2], 2: [], 3: [], 4: [2]}
    assert graph_adjacency_list_object.adj_list == expected_adj_list

    # Test for undirected graph, both vertices are new
    graph_object_undirected = GraphAdjacencyList(False)
    graph_object_undirected.add_edge(1, 2)
    expected_adj_list = {1: [2], 2: [1]}
    assert graph_object_undirected.adj_list == expected_adj_list

    # Test for undirected graph, one vertex is new
    graph_object_undirected.add_edge(1, 3)
    expected_adj_list = {1: [2, 3], 2: [1], 3: [1]}
    assert graph_object_undirected.adj_list == expected_adj_list

    # Test for undirected graph, both vertices are existing
    graph_object_undirected.add_edge(1, 2)
    expected_adj_list = {1: [2, 3, 2], 2: [1, 1], 3: [1]}
    assert graph_object_undirected.adj_list == expected_adj_list
