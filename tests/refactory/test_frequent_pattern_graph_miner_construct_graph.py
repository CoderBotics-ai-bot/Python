#
#import pytest
#import pytest
#from graphs.frequent_pattern_graph_miner import *
#
#
#from typing import Dict, List, Tuple
#
#
#@pytest.fixture
#def input_data() -> Tuple[Dict[int, Dict[str, int]], Dict[str, List[int]]]:
#    cluster = {1: {"Node1": 1, "Node2": 2}, 2: {"Node3": 1, "Node4": 2}}
#    nodes = {
#        "Node1": [1, 2, 3],
#        "Node2": [4, 5, 6],
#        "Node3": [7, 8, 9],
#        "Node4": [10, 11, 12],
#    }
#    return cluster, nodes
#
#
#def test_construct_graph_valid_input(
#    input_data: Tuple[Dict[int, Dict[str, int]], Dict[str, List[int]]]
#) -> None:
#    cluster, nodes = input_data
#    result = construct_graph(cluster, nodes)
#    assert isinstance(result, dict)
#
#
#def test_construct_graph_empty_cluster() -> None:
#    cluster = {}
#    nodes = {
#        "Node1": [1, 2, 3],
#        "Node2": [4, 5, 6],
#        "Node3": [7, 8, 9],
#        "Node4": [10, 11, 12],
#    }
#    result = construct_graph(cluster, nodes)
#    assert isinstance(result, dict)
#    assert len(result.keys()) == 1
#    assert list(result.keys())[0] == (["Header"],)
#
#
#def test_construct_graph_empty_nodes() -> None:
#    cluster = {1: {"Node1": 1, "Node2": 2}, 2: {"Node3": 1, "Node4": 2}}
#    nodes = {}
#    with pytest.raises(KeyError):
#        _ = construct_graph(cluster, nodes)
#
#
#def test_construct_graph_empty_cluster_and_nodes() -> None:
#    cluster = {}
#    nodes = {}
#    result = construct_graph(cluster, nodes)
#    assert isinstance(result, dict)
#    assert len(result.keys()) == 1
#    assert list(result.keys())[0] == (["Header"],)
#
#
#def test_construct_graph_none_cluster() -> None:
#    cluster = None
#    nodes = {
#        "Node1": [1, 2, 3],
#        "Node2": [4, 5, 6],
#        "Node3": [7, 8, 9],
#        "Node4": [10, 11, 12],
#    }
#    with pytest.raises(TypeError):
#        _ = construct_graph(cluster, nodes)
#
#
#def test_construct_graph_none_nodes() -> None:
#    cluster = {1: {"Node1": 1, "Node2": 2}, 2: {"Node3": 1, "Node4": 2}}
#    nodes = None
#    with pytest.raises(TypeError):
#        _ = construct_graph(cluster, nodes)
#