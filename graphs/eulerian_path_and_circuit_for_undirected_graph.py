from typing import List, Optional
from typing import Dict, List, Optional


from typing import Dict, List, Optional


from typing import Dict, List, Tuple


from typing import List, Dict

def check_euler(graph: Dict[int, List[int]], max_node: int) -> None:
    """
    Check if a given graph is Eulerian or semi-Eulerian. Eulerian means all nodes have even degrees while
    Semi-Eulerian means only 2 nodes have odd degrees with others having even degrees.
    If neither the graph has neither a Euler path nor a Euler circuit.

    Args:
        Graph (Dict[int, List[int]]) : The graph represented by adjacency list.
        max_node (int) : maximum node identifier in the graph.

    The function does not return a value, Instead, it either prints "graph is not Eulerian no path"
    if the graph is not Eulerian, "graph has a Euler path" if the graph has a Euler path or
    "graph has a Euler cycle, if the graph has a Euler circuit.
    It also prints the Euler path or circuit if it exists.

    Side effects: Modifies the graph by marking nodes as visited and also prints to the standard output.

    Exceptions raised: This function does not raise any exceptions.

    """

    # Create a list to mark visited edges
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]

    check, odd_node = check_circuit_or_path(graph, max_node)

    # Handle case when graph is not Eulerian
    if check == 3:
        print("graph is not Eulerian")
        print("no path")
        return

    start_node = find_start_node(
        check, odd_node
    )  # Extracted functionality to find start node to its own function

    euler_type_print(
        check
    )  # Extracted functionality to print Euler type to its own function

    path = dfs(start_node, graph, visited_edge)

    print(path)

def check_circuit_or_path(
    graph: Dict[int, List[int]], max_node: int
) -> Tuple[int, int]:
    """
    Check if a given graph has an Euler path or circuit...

    .. detailed docstring truncated for brevity
    """
    odd_degree_nodes, odd_node = count_odd_degree_nodes(graph, max_node)

    if odd_degree_nodes == 0:
        return 1, odd_node
    elif odd_degree_nodes == 2:
        return 2, odd_node
    else:
        return 3, odd_node


def find_start_node(check: int, odd_node: int) -> int:
    """
    Determine the starting node for depth first search. This depends on whether graph is
    Eulerian (start from any node) or semi-Eulerian (start from one of the odd degree nodes)

    Args:
        check (int) : check value from check_circuit_or_path which indicates if graph is
                      Eulerian, semi-Eulerian or not Eulerian at all.
        odd_node (int) : The node with odd degree in case of semi-Eulerian graph.

    Returns:
        start_node (int) : node to start depth first search from.
    """
    return odd_node if check == 2 else 1


def euler_type_print(check: int) -> None:
    """
    Print type of Euler graph (Eulerian, semi-Eulerian or not Eulerian at all) based on check value.

    Args:
        check (int) : check value from check_circuit_or_path which indicates if graph is
                      Eulerian, semi-Eulerian or not Eulerian at all.

    Side Effects:
        Prints to the standard output.
    """

    if check == 2:
        print("graph has a Euler path")
    elif check == 1:
        print("graph has a Euler cycle")


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


def count_odd_degree_nodes(
    graph: Dict[int, List[int]], max_node: int
) -> Tuple[int, int]:
    """
    Count the number of nodes with odd degree in a graph.

    Args:
        graph: A dictionary representing the graph.
        max_node: An integer representing the maximum node number in the graph.

    Returns:
        A tuple where the first element is the count of nodes with odd degree and
        the second element is the node with odd degree (-1 if no such node exists).
    """
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node):
        if i not in graph:
            continue
        if len(graph[i]) % 2 == 1:
            odd_degree_nodes += 1
            odd_node = i

    return odd_degree_nodes, odd_node



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
