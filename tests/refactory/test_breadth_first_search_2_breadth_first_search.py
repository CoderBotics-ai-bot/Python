from graphs.breadth_first_search_2 import *
import pytest


def test_breadth_first_search_no_errors():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    start = "A"
    result = breadth_first_search(graph, start)
    assert result is not None


def test_breadth_first_search_empty():
    graph = {}
    start = "A"
    with pytest.raises(KeyError):
        breadth_first_search(graph, start)


def test_breadth_first_search_single_node():
    graph = {"A": []}
    start = "A"
    result = breadth_first_search(graph, start)
    assert result == ["A"]


def test_breadth_first_search_different_start():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    start = "C"
    result = breadth_first_search(graph, start)
    assert "C" in result
