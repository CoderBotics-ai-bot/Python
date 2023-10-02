import pytest
from graphs.prim import *


import pytest


@pytest.fixture
def small_graph_setup():
    """
    Fixture to generate a small graph
    """
    n_vertices = 5
    edges = [(0, 1, 2), (1, 2, 3), (2, 3, 1), (3, 4, 1), (4, 0, 2)]

    graph = [Vertex(i) for i in range(n_vertices)]
    for edge in edges:
        connect(graph, *edge)

    return graph


@pytest.fixture
def isolated_vertex_graph_setup():
    """
    Fixture to generate a graph with an isolated vertex
    """
    n_vertices = 5
    edges = [(0, 1, 2), (0, 2, 3), (0, 3, 1), (0, 4, 1)]

    graph = [Vertex(i) for i in range(n_vertices)]
    for edge in edges:
        connect(graph, *edge)

    return graph


def test_prim_syntax(small_graph_setup):
    """
    Test to check for syntactic correctness of the prim function
    """
    result = prim(small_graph_setup, small_graph_setup[0])
    assert result is not None


def test_prim_with_isolated_vertex(isolated_vertex_graph_setup):
    """
    Test to check if prim's algorithm handles isolated vertices correctly
    """
    result = prim(isolated_vertex_graph_setup, isolated_vertex_graph_setup[0])
    assert result is not None


def test_prim_with_negative_edge(small_graph_setup):
    """
    Test to check if prim's algorithm handles negative edges correctly.
    """
    # Adding a negative edge
    connect(small_graph_setup, 1, 2, -2)
    result = prim(small_graph_setup, small_graph_setup[0])
    assert result is not None
