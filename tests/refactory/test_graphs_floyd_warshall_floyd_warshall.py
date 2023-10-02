
import pytest
from typing import List, Tuple
from graphs.graphs_floyd_warshall import *


@pytest.fixture
def generate_graph() -> Tuple[List[List[float]], int]:
    graph = [
        [0, 1, float("inf"), 1],
        [1, 0, 1, float("inf")],
        [float("inf"), 1, 0, 1],
        [1, float("inf"), 1, 0],
    ]
    v = 4
    return graph, v


def test_floyd_warshall_no_errors(
    generate_graph: Tuple[List[List[float]], int]
) -> None:
    graph, v = generate_graph
    result = floyd_warshall(graph, v)
    assert result is not None


def test_floyd_warshall_correct_output(
    generate_graph: Tuple[List[List[float]], int]
) -> None:
    graph, v = generate_graph
    dist, vertices = floyd_warshall(graph, v)
    assert len(dist) == v
    assert len(dist[0]) == v
    assert vertices == v


def test_floyd_warshall_correct_distances(
    generate_graph: Tuple[List[List[float]], int]
) -> None:
    graph, v = generate_graph
    dist, vertices = floyd_warshall(graph, v)
    assert dist[0][2] == 2
    assert dist[2][0] == 2
