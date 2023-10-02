from typing import List
def print_dist(dist, v):
    print("\nVertex Distance")
    for i in range(v):
        if dist[i] != float("inf"):
            print(i, "\t", int(dist[i]), end="\t")
        else:
            print(i, "\t", "INF", end="\t")
        print()

## REFACTORED CODE:


def min_dist(mdist: List[float], vset: List[bool], v: int) -> int:
    """
    In a graph, calculate the minimum distance from a vertex to an unvisited vertex.

    Arguments:
    mdist -- list of distances from source vertex to respective vertex
    vset -- set of visited vertices in the graph while traversing
    v -- total number of vertices in the graph

    Returns:
    min_ind -- index of unvisited vertex with minimum distance from source vertex. If there is no such vertex, or all distances are infinity, return -1.

    This function is a helper for the Dijkstra algorithm. It traverse the vertices of a graph and finds
    the unvisited vertex with the smallest distance from the source vertex.
    """
    unvisited = [(dist, i) for i, dist in enumerate(mdist) if not vset[i]]

    # Return early if all distances in unvisited vertices are infinity
    if all(dist == float("inf") for dist, _ in unvisited):  # this line was missing
        return -1

    return min(unvisited)[1]



def dijkstra(graph: List[List[float]], v: int, src: int) -> None:
    """
    Perform Dijkstra's algorithm on the graph to find the shortest path from the source vertex to all other vertices.

    Arguments:
    graph -- An adjacency matrix representing the graph where graph[i][j] is the weight of the edge between vertices i and j.
    v -- Total number of vertices in the graph.
    src -- The source vertex from which shortest distances to other vertices are to be calculated.
    """
    mdist = initialize_distances(v, src)
    vset = [False] * v

    for _ in range(v - 1):
        min_vertex = get_min_distance_vertex(mdist, vset)
        vset[min_vertex] = True
        update_vertex_distances(graph, v, mdist, vset, min_vertex)

    print_dist(mdist, v)


if __name__ == "__main__":
    V = int(input("Enter number of vertices: ").strip())
    E = int(input("Enter number of edges: ").strip())

    graph = [[float("inf") for i in range(V)] for j in range(V)]

    for i in range(V):
        graph[i][i] = 0.0

    for i in range(E):
        print("\nEdge ", i + 1)
        src = int(input("Enter source:").strip())
        dst = int(input("Enter destination:").strip())
        weight = float(input("Enter weight:").strip())
        graph[src][dst] = weight

    gsrc = int(input("\nEnter shortest path source:").strip())
    dijkstra(graph, V, gsrc)


def initialize_distances(v: int, src: int) -> List[float]:
    """
    Initialize the distances array.

    Arguments:
    v -- Total number of vertices in the graph.
    src -- The source vertex from which shortest distances to other vertices are to be calculated.

    Returns:
    mdist -- The initialized distances array.
    """
    mdist = [float("inf")] * v
    mdist[src] = 0.0
    return mdist


def get_min_distance_vertex(mdist: List[float], vset: List[bool]) -> int:
    """
    Get the vertex with the minimum distance from the source.

    Arguments:
    mdist -- The shortest distances from the source to each vertex.
    vset -- The set of visited vertices.

    Returns:
    min_vertex -- The vertex with the minimum distance from the source.
    """
    return min((l, i) for i, l in enumerate(mdist) if not vset[i])[1]


def update_vertex_distances(
    graph: List[List[float]], v: int, mdist: List[float], vset: List[bool], u: int
) -> None:
    """
    Update the distances to all neighboring vertices of the given vertex.

    Arguments:
    graph -- An adjacency matrix representing the graph where graph[i][j] is the weight of the edge between vertices i and j.
    v -- Total number of vertices in the graph.
    mdist -- The shortest distances from the source to each vertex.
    vset -- The set of visited vertices.
    u -- The given vertex.
    """
    for i in range(v):
        if (
            (not vset[i])
            and graph[u][i] != float("inf")
            and mdist[u] + graph[u][i] < mdist[i]
        ):
            mdist[i] = mdist[u] + graph[u][i]
