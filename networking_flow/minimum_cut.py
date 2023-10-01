# Minimum cut on Ford_Fulkerson algorithm.

test_graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]


from typing import List


from typing import List, Tuple

def bfs(graph: List[List[int]], s: int, t: int, parent: List[int]) -> bool:
    """
    Performs a breadth-first search (BFS) on the graph from the given source to target.

    This function iterates through all nodes in the graph, for each node it checks all its
    neighbors. If a neighbor has not been visited and the current edge's weight is greater
    than 0, it gets added to the queue for future investigation.

    Args:
    graph (List[List[int]]): A nested list representing the graph in adjacency matrix format,
                             where each inner list represents a node and the elements represent the edge weights.
    s (int): The index of the start node.
    t (int): The index of the target node.
    parent (List[int]): A list where the index represents the node and the value represents
                        the node's parent.

    Returns:
    bool: Returns True if a path exists from the source to target node. Returns False if no
          such path exists.
    """
    visited = [False] * len(graph)
    visited[s] = True
    queue = [s]

    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    # If we reached sink in BFS starting from source, then return
    # True, else False
    return visited[t]


def mincut(graph: List[List[int]], source: int, sink: int) -> List[Tuple[int, int]]:
    """
    Calculate the minimum cut on a graph based on Ford-Fulkerson algorithm.
    """
    parent = [-1] * (len(graph))
    temp_graph = [i[:] for i in graph]  # Record original cut, copy.

    while bfs(graph, source, sink, parent):
        path_flow = get_path_flow(graph, parent, source, sink)
        update_flow_and_parent(graph, parent, source, sink, path_flow)

    return get_min_cut(graph, temp_graph)


if __name__ == "__main__":
    print(mincut(test_graph, source=0, sink=5))

def get_path_flow(
    graph: List[List[int]], parent: List[int], source: int, sink: int
) -> int:
    """Calculate the path flow from the source to sink in the graph"""
    path_flow = float("Inf")
    s = sink

    while s != source:
        path_flow = min(path_flow, graph[parent[s]][s])
        s = parent[s]

    return path_flow


def update_flow_and_parent(
    graph: List[List[int]], parent: List[int], source: int, sink: int, path_flow: int
):
    """Update the graph flow and parent based on the path flow from source"""
    v = sink

    while v != source:
        u = parent[v]
        graph[u][v] -= path_flow
        graph[v][u] += path_flow
        v = parent[v]


def get_min_cut(
    graph: List[List[int]], temp_graph: List[List[int]]
) -> List[Tuple[int, int]]:
    """Get the minimum cut in the graph"""
    min_cut = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0 and temp_graph[i][j] > 0:
                min_cut.append((i, j))
    return min_cut
