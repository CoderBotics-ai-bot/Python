import pytest
from graphs.frequent_pattern_graph_miner import *


@pytest.fixture
def edge_array_fixture():
    return [
        [["b", "c"], ["d", "e"]],
        [["f", "g"], ["h", "i"]],
        [["j", "k"], ["l", "m"]],
    ]


def test_get_bitcode(edge_array_fixture):
    # Testing when edge array is empty
    assert get_bitcode([], "a") is not None

    # Testing when distinct_edge is not found in the edge_array
    distinct_edge = "n"
    assert get_bitcode(edge_array_fixture, distinct_edge) == "000"

    # Testing when distinct_edge is found in the edge_array
    distinct_edge = "b"
    assert get_bitcode(edge_array_fixture, distinct_edge) == "100"
