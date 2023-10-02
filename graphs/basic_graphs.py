from collections import deque


from typing import List, Dict


from typing import Dict, List


def _input(message):
    return input(message).strip().split(" ")

def initialize_unweighted_undirected_graph(
    node_count: int, edge_count: int
) -> Dict[int, List[int]]:
    """Initialize an unweighted undirected graph.

    This function allows the user to define the nodes and edges of an unweighted undirected graph.
    The user will be prompted to input the two nodes that constitute an edge.
    Node numbers should start at 1 and increment by 1.

    Args:
        node_count (int): The number of nodes in the graph.
        edge_count (int): The number of edges in the graph.

    Returns:
        Dict[int, List[int]]: A dictionary representing the graph. The dictionary's keys are the nodes,
            while the dictionary's values are lists of nodes that the key node is connected to by an edge.

    Raises:
        ValueError: If node values entered for the edges don't exist in the initialized nodes.
    """
    graph = create_graph_nodes(node_count)
    add_graph_edges(graph, edge_count)
    return graph


def initialize_weighted_undirected_graph(
    node_count: int, edge_count: int
) -> dict[int, list[tuple[int, int]]]:
    graph: dict[int, list[tuple[int, int]]] = {}
    for i in range(node_count):
        graph[i + 1] = []

    for e in range(edge_count):
        x, y, w = (int(i) for i in _input(f"Edge {e + 1}: <node1> <node2> <weight> "))
        graph[x].append((y, w))
        graph[y].append((x, w))
    return graph


if __name__ == "__main__":
    n, m = (int(i) for i in _input("Number of nodes and edges: "))

    graph_choice = int(
        _input(
            "Press 1 or 2 or 3 \n"
            "1. Unweighted directed \n"
            "2. Unweighted undirected \n"
            "3. Weighted undirected \n"
        )[0]
    )

    g = {
        1: initialize_unweighted_directed_graph,
        2: initialize_unweighted_undirected_graph,
        3: initialize_weighted_undirected_graph,
    }[graph_choice](n, m)


"""
--------------------------------------------------------------------------------
    Depth First Search.
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  vis - Set of visited nodes
                S - Traversal Stack
--------------------------------------------------------------------------------
"""


def dfs(g, s):
    vis, _s = {s}, [s]
    print(s)
    while _s:
        flag = 0
        for i in g[_s[-1]]:
            if i not in vis:
                _s.append(i)
                vis.add(i)
                flag = 1
                print(i)
                break
        if not flag:
            _s.pop()


"""
--------------------------------------------------------------------------------
    Breadth First Search.
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  vis - Set of visited nodes
                Q - Traversal Stack
--------------------------------------------------------------------------------
"""

def initialize_unweighted_directed_graph(
    node_count: int, edge_count: int
) -> dict[int, list[int]]:
    """
    Initialize an unweighted directed graph using user inputs.

    Arguments:
    node_count -- The total number of nodes in the graph.
    edge_count -- The total number of edges in the graph.

    The function will prompt the user to enter each edge.

    Returns:
    A dictionary representing the graph. The keys of the dictionary are the nodes,
    and the values are lists of nodes that have an edge going from the key.
    """
    graph = create_graph_nodes(node_count)
    add_graph_edges(graph, edge_count)
    return graph


def bfs(g, s):
    vis, q = {s}, deque([s])
    print(s)
    while q:
        u = q.popleft()
        for v in g[u]:
            if v not in vis:
                vis.add(v)
                q.append(v)
                print(v)


def create_graph_nodes(node_count: int) -> dict[int, list[int]]:
    """
    Create a dictionary representing the nodes of a graph.

    Arguments:
    node_count -- The total number of nodes in the graph.

    Returns:
    A dictionary where the keys are the nodes and the values are empty lists.
    """
    return {i: [] for i in range(1, node_count + 1)}


