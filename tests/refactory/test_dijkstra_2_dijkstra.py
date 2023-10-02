
import pytest


from typing import List
from graphs.dijkstra_2 import *
import pytest


def test_dijkstra_no_errors(
    graph_fixture: List[List[float]], v_fixture: int, src_fixture: int
):
    try:
        dijkstra(graph_fixture, v_fixture, src_fixture)
    except Exception as e:
        pytest.fail(f"Dijkstra execution raised {type(e).__name__} Exception. {str(e)}")


def test_dijkstra_with_empty_graph():
    v = 3
    src = 0
    graph = [[0] * v for _ in range(v)]
    try:
        dijkstra(graph, v, src)
    except Exception as e:
        pytest.fail(f"Dijkstra execution raised {type(e).__name__} Exception. {str(e)}")


def test_dijkstra_with_all_infinite_graph():
    v = 3
    src = 0
    graph = [[float("inf")] * v for _ in range(v)]
    try:
        dijkstra(graph, v, src)
    except Exception as e:
        pytest.fail(f"Dijkstra execution raised {type(e).__name__} Exception. {str(e)}")


@pytest.fixture
def graph_fixture():
    return [[0, 2, float("inf")], [2, 0, 3], [float("inf"), 3, 0]]


@pytest.fixture
def v_fixture():
    return 3


@pytest.fixture
def src_fixture():
    return 0
