from typing import List, Optional
from typing import Dict, List, Optional


from typing import Dict, List, Optional


def dfs(
    u: int, graph: Dict, visited_edge: Dict, path: Optional[List[int]] = None
) -> List[int]:
    """
    Determine the Eulerian path of a graph using the depth-first search (DFS) algorithm.

    Args:
        u (int): The current vertex.
        graph (dict): The input graph.
        visited_edge (dict): The dictionary representing the edges of the graph and their visited status.
        path (list, optional): The path traversed so far. If None, the path contains only the starting vertex. Defaults to None.

    Returns:
        path (list): The Eulerian path found by the DFS algorithm.
    """

    path = (path or []) + [u]
    for v in graph[u]:
        if not visited_edge[u][v]:
            visited_edge = update_visited_edges(visited_edge, u, v)
            path = dfs(v, graph, visited_edge, path)
    return path


# for checking in graph has euler path or circuit
def check_circuit_or_path(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node):
        if i not in graph:
            continue
        if len(graph[i]) % 2 == 1:
            odd_degree_nodes += 1
            odd_node = i
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    return 3, odd_node



def update_visited_edges(visited_edge: Dict, u: int, v: int) -> Dict:
    """
    Update the visited_edge dictionary by marking the edge from `u` to `v` as visited.

    Args:
        visited_edge (dict): The dictionary representing the edges of the graph and their visited status.
        u (int): The current vertex.
        v (int): The next vertex to visit.

    Returns:
        visited_edge (dict): The updated visited_edge dictionary with the edge from `u` to `v` marked as visited.
    """

    visited_edge[u][v], visited_edge[v][u] = True, True
    return visited_edge


def check_euler(graph, max_node):
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
    check, odd_node = check_circuit_or_path(graph, max_node)
    if check == 3:
        print("graph is not Eulerian")
        print("no path")
        return
    start_node = 1
    if check == 2:
        start_node = odd_node
        print("graph has a Euler path")
    if check == 1:
        print("graph has a Euler cycle")
    path = dfs(start_node, graph, visited_edge)
    print(path)


def main():
    g1 = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]}
    g2 = {1: [2, 3, 4, 5], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [1, 4]}
    g3 = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2], 4: [1, 2, 5], 5: [4]}
    g4 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    g5 = {
        1: [],
        2: []
        # all degree is zero
    }
    max_node = 10
    check_euler(g1, max_node)
    check_euler(g2, max_node)
    check_euler(g3, max_node)
    check_euler(g4, max_node)
    check_euler(g5, max_node)


if __name__ == "__main__":
    main()
