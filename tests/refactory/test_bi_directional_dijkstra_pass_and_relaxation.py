from graphs.bi_directional_dijkstra import *
import pytest


def test_pass_and_relaxation_exists():
    assert pass_and_relaxation is not None


def test_pass_and_relaxation_no_errors():
    from queue import PriorityQueue

    graph = {"x": [("y", 3), ("z", 4)], "y": [("z", 2)], "z": []}
    v = "x"
    visited_forward = set()
    visited_backward = set()
    cst_fwd = {"x": 0, "y": float("inf"), "z": float("inf")}
    cst_bwd = {"x": float("inf"), "y": float("inf"), "z": 0}
    queue = PriorityQueue()
    parent = {}
    shortest_distance = float("inf")

    assert (
        pass_and_relaxation(
            graph,
            v,
            visited_forward,
            visited_backward,
            cst_fwd,
            cst_bwd,
            queue,
            parent,
            shortest_distance,
        )
        is not None
    )


def test_pass_and_relaxation_correct_values():
    from queue import PriorityQueue

    graph = {"x": [("y", 3), ("z", 4)], "y": [("z", 2)], "z": []}
    v = "x"
    visited_forward = set()
    visited_backward = set()
    cst_fwd = {"x": 0, "y": float("inf"), "z": float("inf")}
    cst_bwd = {"x": float("inf"), "y": float("inf"), "z": 0}
    queue = PriorityQueue()
    parent = {}
    shortest_distance = float("inf")
    result = pass_and_relaxation(
        graph,
        v,
        visited_forward,
        visited_backward,
        cst_fwd,
        cst_bwd,
        queue,
        parent,
        shortest_distance,
    )

    assert result == float("inf")


def test_pass_and_relaxation_correct_values_backward_visited():
    from queue import PriorityQueue

    graph = {"x": [("y", 3), ("z", 4)], "y": [("z", 2)], "z": []}
    v = "x"
    visited_forward = set()
    visited_backward = {"y"}
    cst_fwd = {"x": 0, "y": float("inf"), "z": float("inf")}
    cst_bwd = {"x": float("inf"), "y": 0, "z": 0}
    queue = PriorityQueue()
    parent = {}
    shortest_distance = float("inf")
    result = pass_and_relaxation(
        graph,
        v,
        visited_forward,
        visited_backward,
        cst_fwd,
        cst_bwd,
        queue,
        parent,
        shortest_distance,
    )

    assert result == 3


def test_pass_and_relaxation_correct_values_no_edges():
    from queue import PriorityQueue

    graph = {"x": [], "y": [("z", 2)], "z": []}
    v = "x"
    visited_forward = set()
    visited_backward = {"y"}
    cst_fwd = {"x": 0, "y": float("inf"), "z": float("inf")}
    cst_bwd = {"x": float("inf"), "y": 0, "z": 0}
    queue = PriorityQueue()
    parent = {}
    shortest_distance = float("inf")
    result = pass_and_relaxation(
        graph,
        v,
        visited_forward,
        visited_backward,
        cst_fwd,
        cst_bwd,
        queue,
        parent,
        shortest_distance,
    )

    assert result == float("inf")
