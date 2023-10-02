import pytest
from graphs.frequent_pattern_graph_miner import *


def test_create_edge():
    nodes = {"011": [0, 1, 1], "111": [1, 1, 1], "001": [0, 0, 1]}
    graph = {}
    cluster = {2: ["011", "111"], 3: ["001"]}
    c1 = 2
    create_edge(nodes, graph, cluster, c1)

    assert graph is not None
    assert isinstance(graph, dict)
    for node in graph:
        assert isinstance(node, tuple)
        assert isinstance(graph[node], list)


def test_create_edge_no_common_bit():
    nodes = {"011": [0, 1, 1], "100": [1, 0, 0], "001": [0, 0, 1]}
    graph = {}
    cluster = {2: ["011", "100"], 3: ["001"]}
    c1 = 2
    create_edge(nodes, graph, cluster, c1)

    assert graph == {}


def test_create_edge_no_successor_cluster():
    nodes = {"011": [0, 1, 1], "111": [1, 1, 1]}
    graph = {}
    cluster = {2: ["011", "111"]}
    c1 = 2
    create_edge(nodes, graph, cluster, c1)

    assert graph == {}
