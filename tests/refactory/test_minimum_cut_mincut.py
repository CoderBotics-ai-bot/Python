
import pytest
from networking_flow.minimum_cut import *
from typing import List, Tuple


@pytest.fixture
def valid_graph_input() -> List[List[int]]:
    return [
        [0, 1, 2, 3, 4, 5],
        [1, 0, 2, 3, 4, 5],
        [2, 1, 0, 3, 4, 5],
        [3, 1, 2, 0, 4, 5],
        [4, 1, 2, 3, 0, 5],
        [5, 1, 2, 3, 4, 0],
    ]


@pytest.fixture
def invalid_graph_input() -> List[List[int]]:
    return [
        [0, 1, 2, 3],
        [1, 0, 2, 3],
        [2, 1, 0, 3],
    ]


@pytest.fixture
def valid_source_sink() -> Tuple[int, int]:
    return (0, 3)


@pytest.fixture
def invalid_source_sink() -> Tuple[int, int]:
    return (0, 9)


def test_mincut_when_input_is_valid_and_correct_returns_expected_result(
    valid_graph_input, valid_source_sink
) -> None:
    source, sink = valid_source_sink
    result = mincut(valid_graph_input, source, sink)
    assert result is not None, "Test failed, returned None"
    assert isinstance(result, list), "Test failed, output is not a list"
    for ele in result:
        assert isinstance(
            ele, tuple
        ), "Test failed, a non-tuple element found in the result list"


def test_mincut_when_input_is_valid_but_incorrect_returns_exception(
    invalid_graph_input, valid_source_sink
) -> None:
    source, sink = valid_source_sink
    with pytest.raises(Exception):
        mincut(invalid_graph_input, source, sink)


def test_mincut_when_source_sink_is_invalid_returns_exception(
    valid_graph_input, invalid_source_sink
) -> None:
    source, sink = invalid_source_sink
    with pytest.raises(Exception):
        mincut(valid_graph_input, source, sink)
