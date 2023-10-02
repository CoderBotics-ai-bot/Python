import pytest
from graphs.random_graph_generator import *


def test_random_graph_not_none():
    """
    Test to verify the function random_graph() doesn't throw any errors when it is executed and
    that it doesn't return None.
    """
    result = random_graph(4, 0.5)
    assert result is not None


def test_random_graph_no_edges():
    """
    Test to check if the returned graph doesn't have any edges when probability is 0.
    """
    result = random_graph(4, 0)
    for value in result.values():
        assert not value  # no edges


def test_random_graph_complete():
    """
    Test to check if the returned graph is a complete graph when probability is 1 or more.
    """
    result = random_graph(4, 1)
    for value in result.values():
        assert (
            len(value) == 3
        )  # for a complete graph with 4 vertices, each vertex is connected to 3 others


def test_random_graph_undirected():
    """
    Test to verify the returned graph is undirected when directed = False.
    """
    random.seed(1)
    result = random_graph(4, 0.5)
    # make sure for every edge from u to v, there's an edge from v to u
    for i in range(4):
        for neighbor in result[i]:
            assert i in result[neighbor]


def test_random_graph_directed():
    """
    Test to verify the returned graph is directed when directed = True.
    """
    random.seed(1)
    result = random_graph(4, 0.5, True)
    # make sure for every edge from u to v, there's NO necessary edge from v to u
    for i in range(4):
        for neighbor in result[i]:
            assert i not in result[neighbor]
