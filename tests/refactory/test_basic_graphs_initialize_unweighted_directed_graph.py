from graphs.basic_graphs import *


from typing import List

import pytest
from unittest.mock import patch
from graphs.basic_graphs import initialize_unweighted_directed_graph
from typing import List


@pytest.fixture
def mock_input():
    return iter(["1 2", "2 3"])


@patch("builtins.input")
def test_initialize_unweighted_directed_graph(mock_input):
    mock_input.side_effect = ["1 2", "2 3"]
    graph = initialize_unweighted_directed_graph(3, 2)
    assert graph is not None
    assert graph == {1: [2], 2: [3], 3: []}


def test_initialize_unweighted_directed_graph_no_edges():
    graph = initialize_unweighted_directed_graph(3, 0)
    assert graph is not None
    assert graph == {1: [], 2: [], 3: []}


def test_initialize_unweighted_directed_graph_wrong_type_input_1():
    with pytest.raises(TypeError):
        initialize_unweighted_directed_graph("three", 0)


def test_initialize_unweighted_directed_graph_wrong_type_input_2():
    with pytest.raises(TypeError):
        initialize_unweighted_directed_graph(3, "two")
