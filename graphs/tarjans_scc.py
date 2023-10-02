from collections import deque


from typing import List


def create_graph(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    return g


if __name__ == "__main__":
    # Test
    n_vertices = 7
    source = [0, 0, 1, 2, 3, 3, 4, 4, 6]
    target = [1, 3, 2, 0, 1, 4, 5, 6, 5]
    edges = [(u, v) for u, v in zip(source, target)]
    g = create_graph(n_vertices, edges)

    assert [[5], [6], [4], [3, 2, 1, 0]] == tarjan(g)

def tarjan(adjacency_list: List[List[int]]) -> List[List[int]]:
    """
    This function using Tarjan's algorithm computes the strongly connected components in a graph.
    The graph is represented as an adjacency list.
    The return value is a list of the strongly connected components. Each component is also a list that contains the nodes of that component.
    """

    n = len(adjacency_list)
    g = adjacency_list

    stack = deque()
    on_stack = [False for _ in range(n)]
    index_of = [-1 for _ in range(n)]
    lowlink_of = index_of[:]

    def strong_connect(v: int, index: int, components: List[List[int]]) -> int:
        index_of[v] = lowlink_of[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in g[v]:
            if index_of[w] == -1:
                index = strong_connect(w, index, components)
            elif on_stack[w]:
                lowlink_of[v] = min(lowlink_of[w], lowlink_of[v])

        if lowlink_of[v] == index_of[v]:
            components.append(extract_component(v, stack, on_stack))

        return index

    components = []
    for v in range(n):
        if index_of[v] == -1:
            strong_connect(v, 0, components)

    return components


def extract_component(v: int, stack: deque, on_stack: List[bool]) -> List[int]:
    """
    Helper function used to extract strongly connected components from the stack.
    """
    component = []
    while True:
        w = stack.pop()
        on_stack[w] = False
        component.append(w)
        if w == v:
            break
    return component
