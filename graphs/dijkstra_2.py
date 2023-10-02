

from typing import List
def print_dist(dist, v):
    print("\nVertex Distance")
    for i in range(v):
        if dist[i] != float("inf"):
            print(i, "\t", int(dist[i]), end="\t")
        else:
            print(i, "\t", "INF", end="\t")
        print()


def dijkstra(graph, v, src):
    mdist = [float("inf") for _ in range(v)]
    vset = [False for _ in range(v)]
    mdist[src] = 0.0

    for _ in range(v - 1):
        u = min_dist(mdist, vset, v)
        vset[u] = True

        for i in range(v):
            if (
                (not vset[i])
                and graph[u][i] != float("inf")
                and mdist[u] + graph[u][i] < mdist[i]
            ):
                mdist[i] = mdist[u] + graph[u][i]

    print_dist(mdist, i)

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
