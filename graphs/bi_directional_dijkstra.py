"""
Bi-directional Dijkstra's algorithm.

A bi-directional approach is an efficient and
less time consuming optimization for Dijkstra's
searching algorithm

Reference: shorturl.at/exHM7
"""
from typing import Any

import numpy as np


from queue import PriorityQueue


from typing import Any, Dict, List, Optional, Tuple

# Author: Swayam Singh (https://github.com/practice404)


from queue import PriorityQueue

def pass_and_relaxation(
    graph: dict,
    v: str,
    visited_forward: set,
    visited_backward: set,
    cst_fwd: dict,
    cst_bwd: dict,
    queue: Any,
    parent: dict,
    shortest_distance: float,
) -> float:
    """
    Perform one iteration of pass and relaxation for Bidirectional Dijkstra's algorithm.
    """
    for nxt, d in graph[v]:
        if nxt in visited_forward:
            continue

        new_cost_f = cst_fwd[v] + d
        shortest_distance = update_shortest_distance(
            nxt, visited_backward, cst_fwd, cst_bwd, new_cost_f, shortest_distance
        )

        old_cost_f = cst_fwd.get(nxt, np.inf)
        if new_cost_f < old_cost_f:
            queue.put((new_cost_f, nxt))
            cst_fwd[nxt] = new_cost_f
            parent[nxt] = v
    return shortest_distance


def bidirectional_dij(
    source: str,
    destination: str,
    graph_forward: Dict[str, List[Tuple[str, int]]],
    graph_backward: Dict[str, List[Tuple[str, int]]],
) -> int:
    shortest_path_distance = -1

    visited_forward = set()
    visited_backward = set()

    queue_forward: PriorityQueue[Tuple[int, str]] = PriorityQueue()
    queue_backward: PriorityQueue[Tuple[int, str]] = PriorityQueue()

    shortest_distance = np.inf

    queue_forward.put((0, source))
    queue_backward.put((0, destination))

    if source == destination:
        return 0

    (
        cst_fwd,
        cst_bwd,
        parent_forward,
        parent_backward,
    ) = initialize_cost_and_parent_dicts(source, destination)

    continue_loop, shortest_distance = True, np.inf
    while not queue_forward.empty() and not queue_backward.empty() and continue_loop:
        _, v_fwd = update_visited_and_queue(visited_forward, queue_forward)
        _, v_bwd = update_visited_and_queue(visited_backward, queue_backward)

        shortest_distance = pass_and_relaxation(
            graph_forward,
            v_fwd,
            visited_forward,
            visited_backward,
            cst_fwd,
            cst_bwd,
            queue_forward,
            parent_forward,
            shortest_distance,
        )

        shortest_distance = pass_and_relaxation(
            graph_backward,
            v_bwd,
            visited_backward,
            visited_forward,
            cst_bwd,
            cst_fwd,
            queue_backward,
            parent_backward,
            shortest_distance,
        )

        continue_loop, shortest_distance = calculate_shortest_distance(
            shortest_distance, cst_fwd, cst_bwd, v_fwd, v_bwd
        )

    if shortest_distance != np.inf:
        shortest_path_distance = shortest_distance
    return shortest_path_distance


def update_shortest_distance(
    nxt: str,
    visited_backward: set,
    cst_fwd: dict,
    cst_bwd: dict,
    new_cost_f: float,
    shortest_distance: float,
) -> float:
    """Update shortest distance."""
    if nxt in visited_backward:
        shortest_distance = min(shortest_distance, new_cost_f + cst_bwd[nxt])
    return shortest_distance

def initialize_cost_and_parent_dicts(
    source: str, destination: str
) -> Tuple[
    Dict[str, int], Dict[str, int], Dict[str, Optional[str]], Dict[str, Optional[str]]
]:
    cst_fwd = {source: 0}
    cst_bwd = {destination: 0}
    parent_forward = {source: None}
    parent_backward = {destination: None}
    return cst_fwd, cst_bwd, parent_forward, parent_backward


def update_visited_and_queue(
    v: str, visited: set, queue: PriorityQueue[Tuple[int, str]]
):
    visited.add(v)
    queue.get()


def calculate_shortest_distance(
    shortest_distance: float,
    cst_fwd: Dict[str, float],
    cst_bwd: Dict[str, float],
    v_fwd: str,
    v_bwd: str,
) -> float:
    if cst_fwd[v_fwd] + cst_bwd[v_bwd] >= shortest_distance:
        return False, shortest_distance
    else:
        return True, shortest_distance


graph_fwd = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["G", 2]],
    "F": [],
    "G": [["F", 1]],
}
graph_bwd = {
    "B": [["E", 1]],
    "C": [["B", 1]],
    "D": [["C", 1]],
    "F": [["D", 1], ["G", 1]],
    "E": [[None, np.inf]],
    "G": [["E", 2]],
}

if __name__ == "__main__":
    import doctest

    doctest.testmod()