def add_graph_edges(graph: dict[int, list[int]], edge_count: int) -> None:
    """
    Prompt the user to enter the edges of the graph and add them to the graph.

    Arguments:
    graph -- The graph to add edges to.
    edge_count -- The total number of edges in the graph.
    """
    for e in range(edge_count):
        x, y = map(int, input(f"Edge {e + 1}: <node1> <node2> ").split())
        graph[x].append(y)


"""
--------------------------------------------------------------------------------
    Dijkstra's shortest path Algorithm
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  dist - Dictionary storing shortest distance from s to every other node
                known - Set of knows nodes
                path - Preceding node in path
--------------------------------------------------------------------------------
"""


def dijk(g, s):
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(g) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in g[u]:
            if v[0] not in known and dist[u] + v[1] < dist.get(v[0], 100000):
                dist[v[0]] = dist[u] + v[1]
                path[v[0]] = u
    for i in dist:
        if i != s:
            print(dist[i])


"""
--------------------------------------------------------------------------------
    Topological Sort
--------------------------------------------------------------------------------
"""


def topo(g, ind=None, q=None):
    if q is None:
        q = [1]
    if ind is None:
        ind = [0] * (len(g) + 1)  # SInce oth Index is ignored
        for u in g:
            for v in g[u]:
                ind[v] += 1
        q = deque()
        for i in g:
            if ind[i] == 0:
                q.append(i)
    if len(q) == 0:
        return
    v = q.popleft()
    print(v)
    for w in g[v]:
        ind[w] -= 1
        if ind[w] == 0:
            q.append(w)
    topo(g, ind, q)


"""
--------------------------------------------------------------------------------
    Reading an Adjacency matrix
--------------------------------------------------------------------------------
"""


def adjm():
    n = input().strip()
    a = []
    for _ in range(n):
        a.append(map(int, input().strip().split()))
    return a, n


"""
--------------------------------------------------------------------------------
    Floyd Warshall's algorithm
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  dist - Dictionary storing shortest distance from s to every other node
                known - Set of knows nodes
                path - Preceding node in path

--------------------------------------------------------------------------------
"""


def floy(a_and_n):
    (a, n) = a_and_n
    dist = list(a)
    path = [[0] * n for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][k] = k
    print(dist)


"""
--------------------------------------------------------------------------------
    Prim's MST Algorithm
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  dist - Dictionary storing shortest distance from s to nearest node
                known - Set of knows nodes
                path - Preceding node in path
--------------------------------------------------------------------------------
"""


def prim(g, s):
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(g) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in g[u]:
            if v[0] not in known and v[1] < dist.get(v[0], 100000):
                dist[v[0]] = v[1]
                path[v[0]] = u
    return dist


"""
--------------------------------------------------------------------------------
    Accepting Edge list
        Vars :  n - Number of nodes
                m - Number of edges
        Returns : l - Edge list
                n - Number of Nodes
--------------------------------------------------------------------------------
"""


def edglist():
    n, m = map(int, input().split(" "))
    edges = []
    for _ in range(m):
        edges.append(map(int, input().split(" ")))
    return edges, n


"""
--------------------------------------------------------------------------------
    Kruskal's MST Algorithm
        Args :  E - Edge list
                n - Number of Nodes
        Vars :  s - Set of all nodes as unique disjoint sets (initially)
--------------------------------------------------------------------------------
"""


def krusk(e_and_n):
    # Sort edges on the basis of distance
    (e, n) = e_and_n
    e.sort(reverse=True, key=lambda x: x[2])
    s = [{i} for i in range(1, n + 1)]
    while True:
        if len(s) == 1:
            break
        print(s)
        x = e.pop()
        for i in range(len(s)):
            if x[0] in s[i]:
                break
        for j in range(len(s)):
            if x[1] in s[j]:
                if i == j:
                    break
                s[j].update(s[i])
                s.pop(i)
                break


# find the isolated node in the graph
def find_isolated_nodes(graph):
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated.append(node)
    return isolated
