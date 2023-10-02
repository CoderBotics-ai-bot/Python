import pytest
from graphs.matching_min_vertex_cover import *


def test_matching_min_vertex_cover_no_errors():
    """
    Test if the function matching_min_vertex_cover runs without errors
    """
    graph = {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}
    result = matching_min_vertex_cover(graph)
    assert result is not None
    assert isinstance(result, set)


def test_matching_min_vertex_cover_empty_graph():
    """
    Test the function matching_min_vertex_cover with an empty graph
    """
    graph = {}
    result = matching_min_vertex_cover(graph)
    assert result is not None
    assert isinstance(result, set)
    assert len(result) == 0


def test_matching_min_vertex_cover_single_vertex_no_edges():
    """
    Test the function matching_min_vertex_cover with a single vertex with no edges
    """
    graph = {0: []}
    result = matching_min_vertex_cover(graph)
    assert result is not None
    assert isinstance(result, set)
    assert len(result) == 0


def test_matching_min_vertex_cover_singe_vertex_self_edges():
    """
    Test the function matching_min_vertex_cover with a single node edge that connects to itself
    """
    graph = {0: [0]}
    result = matching_min_vertex_cover(graph)
    assert result is not None
    assert isinstance(result, set)
    assert len(result) == 1
    assert 0 in result
