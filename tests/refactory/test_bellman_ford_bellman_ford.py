from graphs.bellman_ford import *
import pytest


import pytest


def test_bellman_ford_no_errors(graph_fixture):
    """
    Test if function bellman_ford runs without errors with correct input
    """
    assert bellman_ford(graph_fixture["correct_edges"], 4, 4, 0) is not None


def test_bellman_ford_negative_cycle(graph_fixture):
    """
    Test if function bellman_ford correctly raises an exception if a negative cycle is detected
    """
    with pytest.raises(Exception) as excinfo:
        bellman_ford(graph_fixture["negative_cycle"], 4, 5, 0)
    assert str(excinfo.value) == "Negative cycle found"


@pytest.fixture
def graph_fixture():
    """
    Fixture for reusing edges with and without negative cycles
    """
    correct_edges = [
        {"src": s, "dst": d, "weight": w}
        for s, d, w in [(2, 1, -10), (3, 2, 3), (0, 3, 5), (0, 1, 4)]
    ]
    negative_cycle = [
        {"src": s, "dst": d, "weight": w}
        for s, d, w in [(2, 1, -10), (3, 2, 3), (0, 3, 5), (0, 1, 4), (1, 3, 5)]
    ]
    return {"correct_edges": correct_edges, "negative_cycle": negative_cycle}
