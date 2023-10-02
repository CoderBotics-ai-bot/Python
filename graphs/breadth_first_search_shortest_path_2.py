"""Breadth-first search shortest path implementations.
    doctest:
    python -m doctest -v bfs_shortest_path.py
    Manual test:
    python bfs_shortest_path.py
"""
demo_graph = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["A", "B", "D"],
    "F": ["C"],
    "G": ["C"],
}

def bfs_shortest_path(graph: dict, start: str, goal: str) -> list[str]:
    """
    Find the shortest path between given start and goal nodes in the graph using Breadth-First Search (BFS).

    Function accepts a dictionary, where each key/value pair represents a node and a list of its neighbouring
    nodes. Returns the shortest path as a list of node strings if there exists a path between start and goal.
    If no path is found, it returns an empty list.

    Args:
        graph (dict): Representation of graph where each key is a node and each value is a list of neighbouring nodes
        start (str): The starting node in the graph
        goal (str): The target node in the graph

    Returns:
        list[str]: The shortest path from start to goal as a list of node strings.
                   If no path exists, an empty list is returned.

    Raises:
        KeyError: If graph is an empty dictionary.

    Examples:
        >>> bfs_shortest_path(demo_graph, "G", "D")
        ['G', 'C', 'A', 'B', 'D']

        >>> bfs_shortest_path(demo_graph, "G", "G")
        ['G']

        >>> bfs_shortest_path(demo_graph, "G", "Unknown")
        []

    """
    if start == goal:
        return [start]

    explored = set()
    queue = [[start]]

    for path in queue:
        node = path[-1]
        if node not in explored:
            explored.add(node)
            for neighbour in graph[node]:
                new_path = path + [neighbour]
                if neighbour == goal:
                    return new_path
                queue.append(new_path)

    return []

def bfs_shortest_path_distance(graph: dict, start: str, target: str) -> int:
    """
    Find and return the shortest path distance between the `start` and `target` nodes using
    Breadth-First Search algorithm.

    The function works by checking if the `start` and `target` nodes exist in the `graph`,
    and if they are the same. If so, it returns prepared values. Else,
    it returns the shortest path distance or -1, if there is no path between nodes.

    Args:
        graph (dict): A dictionary representing the graph where keys are nodes and values
                      are lists of neighbors.
        start (str): The beginning node.
        target (str): The node we are looking for.

    Returns:
        int: An integer representing the shortest distance (the lowest number of edges) or -1,
             if there is no path between nodes.

    Examples:
        >>> bfs_shortest_path_distance(demo_graph, "G", "D")
        4
        >>> bfs_shortest_path_distance(demo_graph, "A", "A")
        0
        >>> bfs_shortest_path_distance(demo_graph, "A", "H")
        -1
    """
    if start == target:
        return 0
    if not graph or start not in graph or target not in graph:
        return -1

    visited, dist, queue = {start}, {start: 0, target: -1}, [start]

    while queue:
        node = queue.pop(0)
        if node == target:
            return dist[node]
        update_queue_and_dist(graph, visited, dist, queue, node)

    return -1


if __name__ == "__main__":
    print(bfs_shortest_path(demo_graph, "G", "D"))  # returns ['G', 'C', 'A', 'B', 'D']
    print(bfs_shortest_path_distance(demo_graph, "G", "D"))  # returns 4


def update_queue_and_dist(graph, visited, dist, queue, node):
    """Update visited nodes, distances and add non-visited nodes into queue."""
    for adjacent in graph[node]:
        if adjacent not in visited:
            visited.add(adjacent)
            queue.append(adjacent)
            dist[adjacent] = dist[node] + 1
