"""
Finding the shortest path in 0-1-graph in O(E + V) which is faster than dijkstra.
0-1-graph is the weighted graph with the weights equal to 0 or 1.
Link: https://codeforces.com/blog/entry/22276
"""
from __future__ import annotations

from collections import deque
from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Edge:
    """Weighted directed graph edge."""

    destination_vertex: int
    weight: int




class AdjacencyList:

    def __init__(self, size: int):
        self._graph: list[list[Edge]] = [[] for _ in range(size)]
        self._size = size

    def __getitem__(self, vertex: int) -> Iterator[Edge]:
        """Get all the vertices adjacent to the given one."""
        return iter(self._graph[vertex])

    @property
    def size(self):
        return self._size

    def add_edge(self, from_vertex: int, to_vertex: int, weight: int):
        """
        >>> g = AdjacencyList(2)
        >>> g.add_edge(0, 1, 0)
        >>> g.add_edge(1, 0, 1)
        >>> list(g[0])
        [Edge(destination_vertex=1, weight=0)]
        >>> list(g[1])
        [Edge(destination_vertex=0, weight=1)]
        >>> g.add_edge(0, 1, 2)
        Traceback (most recent call last):
            ...
        ValueError: Edge weight must be either 0 or 1.
        >>> g.add_edge(0, 2, 1)
        Traceback (most recent call last):
            ...
        ValueError: Vertex indexes must be in [0; size).
        """
        if weight not in (0, 1):
            raise ValueError("Edge weight must be either 0 or 1.")

        if to_vertex < 0 or to_vertex >= self.size:
            raise ValueError("Vertex indexes must be in [0; size).")

        self._graph[from_vertex].append(Edge(to_vertex, weight))


    def get_shortest_path(self, start_vertex: int, finish_vertex: int) -> int | None:
        """
        Return the shortest distance from start_vertex to finish_vertex in a 0-1 graph.

        This method uses the breadth-first search algorithm to find the shortest path.
        It maintains a queue of vertices to visit along with their current distance from
        the start_vertex. Edges with a weight of 0 are processed first, thereby ensuring
        the shortest path is found.

        :param start_vertex: the starting vertex of the path.
        :param finish_vertex: the ending vertex of the path.
        :return: the shortest distance from the starting vertex to the ending vertex or
        raises a ValueError when no path exists.

        :raises ValueError: if there is no path from the starting vertex to the ending vertex.
        """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
