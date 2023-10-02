# floyd_warshall.py
"""
    The problem is to find the shortest distance between all pairs of vertices in a
    weighted directed graph that can have negative edge weights.
"""


from typing import List


from typing import List, Tuple

def _print_dist(dist: List[List[float]], v: int) -> None:
    """
    Print the matrix of shortest path distances.

    This function uses Floyd Warshall algorithm and prints the matrix of shortest paths between all pairs of vertices.
    The matrix is printed in a human readable format: each row corresponds to a vertex, each column
    to a destination vertex, and each cell contains the shortest path distance from the corresponding vertex
    to the destination vertex. If a certain path is not reachable, "INF" is printed in the corresponding cell.

    Arguments:
    dist -- 2D list representing the distances between each pair of vertices
    v -- Number of vertices in the graph

    Returns:
    None
    """
    print("\nThe shortest path matrix using Floyd Warshall algorithm\n")

    def format_value(value: float) -> str:
        """Format the value to display"""
        return str(int(value)) if value != float("inf") else "INF"

    rows = ["\t".join(format_value(dist[i][j]) for j in range(v)) for i in range(v)]
    print("\n".join(rows))

def floyd_warshall(graph: List[List[float]], v: int) -> Tuple[List[List[float]], int]:
    """
    Implement the Floyd Warshall algorithm to find the shortest paths between all pairs of vertices in a given graph.

    This function takes a graph represented by a 2D matrix and the number of vertices in the graph. It calculates the
    shortest path between all pairs of vertices and returns a 2D matrix of shortest path distances and the number of vertices.

    The Floyd Warshall algorithm is a dynamic programming algorithm that solves the all-pairs shortest path problem.
    The algorithm compares all possible paths through the graph between each pair of vertices and keeps the shortest one.

    Arguments:
    graph -- 2D list representing the graph where each cell [i, j] represents the weight of the edge between vertices i and j.
    v -- Number of vertices in the graph.

    Returns:
    dist -- 2D list representing the shortest path distances between each pair of vertices.
    v -- Number of vertices in the graph.
    """

    # initialize the distance matrix
    dist = initialize_dist(graph, v)

    # calculate shortest path
    dist = calculate_shortest_path(dist, v)

    # print the shortest path
    _print_dist(dist, v)

    return dist, v


if __name__ == "__main__":
    v = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    graph = [[float("inf") for i in range(v)] for j in range(v)]

    for i in range(v):
        graph[i][i] = 0.0

        # src and dst are indices that must be within the array size graph[e][v]
        # failure to follow this will result in an error
    for i in range(e):
        print("\nEdge ", i + 1)
        src = int(input("Enter source:"))
        dst = int(input("Enter destination:"))
        weight = float(input("Enter weight:"))
        graph[src][dst] = weight

    floyd_warshall(graph, v)

    # Example Input
    # Enter number of vertices: 3
    # Enter number of edges: 2

    # # generated graph from vertex and edge inputs
    # [[inf, inf, inf], [inf, inf, inf], [inf, inf, inf]]
    # [[0.0, inf, inf], [inf, 0.0, inf], [inf, inf, 0.0]]

    # specify source, destination and weight for edge #1
    # Edge  1
    # Enter source:1
    # Enter destination:2
    # Enter weight:2

    # specify source, destination and weight for edge #2
    # Edge  2
    # Enter source:2
    # Enter destination:1
    # Enter weight:1

    # # Expected Output from the vertice, edge and src, dst, weight inputs!!
    # 0		INF	INF
    # INF	0	2
    # INF	1	0


def initialize_dist(graph: List[List[float]], v: int) -> List[List[float]]:
    """Initialize the distance matrix with edges' weights or infinity if no edge"""
    dist = [[float("inf") for _ in range(v)] for _ in range(v)]

    for i in range(v):
        for j in range(v):
            dist[i][j] = graph[i][j]

    return dist


def calculate_shortest_path(dist: List[List[float]], v: int) -> List[List[float]]:
    """Calculate the shortest path for all pairs of vertices using Floyd Warshall algorithm"""
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if (
                    dist[i][k] != float("inf")
                    and dist[k][j] != float("inf")
                    and dist[i][k] + dist[k][j] < dist[i][j]
                ):
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
