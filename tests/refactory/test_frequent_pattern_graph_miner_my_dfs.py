#import pytest
#from graphs.frequent_pattern_graph_miner import *
#
#
#def test_my_dfs_no_error():
#    paths = []
#    my_dfs.def_globals["paths"] = paths
#    graph = {
#        "A": ["B", "C"],
#        "B": ["D", "E"],
#        "C": ["A", "F"],
#        "D": ["B"],
#        "E": ["B", "F"],
#        "F": ["C", "E"],
#    }
#    # start and end are present in the graph
#    my_dfs(graph, "A", "E")
#    assert paths != []
#
#
#def test_my_dfs_unreachable_nodes():
#    paths = []
#    my_dfs.def_globals["paths"] = paths
#    graph = {"A": ["B"], "B": [], "C": ["D"], "D": []}
#
#    # there is no path from A to C
#    my_dfs(graph, "A", "C")
#    assert paths == []
#
#
#def test_my_dfs_node_to_itself():
#    paths = []
#    my_dfs.def_globals["paths"] = paths
#    graph = {"A": ["B"], "B": ["A"]}
#
#    # there should be a path from a node to itself
#    my_dfs(graph, "A", "A")
#    assert paths != []
#