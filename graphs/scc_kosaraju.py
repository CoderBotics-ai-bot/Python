from __future__ import annotations
from typing import List


def dfs(u):
    global graph, reversed_graph, scc, component, visit, stack
    if visit[u]:
        return
    visit[u] = True
    for v in graph[u]:
        dfs(v)
    stack.append(u)


def dfs2(u):
    global graph, reversed_graph, scc, component, visit, stack
    if visit[u]:
        return
    visit[u] = True
    component.append(u)
    for v in reversed_graph[u]:
        dfs2(v)


def kosaraju() -> List[List[int]]:
    """
    Implements Kosaraju's algorithm to find strongly connected components in the given graph.

    Global variables:
    - graph: Adjacency list representation of the graph
    - reversed_graph: Reversed graph of the original graph
    - scc: List to store all strongly connected components
    - component: List to store the current strongly connected component
    - visit: Boolean list to keep track of visited nodes
    - stack: Stack to store visited nodes in DFS
    - n: Number of nodes in the graph

    Returns:
        List of strongly connected components. Each component is represented as a list of nodes.
    """
    global graph, reversed_graph, n
    initiate_global_variables(n)

    return perform_kosaraju_algorithm(n)


if __name__ == "__main__":
    # n - no of nodes, m - no of edges
    n, m = list(map(int, input().strip().split()))

    graph: list[list[int]] = [[] for _ in range(n)]  # graph
    reversed_graph: list[list[int]] = [[] for i in range(n)]  # reversed graph
    # input graph data (edges)
    for _ in range(m):
        u, v = list(map(int, input().strip().split()))
        graph[u].append(v)
        reversed_graph[v].append(u)

    stack: list[int] = []
    visit: list[bool] = [False] * n
    scc: list[int] = []
    component: list[int] = []
    print(kosaraju())

def initiate_global_variables(n: int) -> None:
    """
    Initialize the given global variables before implementing the Kosaraju's
    algorithm.

    Args:
        n: Number of nodes in the graph
    """
    global component, visit, stack, scc

    visit = [False] * n
    stack = []
    scc = []
    component = []


def perform_kosaraju_algorithm(n: int) -> List[List[int]]:
    """
    Perform the Kosaraju's algorithm and return the result.

    Args:
        n: Number of nodes in the graph

    Returns:
        List of strongly connected components. Each component is represented
        as a list of nodes.
    """
    for i in range(n):
        if not visit[i]:
            dfs(i)

    visit = [False] * n

    for node in reversed(stack):
        if not visit[node]:
            component = []
            dfs2(node)
            scc.append(component)

    return scc
