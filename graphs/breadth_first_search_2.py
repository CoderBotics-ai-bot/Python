"""
https://en.wikipedia.org/wiki/Breadth-first_search
pseudo-code:
breadth_first_search(graph G, start vertex s):
// all nodes initially unexplored
mark s as explored
let Q = queue data structure, initialized with s
while Q is non-empty:
    remove the first node of Q, call it v
    for each edge(v, w):  // for w in graph[v]
        if w unexplored:
            mark w as explored
            add w to Q (at the end)
"""
from __future__ import annotations

from collections import deque
from queue import Queue
from timeit import timeit
from typing import List
from typing import Dict, List

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

def breadth_first_search(graph: dict, start: str) -> List[str]:
    """
    Performs a breadth first search on a graph starting from a given node.

    The breadth first search algorithm starts at the root node and explores all the neighboring nodes.
    Then, all the unexplored neighbor nodes are explored, and so on, until all the nodes in the graph have been reached.

    Args:
        graph (dict): The graph to be searched in a dictionary format.
                      The dictionary contains each node as a key and a list of neighboring nodes as its value.
        start (str): The starting node for the search.

    Returns:
        List[str]: A list of nodes traversed during the search. The order of the nodes in the list represents the order of their traversal.
    """
    explored, queue = set([start]), deque([start])
    result = []

    while queue:
        v = queue.popleft()
        result.append(v)

        # We add nodes connected to the current node to the queue if not explored.
        queue.extend(w for w in graph[v] if w not in explored and not explored.add(w))

    return result

def breadth_first_search_with_deque(graph: dict, start: str) -> list[str]:
    """
    Implementation of breadth first search using collections.deque.

    Args:
        graph (dict): A representation of the graph as an adjacency list.
        start (str): The starting node for the search.

    Returns:
        list[str]: A list of the nodes in the order they were visited.
    """
    visited = {start}
    queue = deque([start])
    result = []

    def _visit_node() -> None:
        node = queue.popleft()
        result.append(node)
        unvisited_children = (child for child in graph[node] if child not in visited)
        for child in unvisited_children:
            visited.add(child)
            queue.append(child)

    while queue:
        _visit_node()

    return result


def benchmark_function(name: str) -> None:
    setup = f"from __main__ import G, {name}"
    number = 10000
    res = timeit(f"{name}(G, 'A')", setup=setup, number=number)
    print(f"{name:<35} finished {number} runs in {res:.5f} seconds")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    benchmark_function("breadth_first_search")
    benchmark_function("breadth_first_search_with_deque")
    # breadth_first_search                finished 10000 runs in 0.20999 seconds
    # breadth_first_search_with_deque     finished 10000 runs in 0.01421 seconds
