

from typing import List, Tuple


def topological_sort(graph: dict) -> None:
    indegree = calculate_indegrees(graph)

    if check_for_cycle(indegree):
        print("Cycle exists")
        return

    queue = initial_vertices_to_process(indegree)
    visited_vertices, indegree = visit_nodes(graph, indegree, queue)

    print(visited_vertices)


# Adjacency List of Graph
graph = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []}

def calculate_indegrees(graph: dict) -> List[int]:
    """
    Calculate the indegree for each node in the graph.

    Args:
        graph (dict): A dictionary representing the graph.

    Returns:
        A list of indegrees for each node in graph.
    """
    indegree = [0] * len(graph)

    for values in graph.values():
        for node in values:
            indegree[node] += 1

    return indegree


def check_for_cycle(indegree: List[int]) -> bool:
    """
    Check if the graph contains a cycle.

    Args:
        indegree (List[int]): The indegrees for each node in the graph.

    Returns:
        A boolean indicating if the graph contains a cycle.
    """
    return indegree != len(graph)


def initial_vertices_to_process(indegree: List[int]) -> List[int]:
    """
    Identify the initial list of nodes to process.

    Args:
        indegree (List[int]): The indegrees for each node in the graph.

    Returns:
        A list of vertices with indegree zero i.e. no incoming edges.
    """
    return [i for i in range(len(indegree)) if indegree[i] == 0]


def visit_nodes(
    graph: dict, indegree: List[int], queue: List[int]
) -> Tuple[List[int], List[int]]:
    """
    Visit all nodes in graph by starting with nodes in the queue.

    Args:
        graph (dict): A dictionary representing the graph.
        indegree (List[int]):  The indegrees for each node in the graph.
        queue (List[int]): A list of vertices to start visiting with.

    Returns:
        A tuple of a list of visited vertices and the updated indegrees.
    """
    visited_vertices = []

    while queue:
        node = queue.pop(0)
        visited_vertices.append(node)

        for adjacent_node in graph[node]:
            indegree[adjacent_node] -= 1
            if indegree[adjacent_node] == 0:
                queue.append(adjacent_node)

    return visited_vertices, indegree
topological_sort(graph)
