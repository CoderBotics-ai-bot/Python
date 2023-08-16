

from typing import Dict, List, Tuple
# Eulerian Path is a path in graph that visits every edge exactly once.
# Eulerian Circuit is an Eulerian Path which starts and ends on the same
# vertex.
# time complexity is O(V+E)
# space complexity is O(VE)


# using dfs for finding eulerian path traversal
def dfs(u, graph, visited_edge, path=None):
    path = (path or []) + [u]
    for v in graph[u]:
        if visited_edge[u][v] is False:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    return path

def check_circuit_or_path(
    graph: Dict[int, List[int]], max_node: int
) -> Tuple[int, int]:
    """
    Check if a given graph has an Eulerian circuit or path.

    This function checks the graph for the presence of an Eulerian circuit or path
    based on the degrees (number of edges) of each node.
    An Eulerian circuit exists if all nodes have an even degree.
    An Eulerian path exists if exactly 2 nodes have an odd degree, while the others
    have an even degree.

    Arguments:
    graph -- a dictionary representing the graph, where keys are node numbers,
             and values are lists of nodes that are directly connected to the key node.
    max_node -- the maximum node number in the graph.

    Returns a tuple:
    - The first element is an integer that represents the presence of an Eulerian circuit
      or path:
         1 -- Eulerian circuit
         2 -- Eulerian path
         3 -- neither Eulerian circuit nor path.
    - The second element is the number of a node with an odd degree (-1 if none exists).
    """
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
