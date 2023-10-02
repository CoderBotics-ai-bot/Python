from graphs.strongly_connected_components import *
import pytest


def test_strongly_connected_components_base():
    graph = {0: [1], 1: [2], 2: [0], 3: [], 4: []}
    result = strongly_connected_components(graph)
    assert result is not None


def test_strongly_connected_components_complex():
    graph = {0: [1], 1: [2], 2: [0], 3: [4, 5], 4: [3, 5], 5: [3, 4]}
    result = strongly_connected_components(graph)
    assert len(result) == 2


def test_strongly_connected_components_single_node():
    graph = {0: []}
    result = strongly_connected_components(graph)
    assert len(result) == 1


def test_strongly_connected_components_empty():
    graph = {}
    result = strongly_connected_components(graph)
    assert len(result) == 0
