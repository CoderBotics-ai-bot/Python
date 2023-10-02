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


def bfs_shortest_path_distance(graph: dict, start, target) -> int:
    """Find shortest path distance between `start` and `target` nodes.
    Args:
        graph: node/list of neighboring nodes key/value pairs.
        start: node to start search from.
        target: node to search for.
    Returns:
        Number of edges in shortest path between `start` and `target` nodes.
        -1 if no path exists.
    Example:
        >>> bfs_shortest_path_distance(demo_graph, "G", "D")
        4
        >>> bfs_shortest_path_distance(demo_graph, "A", "A")
        0
        >>> bfs_shortest_path_distance(demo_graph, "A", "Unknown")
        -1
    """
    if not graph or start not in graph or target not in graph:
        return -1
    if start == target:
        return 0
    queue = [start]
    visited = set(start)
    # Keep tab on distances from `start` node.
    dist = {start: 0, target: -1}
    while queue:
        node = queue.pop(0)
        if node == target:
            dist[target] = (
                dist[node] if dist[target] == -1 else min(dist[target], dist[node])
            )
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
                dist[adjacent] = dist[node] + 1
    return dist[target]


if __name__ == "__main__":
    print(bfs_shortest_path(demo_graph, "G", "D"))  # returns ['G', 'C', 'A', 'B', 'D']
    print(bfs_shortest_path_distance(demo_graph, "G", "D"))  # returns 4
