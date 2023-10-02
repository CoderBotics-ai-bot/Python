"""Prim's Algorithm.

    Determines the minimum spanning tree(MST) of a graph using the Prim's Algorithm.

    Details: https://en.wikipedia.org/wiki/Prim%27s_algorithm
"""

import heapq as hq
import math
from collections.abc import Iterator


from typing import List, Tuple
from typing import List
from heapq import heapify, heappop
from math import inf
from dataclasses import dataclass
from typing import Dict, List, Optional


from typing import List, Iterator, Tuple, Dict, Optional
from heapq import heapify, heappop
from math import inf
from dataclasses import dataclass


class Vertex:
    """Class Vertex."""

    def __init__(self, id_):
        """
        Arguments:
            id - input an id to identify the vertex
        Attributes:
            neighbors - a list of the vertices it is linked to
            edges     - a dict to store the edges's weight
        """
        self.id = str(id_)
        self.key = None
        self.pi = None
        self.neighbors = []
        self.edges = {}  # {vertex:distance}

    def __lt__(self, other):
        """Comparison rule to < operator."""
        return self.key < other.key

    def __repr__(self):
        """Return the vertex id."""
        return self.id

    def add_neighbor(self, vertex):
        """Add a pointer to a vertex at neighbor's list."""
        self.neighbors.append(vertex)

    def add_edge(self, vertex, weight):
        """Destination vertex and weight."""
        self.edges[vertex.id] = weight


def connect(graph, a, b, edge):
    # add the neighbors:
    graph[a - 1].add_neighbor(graph[b - 1])
    graph[b - 1].add_neighbor(graph[a - 1])
    # add the edges:
    graph[a - 1].add_edge(graph[b - 1], edge)
    graph[b - 1].add_edge(graph[a - 1], edge)


def prim(graph: List[Vertex], root: Vertex) -> List[Tuple[int, int]]:
    """Compute the Minimum Spanning Tree of a graph using Prim's Algorithm."""
    a = []
    queue = _initialize_graph(graph, root)

    while queue:
        u = _extract_min_vertex(queue)
        _update_vertex_neighbours(u, queue)

    for vertex in graph[1:]:
        a.append((int(vertex.id) + 1, int(vertex.pi.id) + 1))

    return a


def prim_heap(graph: List[Vertex], root: Vertex) -> Iterator[Tuple[int, int]]:
    """
    Function to execute Prim's algorithm using a min heap data structure to find the minimum spanning tree
    of a connected, undirected graph with weighted edges.

    Yields:
        tuple: Each yield is a tuple of two vertices that forms one edge of the minimum spanning tree.
    """

    h = setup_vertices(graph, root)
    heapify(h)

    while h:
        u = heappop(h)
        for v in u.neighbours:
            adjust_heap_and_vertex(h, v, u)

    for i in range(1, len(graph)):
        yield (graph[i].id + 1, graph[i].pi.id + 1)

def _initialize_graph(graph: List[Vertex], root: Vertex) -> List[Vertex]:
    """Setup initial values for each vertex."""
    for u in graph:
        u.key = math.inf
        u.pi = None
    root.key = 0
    return graph[:]



def setup_vertices(graph: List[Vertex], root: Vertex) -> List[Vertex]:
    """Initialize the vertices for the execution of the Prim's algorithm."""
    inf_value = float(inf)

    for vertex in graph:
        vertex.update_key(inf_value)
        vertex.update_pi(None)

    root.update_key(0)

    return list(graph)


def adjust_heap_and_vertex(h: List[Vertex], v: Vertex, u: Vertex) -> None:
    """Adjust the heap and update the keys of the vertices as per the edge weight."""
    if v in h and u.neighbours[v] < v.key:
        v.update_pi(u)
        v.update_key(u.neighbours[v])
        heapify(h)


def _extract_min_vertex(queue: List[Vertex]) -> Vertex:
    """Extract vertex from queue with minimum cost."""
    u = min(queue)
    queue.remove(u)
    return u


def _update_vertex_neighbours(u: Vertex, queue: List[Vertex]):
    """Update the keys of neighbours of a vertex if current weight is less than previous weight."""
    for v in u.neighbors:
        if (v in queue) and (u.edges[v.id] < v.key):
            v.pi = u
            v.key = u.edges[v.id]


def test_vector() -> None:
    """
    # Creates a list to store x vertices.
    >>> x = 5
    >>> G = [Vertex(n) for n in range(x)]

    >>> connect(G, 1, 2, 15)
    >>> connect(G, 1, 3, 12)
    >>> connect(G, 2, 4, 13)
    >>> connect(G, 2, 5, 5)
    >>> connect(G, 3, 2, 6)
    >>> connect(G, 3, 4, 6)
    >>> connect(G, 0, 0, 0)  # Generate the minimum spanning tree:
    >>> G_heap = G[:]
    >>> MST = prim(G, G[0])
    >>> MST_heap = prim_heap(G, G[0])
    >>> for i in MST:
    ...     print(i)
    (2, 3)
    (3, 1)
    (4, 3)
    (5, 2)
    >>> for i in MST_heap:
    ...     print(i)
    (2, 3)
    (3, 1)
    (4, 3)
    (5, 2)
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
