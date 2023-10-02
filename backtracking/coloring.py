"""
    Graph Coloring also called "m coloring problem"
    consists of coloring a given graph with at most m colors
    such that no adjacent vertices are assigned the same color

    Wikipedia: https://en.wikipedia.org/wiki/Graph_coloring
"""


def valid_coloring(
    neighbours: list[int], colored_vertices: list[int], color: int
) -> bool:
    """
    For each neighbour check if the coloring constraint is satisfied
    If any of the neighbours fail the constraint return False
    If all neighbours validate the constraint return True

    >>> neighbours = [0,1,0,1,0]
    >>> colored_vertices = [0, 2, 1, 2, 0]

    >>> color = 1
    >>> valid_coloring(neighbours, colored_vertices, color)
    True

    >>> color = 2
    >>> valid_coloring(neighbours, colored_vertices, color)
    False
    """
    # Does any neighbour not satisfy the constraints
    return not any(
        neighbour == 1 and colored_vertices[i] == color
        for i, neighbour in enumerate(neighbours)
    )

def util_color(
    graph: list[list[int]], max_colors: int, colored_vertices: list[int], index: int
) -> bool:
    """
    Try to color the graph using a recursive, depth-first approach.
    Args:
        graph (list[list[int]]): Adjacency matrix of the graph to color.
        max_colors (int): Maximum number of different colors that can be used.
        colored_vertices (list[int]):
            List that will hold the color for each vertex. -1 indicates that vertex is not yet colored.
        index (int): The index of the current vertex to try and color.
    Returns:
        bool: True if a valid coloring of the graph was found. False otherwise.
    """
    if index == len(graph):
        return True

    for i in range(max_colors):
        if valid_coloring(graph[index], colored_vertices, i):
            colored_vertices[index] = i
            if util_color(graph, max_colors, colored_vertices, index + 1):
                return True
            colored_vertices[index] = -1

    return False


def color(graph: list[list[int]], max_colors: int) -> list[int]:
    """
    Wrapper function to call subroutine called util_color
    which will either return True or False.
    If True is returned colored_vertices list is filled with correct colorings

    >>> graph = [[0, 1, 0, 0, 0],
    ...          [1, 0, 1, 0, 1],
    ...          [0, 1, 0, 1, 0],
    ...          [0, 1, 1, 0, 0],
    ...          [0, 1, 0, 0, 0]]

    >>> max_colors = 3
    >>> color(graph, max_colors)
    [0, 1, 0, 2, 0]

    >>> max_colors = 2
    >>> color(graph, max_colors)
    []
    """
    colored_vertices = [-1] * len(graph)

    if util_color(graph, max_colors, colored_vertices, 0):
        return colored_vertices

    return []
