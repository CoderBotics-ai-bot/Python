import pytest
from graphs.frequent_pattern_graph_miner import *


def test_freq_subgraphs_edge_list():
    paths = [[[(1, 2)], [(2, 3)], [(3, 4)]], [[(4, 5)], [(5, 6)], [(6, 7)]]]
    result = freq_subgraphs_edge_list(paths)
    assert result is not None


def test_freq_subgraphs_edge_list_empty():
    paths = []
    result = freq_subgraphs_edge_list(paths)
    assert result == []


def test_freq_subgraphs_edge_list_single_path():
    paths = [[[(1, 2)], [(2, 3)]]]
    result = freq_subgraphs_edge_list(paths)
    assert len(result) == 1


def test_freq_subgraphs_edge_list_multiple_paths():
    paths = [[[(1, 2)], [(2, 3)], [(3, 4)]], [[(4, 5)], [(5, 6)], [(6, 7)]]]
    result = freq_subgraphs_edge_list(paths)
    assert len(result) == len(paths)
