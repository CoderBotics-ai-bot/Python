#
#import pytest
#import pytest
#
#
#from unittest.mock import patch
#from graphs.frequent_pattern_graph_miner import *
#
#
#def test_print_all(mocker):
#    nodes = mocker.patch("builtins.nodes", {"n1": "node 1", "n2": "node 2"})
#    cluster = mocker.patch("builtins.cluster", {"c1": "cluster 1", "c2": "cluster 2"})
#    graph = mocker.patch("builtins.graph", {"g1": "graph 1", "g2": "graph 2"})
#    support = mocker.patch("builtins.support", "support string")
#    freq_subgraph_edge_list = mocker.patch(
#        "builtins.freq_subgraph_edge_list", ["edge list 1", "edge list 2"]
#    )
#
#    try:
#        print_all()  # Execute the function
#    except Exception:
#        pytest.fail(
#            "print_all function raised an error"
#        )  # Test fails if an exception is raised
#