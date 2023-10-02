#from graphs.basic_graphs import *
#import pytest
#
#
#def test_initialize_unweighted_undirected_graph_no_throw():
#    with patch("builtins.input", return_value="1 2"):
#        assert initialize_unweighted_undirected_graph(2, 1) is not None
#
#
#def test_initialize_unweighted_undirected_graph_correct_output():
#    with patch("builtins.input", return_value="1 2"):
#        result = initialize_unweighted_undirected_graph(2, 1)
#        assert result is not None
#        assert result == {1: [2], 2: [1]}
#
#
#def test_initialize_unweighted_undirected_graph_zero_edges():
#    with patch("builtins.input", return_value="1 2"):
#        result = initialize_unweighted_undirected_graph(2, 0)
#        assert result is not None
#        assert result == {1: [], 2: []}
#
#
#def test_initialize_unweighted_undirected_graph_edge_count_greater_than_possible():
#    with patch("builtins.input", return_value="1 2"):
#        result = initialize_unweighted_undirected_graph(3, 4)
#        assert result is not None
#        assert len(result) == 3
#