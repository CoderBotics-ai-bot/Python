from __future__ import annotations


def print_distance(distance: list[float], src):
    print(f"Vertex\tShortest Distance from vertex {src}")
    for i, d in enumerate(distance):
        print(f"{i}\t\t{d}")

def check_negative_cycle(
    graph: list[dict[str, int]], distance: list[float], edge_count: int
) -> bool:
    """Check existence of negative weight cycle in the graph.

    This function takes a graph (represented as a list of dictionaries, with each dictionary having a source vertex,
    destination vertex and weight), a list of distances representing the minimum distance from the source to each vertex,
    (initialized with infinity except the source which is zero), and an integer representing the number of edges in the graph,
    all as input.

    It iterates over all the edges and for each edge it checks if the distance to the destination vertex
    can be shortened by going through the source.
    It returns True if it can, implying that a negative weight cycle exists and False otherwise.

    Args:
        graph (list[dict[str, int]]): A list of dictionaries, each representing an edge in the form
                                      {"src": source_vertex, "dst": destination_vertex, "weight": edge_weight}.
        distance (list[float]): A list representing the minimum distance from the source to each vertex.
        edge_count (int): An integer representing the number of edges in the graph.

    Returns:
        bool: True if there exists a negative weight cycle in the graph, False otherwise.

    """
    for edge in graph[:edge_count]:
        u, v, w = edge["src"], edge["dst"], edge["weight"]
        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            return True
    return False


def bellman_ford(
    graph: list[dict[str, int]], vertex_count: int, edge_count: int, src: int
) -> list[float]:
    """
    Returns shortest paths from a vertex src to all
    other vertices.
    >>> edges = [(2, 1, -10), (3, 2, 3), (0, 3, 5), (0, 1, 4)]
    >>> g = [{"src": s, "dst": d, "weight": w} for s, d, w in edges]
    >>> bellman_ford(g, 4, 4, 0)
    [0.0, -2.0, 8.0, 5.0]
    >>> g = [{"src": s, "dst": d, "weight": w} for s, d, w in edges + [(1, 3, 5)]]
    >>> bellman_ford(g, 4, 5, 0)
    Traceback (most recent call last):
     ...
    Exception: Negative cycle found
    """
    distance = [float("inf")] * vertex_count
    distance[src] = 0.0

    for _ in range(vertex_count - 1):
        for j in range(edge_count):
            u, v, w = (graph[j][k] for k in ["src", "dst", "weight"])

            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    negative_cycle_exists = check_negative_cycle(graph, distance, edge_count)
    if negative_cycle_exists:
        raise Exception("Negative cycle found")

    return distance


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    V = int(input("Enter number of vertices: ").strip())
    E = int(input("Enter number of edges: ").strip())

    graph: list[dict[str, int]] = [{} for _ in range(E)]

    for i in range(E):
        print("Edge ", i + 1)
        src, dest, weight = (
            int(x)
            for x in input("Enter source, destination, weight: ").strip().split(" ")
        )
        graph[i] = {"src": src, "dst": dest, "weight": weight}

    source = int(input("\nEnter shortest path source:").strip())
    shortest_distance = bellman_ford(graph, V, E, source)
    print_distance(shortest_distance, 0)
