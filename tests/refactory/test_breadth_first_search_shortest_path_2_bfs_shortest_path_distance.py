from graphs.breadth_first_search_shortest_path_2 import *
import pytest


def test_bfs_shortest_path_distance_no_error():
    graph = {"A": ["B"], "B": ["A"], "C": []}
    assert bfs_shortest_path_distance(graph, "A", "B") is not None


def test_bfs_shortest_path_distance_positive():
    graph = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
    assert bfs_shortest_path_distance(graph, "A", "C") == 1


def test_bfs_shortest_path_distance_same_start_and_goal():
    graph = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
    assert bfs_shortest_path_distance(graph, "A", "A") == 0


def test_bfs_shortest_path_distance_no_path():
    graph = {"A": ["B"], "B": ["A"], "C": []}
    assert bfs_shortest_path_distance(graph, "A", "C") == -1


def test_bfs_shortest_path_distance_empty_graph():
    graph = {}
    assert bfs_shortest_path_distance(graph, "A", "C") == -1


def test_bfs_shortest_path_distance_null_nodes():
    graph = {"A": ["B"], "B": ["A"], "C": []}
    assert bfs_shortest_path_distance(graph, None, "C") == -1
    assert bfs_shortest_path_distance(graph, "A", None) == -1
