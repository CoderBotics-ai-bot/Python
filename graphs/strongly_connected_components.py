"""
https://en.wikipedia.org/wiki/Strongly_connected_component

Finding strongly connected components in directed graph

"""

test_graph_1 = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []}

test_graph_2 = {0: [1, 2, 3], 1: [2], 2: [0], 3: [4], 4: [5], 5: [3]}


def topology_sort(
    graph: dict[int, list[int]], vert: int, visited: list[bool]
) -> list[int]:
    """
    Use depth first search to sort graph
    At this time graph is the same as input
    >>> topology_sort(test_graph_1, 0, 5 * [False])
    [1, 2, 4, 3, 0]
    >>> topology_sort(test_graph_2, 0, 6 * [False])
    [2, 1, 5, 4, 3, 0]
    """

    visited[vert] = True
    order = []

    for neighbour in graph[vert]:
        if not visited[neighbour]:
            order += topology_sort(graph, neighbour, visited)

    order.append(vert)

    return order


def find_components(
    reversed_graph: dict[int, list[int]], vert: int, visited: list[bool]
) -> list[int]:
    """
    Use depth first search to find strongliy connected
    vertices. Now graph is reversed
    >>> find_components({0: [1], 1: [2], 2: [0]}, 0, 5 * [False])
    [0, 1, 2]
    >>> find_components({0: [2], 1: [0], 2: [0, 1]}, 0, 6 * [False])
    [0, 2, 1]
    """

    visited[vert] = True
    component = [vert]

    for neighbour in reversed_graph[vert]:
        if not visited[neighbour]:
            component += find_components(reversed_graph, neighbour, visited)

    return component

def strongly_connected_components(graph: dict[int, list[int]]) -> list[list[int]]:
    """
    Identifies and returns the strongly connected components of a given graph.

    Args:
        graph (dict[int, list[int]]): The input graph as a dictionary where
            each key represents a vertex and the corresponding value is a list
            of all adjacent vertices.

    Returns:
        list[list[int]]: A list of strongly connected components where each
            component is represented as a list of vertices.
    """
    order = get_topological_sort(graph)
    reversed_graph = build_reversed_graph(graph)
    return find_components_in_order(order, reversed_graph)


def get_topological_sort(graph: dict[int, list[int]]) -> list[int]:
    visited = [False] * len(graph)
    order = []
    for i in range(len(graph)):
        if not visited[i]:
            order += topology_sort(graph, i, visited)
    return order


def build_reversed_graph(graph: dict[int, list[int]]) -> dict[int, list[int]]:
    reversed_graph = {vert: [] for vert in range(len(graph))}
    for vert, neighbours in graph.items():
        for neighbour in neighbours:
            reversed_graph[neighbour].append(vert)
    return reversed_graph


def find_components_in_order(
    order: list[int], reversed_graph: dict[int, list[int]]
) -> list[list[int]]:
    components_list = []
    visited = [False] * len(reversed_graph)
    for i in range(len(reversed_graph)):
        vert = order[len(reversed_graph) - i - 1]
        if not visited[vert]:
            component = find_components(reversed_graph, vert, visited)
            components_list.append(component)
    return components_list
