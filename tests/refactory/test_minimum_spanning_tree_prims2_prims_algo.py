
import pytest
from sys import maxsize
from typing import Any, Dict, Optional, TypeVar
from graphs.minimum_spanning_tree_prims2 import *


@pytest.fixture
def graph_data():
    T = TypeVar("T")
    graph = GraphUndirectedWeighted()
    graph.add_edge("a", "b", 3)
    graph.add_edge("b", "c", 10)
    graph.add_edge("c", "d", 5)
    graph.add_edge("a", "c", 15)
    graph.add_edge("b", "d", 100)
    return graph


def test_prims_algo(graph_data):
    dist, parent = prims_algo(graph_data)
    assert isinstance(dist, dict)
    assert isinstance(parent, dict)


def test_prims_algo_empty():
    graph = GraphUndirectedWeighted()
    dist, parent = prims_algo(graph)
    assert dist == {}
    assert parent == {}


def test_prims_algo_single_node():
    graph = GraphUndirectedWeighted()
    graph.add_edge("a", "a", 0)
    dist, parent = prims_algo(graph)
    assert dist == {"a": 0}
    assert parent == {"a": None}
