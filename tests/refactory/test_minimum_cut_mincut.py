from networking_flow.minimum_cut import *
import pytest


@pytest.fixture
def setUpGraph():
    test_graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0],
    ]
    return test_graph


def test_mincut_function_does_not_fail_with_correct_inputs(setUpGraph):
    source = 0
    sink = 5
    result = mincut(setUpGraph, source, sink)
    assert result is not None


def test_mincut_function_returns_correct_portion(setUpGraph):
    source = 0
    sink = 5
    result = mincut(setUpGraph, source, sink)
    assert isinstance(result, list)
    assert all(isinstance(i, tuple) and len(i) == 2 for i in result)


def test_mincut_function_raise_error_if_source_sink_out_of_bound(setUpGraph):
    source = 8
    sink = 5
    with pytest.raises(IndexError):
        mincut(setUpGraph, source, sink)
