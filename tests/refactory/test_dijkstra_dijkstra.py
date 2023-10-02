from graphs.dijkstra import *
import pytest


def test_dijkstra_successful_execution():
    graph = {
        "A": [("B", 1), ("C", 3)],
        "B": [("A", 1), ("C", 2)],
        "C": [("A", 3), ("B", 2)],
    }
    start = "A"
    end = "C"

    result = dijkstra(graph, start, end)
    assert result is not None


def test_dijkstra_negative_path():
    graph = {
        "A": [("B", 1)],
        "B": [("A", 1)],
        "C": [],
    }
    start = "A"
    end = "C"

    result = dijkstra(graph, start, end)
    assert result == -1


def test_dijkstra_same_start_and_end():
    graph = {
        "A": [("B", 1), ("C", 3)],
        "B": [("A", 1), ("C", 2)],
        "C": [("A", 3), ("B", 2)],
    }
    start = "A"
    end = "A"

    result = dijkstra(graph, start, end)
    assert result == 0


def test_dijkstra_no_path_but_nodes_exist():
    graph = {"A": [("B", 1)], "B": [("A", 1)], "C": [("D", 2)], "D": [("C", 2)]}
    start = "A"
    end = "C"

    result = dijkstra(graph, start, end)
    assert result == -1
