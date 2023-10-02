import pytest
from graphs.greedy_min_vertex_cover import *


@pytest.fixture
def sample_graph():
    return {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}


def test_greedy_min_vertex_cover_exists(sample_graph):
    result = greedy_min_vertex_cover(sample_graph)
    assert result is not None


def test_greedy_min_vertex_cover_return_type(sample_graph):
    result = greedy_min_vertex_cover(sample_graph)
    assert isinstance(result, set)


def test_greedy_min_vertex_cover_empty_input():
    result = greedy_min_vertex_cover({})
    assert isinstance(result, set)
    assert len(result) == 0


@pytest.fixture
def larger_graph():
    return {
        0: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        1: [0, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        2: [0, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        3: [0, 29, 30, 31, 32, 33, 34, 35, 36, 37],
    }


def test_greedy_min_vertex_cover_larger_input(larger_graph):
    result = greedy_min_vertex_cover(larger_graph)
    assert isinstance(result, set)
    assert len(result) == 4  # Only one vertex from each edges is needed
