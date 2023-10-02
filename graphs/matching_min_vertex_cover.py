"""
* Author: Manuel Di Lullo (https://github.com/manueldilullo)
* Description: Approximization algorithm for minimum vertex cover problem.
               Matching Approach. Uses graphs represented with an adjacency list

URL: https://mathworld.wolfram.com/MinimumVertexCover.html
URL: https://www.princeton.edu/~aaa/Public/Teaching/ORF523/ORF523_Lec6.pdf
"""

def matching_min_vertex_cover(graph: dict) -> set:
    """
    Approximation Algorithm for the minimum Vertex Cover problem using a Matching Approach.

    This function employs a matching-based approach to approximately solve the
    minimum vertex cover problem (an NP-hard problem). The algorithm continues to
    select arbitrary edges until no edges remain. It then adds both vertices to
    the vertex cover, and removes all edges incident to these vertices.

    Args:
        graph (dict): Graph represented as an adjacency list where each vertex is
            an integer.

    Returns:
        set: A set of nodes forming an approximate minimal vertex cover for the graph.

    Example:
        >>> matching_min_vertex_cover({0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]})
        {0, 1, 2, 4}
    """
    chosen_vertices = set()
    edges = get_edges(graph)

    while edges:
        edge = edges.pop()
        chosen_vertices.update(edge)
        edges = _discard_incident_edges(edges, edge)

    return chosen_vertices


def get_edges(graph: dict) -> set:
    """
    Return a set of couples that represents all of the edges.
    @input: graph (graph stored in an adjacency list where each vertex is
            represented as an integer)
    @example:
    >>> graph = {0: [1, 3], 1: [0, 3], 2: [0, 3], 3: [0, 1, 2]}
    >>> get_edges(graph)
    {(0, 1), (3, 1), (0, 3), (2, 0), (3, 0), (2, 3), (1, 0), (3, 2), (1, 3)}
    """
    edges = set()
    for from_node, to_nodes in graph.items():
        for to_node in to_nodes:
            edges.add((from_node, to_node))
    return edges


def _discard_incident_edges(edges: set, selected_edge: tuple) -> set:
    """
    Discard any edge incident to the vertices in the selected edge.

    Args:
        edges (set): A set of edges in the graph.
        selected_edge (tuple): The selected edge.

    Returns:
        set: The updated set of edges.
    """
    return {edge for edge in edges if not _edge_is_incident(edge, selected_edge)}


def _edge_is_incident(edge: tuple, another_edge: tuple) -> bool:
    """
    Determine if an edge is incident to another edge. An edge is incident
    to another edge if they share a vertex.

    Args:
        edge (tuple): The edge to check for incidence.
        another_edge (tuple): The another edge.

    Returns:
        bool: True if the edge is incident to the another edge, False otherwise.
    """
    return any(vertex in another_edge for vertex in edge)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # graph = {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}
    # print(f"Matching vertex cover:\n{matching_min_vertex_cover(graph)}")
