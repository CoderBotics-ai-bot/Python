from typing import Dict, List


from typing import Dict, List



def check_bipartite_dfs(graph: Dict[int, List[int]]) -> bool:
    """Check if a graph is bipartite using DFS"""
    visited = [False] * len(graph)
    color = [-1] * len(graph)

    def dfs(v, c):
        visited[v] = True
        color[v] = c
        for u in graph[v]:
            if not visited[u]:
                dfs(u, 1 - c)

    def visit_all_nodes():
        for i in range(len(graph)):
            if not visited[i]:
                dfs(i, 0)

    def verify_edge_colors():
        for i in range(len(graph)):
            for j in graph[i]:
                if color[i] == color[j]:
                    return False
        return True

    visit_all_nodes()
    return verify_edge_colors()


# Adjacency list of graph
graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: []}
print(check_bipartite_dfs(graph))
