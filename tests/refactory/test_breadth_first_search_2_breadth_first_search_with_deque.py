from graphs.breadth_first_search_2 import *
import pytest


def test_breadth_first_search_with_deque_no_errors():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    start = "A"
    result = breadth_first_search_with_deque(graph, start)
    assert result is not None, "Function should not return None"


def test_breadth_first_search_with_deque_single_node():
    graph = {"A": []}
    start = "A"
    result = breadth_first_search_with_deque(graph, start)
    assert result == [
        "A"
    ], "Function should return list with single element for graph with single node"


def test_breadth_first_search_with_deque_different_start():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    start = "B"
    result = breadth_first_search_with_deque(graph, start)
    assert "B" in result, "Function should include start node in results"
