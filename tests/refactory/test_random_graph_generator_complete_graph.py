import pytest
from graphs.random_graph_generator import *


def test_complete_graph_functionality():
    """
    Basic functionality test. Checks if the function doesn't throw errors
    when it's executed and it should return something (not None).
    """
    result = complete_graph(5)
    assert result is not None


def test_complete_graph_vertex_count():
    """
    Checks if the number of vertices in the graph is equal to the input value.
    """
    for i in range(1, 51):
        g = complete_graph(i)
        assert len(g) == i, f"Expected {i} vertices, received {len(g)}"


def test_complete_graph_connectivity():
    """
    Checks if every vertex is connected to every other vertex.
    """
    for i in range(2, 51):
        g = complete_graph(i)

        for vertice, edges in g.items():
            assert (
                len(edges) == i - 1
            ), f"Vertice {vertice} is not connected with all other vertices."


def test_complete_graph_no_self_loops():
    """
    Checks if any vertex is connected to itself.
    """
    for i in range(1, 51):
        g = complete_graph(i)
        assert all(
            i not in edges for i, edges in g.items()
        ), "There is a self loop in the graph."
