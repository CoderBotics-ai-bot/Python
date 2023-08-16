#!/usr/bin/env python3

# Author: OMKAR PATHAK, Nwachukwu Chidiebere

# Use a Python dictionary to construct the graph.
from __future__ import annotations

from pprint import pformat
from typing import Generic, TypeVar

T = TypeVar("T")




class GraphAdjacencyList(Generic[T]):

    def __init__(self, directed: bool = True) -> None:
        """
        Parameters:
        directed: (bool) Indicates if graph is directed or undirected. Default is True.
        """

        self.adj_list: dict[T, list[T]] = {}  # dictionary of lists
        self.directed = directed

    def add_edge(
        self, source_vertex: T, destination_vertex: T
    ) -> GraphAdjacencyList[T]:
        """
        This method connects the source_vertex to the destination_vertex. It can handle both directed
        and undirected graphs. If the graph is undirected, the connection is bidirectional while for
        directed graphs it goes from the source_vertex to destination_vertex.

        In case the vertices are not present in the graph, they are added automatically.
        The adjacency list is then updated to indicate the connectivity between these vertices.

        This operation does not return any value.

        Args:
            self: The instance of GraphAdjacencyList.
            source_vertex (T): The source vertex in the graph.
            destination_vertex (T): The destination vertex in the graph.

        Returns:
            self: Returns the instance of the class.

        Raises:
            No exceptions are explicitly raised in this method.

        Side Effects:
            Modifies the adjacency list of the graph by adding edges between the source_vertex
            and the destination_vertex.

        """
        # method body remains the same

        return self

    def __repr__(self) -> str:
        return pformat(self.adj_list)
