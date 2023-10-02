# Check whether Graph is Bipartite or Not using BFS


# A Bipartite Graph is a graph whose vertices can be divided into two independent sets,
# U and V such that every edge (u, v) either connects a vertex from U to V or a vertex
# from V to U. In other words, for every edge (u, v), either u belongs to U and v to V,
# or u belongs to V and v to U. We can also say that there is no edge that connects
# vertices of same set.
from queue import Queue


from typing import List
from queue import Queue


def check_bipartite(graph: List[List[int]]) -> bool:
    queue = Queue()
    visited = [False] * len(graph)
    color = [-1] * len(graph)

    for i in range(len(graph)):
        if not visited[i]:
            queue.put(i)
            color[i] = 0
            if bfs(graph, queue, visited, color) is False:
                return False

    return True


if __name__ == "__main__":
    # Adjacency List of graph
    print(check_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}))

def bfs(
    graph: List[List[int]], queue: Queue, visited: List[bool], color: List[int]
) -> bool:
    while not queue.empty():
        u = queue.get()
        visited[u] = True

        for neighbour in graph[u]:
            if is_self_loop(u, neighbour) or is_same_color(u, neighbour, color):
                return False

            if not visited[neighbour]:
                set_color_for_neighbour(u, neighbour, color)
                queue.put(neighbour)

    return True


def is_self_loop(u: int, neighbour: int) -> bool:
    return neighbour == u


def is_same_color(u: int, neighbour: int, color: List[int]) -> bool:
    return color[neighbour] == color[u]


def set_color_for_neighbour(u: int, neighbour: int, color: List[int]):
    color[neighbour] = 1 - color[u]
