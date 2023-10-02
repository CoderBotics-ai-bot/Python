from graphs.breadth_first_search_shortest_path_2 import *
import pytest


def test_bfs_shortest_path_no_error():
    demo_graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }
    result = bfs_shortest_path(demo_graph, "G", "D")
    assert result is not None


def test_bfs_shortest_path_positive():
    demo_graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }
    result = bfs_shortest_path(demo_graph, "G", "D")
    assert result == ["G", "F", "E", "B", "D"]


def test_bfs_shortest_path_same_start_and_goal():
    demo_graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }
    result = bfs_shortest_path(demo_graph, "G", "G")
    assert result == ["G"]


def test_bfs_shortest_path_no_path():
    demo_graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }
    result = bfs_shortest_path(demo_graph, "G", "Unknown")
    assert result == []
