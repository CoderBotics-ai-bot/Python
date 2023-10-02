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
    Generate a complete graph with vertices_number vertices.
    @input: vertices_number (number of vertices),
            directed (False if the graph is undirected, True otherwise)
    @example:
    >>> complete_graph(3)
    {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    """
    return {
        i: [j for j in range(vertices_number) if i != j] for i in range(vertices_number)
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
