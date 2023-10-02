from graphs.bellman_ford import *
import pytest


def test_check_negative_cycle_no_errors():
    graph = [
        {"src": 0, "dst": 1, "weight": -1},
        {"src": 1, "dst": 2, "weight": -3},
        {"src": 2, "dst": 0, "weight": -2},
        {"src": 2, "dst": 3, "weight": -1},
    ]
    distance = [0, float("inf"), float("inf"), float("inf")]
    edge_count = len(graph)
    try:
        result = check_negative_cycle(graph, distance, edge_count)
    except Exception as e:
        pytest.fail(
            f"check_negative_cycle() raised {type(e).__name__} when it shouldn't."
        )
    assert result is not None, "check_negative_cycle() returned None when it shouldn't."


def test_check_negative_cycle_with_negative_cycle():
    graph = [
        {"src": 0, "dst": 1, "weight": -1},
        {"src": 1, "dst": 2, "weight": -3},
        {"src": 2, "dst": 0, "weight": -2},
        {"src": 2, "dst": 3, "weight": -1},
    ]
    distance = [0, float("inf"), float("inf"), float("inf")]
    edge_count = len(graph)
    result = check_negative_cycle(graph, distance, edge_count)
    assert (
        result is True
    ), "check_negative_cycle() should have detected a negative cycle but didn't."
