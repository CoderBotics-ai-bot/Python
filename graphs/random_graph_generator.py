"""
* Author: Manuel Di Lullo (https://github.com/manueldilullo)
* Description: Random graphs generator.
               Uses graphs represented with an adjacency list.

URL: https://en.wikipedia.org/wiki/Random_graph
"""

import random

def random_graph(
    vertices_number: int, probability: float, directed: bool = False
) -> dict:
    """Generate a random adjacency-list representation of a graph based on the number of vertices, edge probability,
    and whether it is directed or not."""
    # Return complete graph if probability >= 1
    if probability >= 1:
        return complete_graph(vertices_number)

    # Return graph without edges if probability <= 0
    if probability <= 0:
        return {i: [] for i in range(vertices_number)}

    # Generate edges for the graph
    adjacency_list = generate_edges(vertices_number, probability, directed)
    return adjacency_list

def complete_graph(vertices_number: int) -> dict:
    """
    Function to generate a complete graph with a specified number of vertices.

    A complete graph is a simple undirected graph in which every pair of distinct vertices is connected by a unique edge.

    Args:
        vertices_number (int): The number of vertices to be included in the graph.

    Returns:
        dict: A dictionary representing the vertices and edges of the complete graph.
              Each key in the dictionary represents a vertex.
              The corresponding value is a list of all other vertices (i.e., the ones with which the key vertex is connected).
              For example, for a graph with 3 vertices, the output will be {0: [1, 2], 1: [0, 2], 2: [0, 1]}.

    Example:
        >>> complete_graph(3)
        {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    """
    vertices = list(range(vertices_number))
    return {
        vertex: [other_vertex for other_vertex in vertices if other_vertex != vertex]
        for vertex in vertices
    }


def generate_edges(vertices_number: int, probability: float, directed: bool) -> dict:
    """Generates and returns edges of a graph based on the number of vertices, edge probability,
    and whether it's directed or not."""
    graph = {i: [] for i in range(vertices_number)}

    for i in range(vertices_number):
        for j in range(i + 1, vertices_number):
            if random.random() < probability:
                graph[i].append(j)
                if not directed:
                    graph[j].append(i)

    return graph


if __name__ == "__main__":
    import doctest

    doctest.testmod()
