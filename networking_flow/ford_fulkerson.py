# Ford-Fulkerson Algorithm for Maximum Flow Problem
"""
Description:
    (1) Start with initial flow as 0;
    (2) Choose augmenting path from source to sink and add path to flow;
"""


from typing import List


def bfs(graph: List[List[int]], s: int, t: int, parent: List[int]) -> bool:
    """
    Breadth-first-search from source node to the sink node.

    Args:
        graph (List[List[int]]): Adjacency matrix representation of the graph.
        s (int): The source node id.
        t (int): The terminal (or sink) node id.
        parent (List[int]): The array to store the path.

    Returns:
        bool: True if a path exists from source to sink node, False otherwise.
    """
    visited = [False] * len(graph)
    queue = [s]
    visited[s] = True

    while queue:
        u = queue.pop(0)
        queue_next_node(queue, visited, graph, u, parent)

    return visited[t]


def ford_fulkerson(graph, source, sink):
    # This array is filled by BFS and to store path
    parent = [-1] * (len(graph))
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink

        while s != source:
            # Find the minimum value in select path
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

def queue_next_node(
    queue: List[int],
    visited: List[bool],
    graph: List[List[int]],
    u: int,
    parent: List[int],
) -> None:
    """
    Append next node into queue if it's not iterated and has edge > 0 with current node.

    Args:
        queue (List[int]): The current queue of nodes in BFS.
        visited (List[bool]): Boolean list marking visited nodes.
        graph (List[List[int]]): Adjacency matrix representation of the graph.
        u (int): The current node id.
        parent (List[int]): The array to store our path.
    """
    for ind in range(len(graph[u])):
        if not visited[ind] and graph[u][ind] > 0:
            queue.append(ind)
            visited[ind] = True
            parent[ind] = u


graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]

source, sink = 0, 5
print(ford_fulkerson(graph, source, sink))
