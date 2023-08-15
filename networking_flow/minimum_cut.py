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

def bfs(graph: List[List[int]], s: int, t: int, parent: List[int]) -> bool:
    """
    Perform Breadth-First-Search (BFS) on the graph.

    Args:
        graph (List[List[int]]): The adjacency matrix representation of the graph.
        s (int): The source vertex.
        t (int): The target vertex.
        parent (List[int]): List to save the parent of a given node.

    Returns:
        bool: True if there is a path from source to target. False otherwise.
    """

    # Return True if there is node that has not iterated.
    visited = [False] * len(graph)
    queue = [s]
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for ind in range(len(graph[u])):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[t]


def mincut(graph, source, sink):
    """This array is filled by BFS and to store path
    >>> mincut(test_graph, source=0, sink=5)
    [(1, 3), (4, 3), (4, 5)]
    """
    parent = [-1] * (len(graph))
    max_flow = 0
    res = []
    temp = [i[:] for i in graph]  # Record original cut, copy.
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

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0 and temp[i][j] > 0:
                res.append((i, j))

    return res


if __name__ == "__main__":
    print(mincut(test_graph, source=0, sink=5))
