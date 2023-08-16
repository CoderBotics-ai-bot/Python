from graphs.breadth_first_search_zero_one_shortest_path import *
import pytest


import pytest


def test_get_shortest_path_success():
    # Given
    g = AdjacencyList(11)
    g.add_edge(0, 1, 0)
    g.add_edge(0, 3, 1)
    g.add_edge(1, 2, 0)
    g.add_edge(2, 3, 0)
    g.add_edge(4, 2, 1)
    g.add_edge(4, 5, 1)
    g.add_edge(4, 6, 1)
    g.add_edge(5, 9, 0)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 1)
    g.add_edge(8, 10, 1)
    g.add_edge(9, 7, 0)
    g.add_edge(9, 10, 1)

    # When & Then
    assert g.get_shortest_path(0, 3) == 0
    assert g.get_shortest_path(4, 10) == 2
    assert g.get_shortest_path(4, 8) == 2
    assert g.get_shortest_path(0, 1) == 0


def test_get_shortest_path_no_path():
    # Given
    g = AdjacencyList(11)
    g.add_edge(0, 1, 0)
    g.add_edge(0, 3, 1)
    g.add_edge(1, 2, 0)
    g.add_edge(2, 3, 0)
    g.add_edge(4, 2, 1)
    g.add_edge(4, 5, 1)
    g.add_edge(4, 6, 1)
    g.add_edge(5, 9, 0)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 1)
    g.add_edge(8, 10, 1)
    g.add_edge(9, 7, 0)
    g.add_edge(9, 10, 1)

    # When & Then
    with pytest.raises(ValueError) as e:
        g.get_shortest_path(0, 4)
    assert str(e.value) == "No path from start_vertex to finish_vertex."

    with pytest.raises(ValueError) as e:
        g.get_shortest_path(1, 0)
    assert str(e.value) == "No path from start_vertex to finish_vertex."
