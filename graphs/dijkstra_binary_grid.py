"""
This script implements the Dijkstra algorithm on a binary grid.
The grid consists of 0s and 1s, where 1 represents
a walkable node and 0 represents an obstacle.
The algorithm finds the shortest path from a start node to a destination node.
Diagonal movement can be allowed or disallowed.
"""

from heapq import heappop, heappush

import numpy as np


from typing import List, Tuple, Optional, Union


def dijkstra(
    grid: np.ndarray,
    start: Tuple[int, int],
    destination: Optional[Tuple[int, int]] = None,
    diagonal_movement: bool = False,
) -> Union[np.ndarray, Tuple[np.ndarray, List[Tuple[int, int]]]]:
    """
    A method that takes a binary grid and finds the shortest path from start to destination.
    If the destination is unreachable or not given, returns a grid of distances to each point from the start.
    :param grid: a 2D numpy array of 0's and 1's, where 0's are walkable areas and 1's are obstacles
    :param start: a point in the grid where the path will start from
    :param destination: a target point, if exists one
    :param diagonal_movement: If diagonal_movement is set to True, 8 directions movement is allowed. Otherwise only 4 directions movement is allowed.
    :return: a 2D numpy array of the same shape as grid with distances, if destination is not reachable or not provided or a tuple of a 2D numpy array of the same shape as grid with distances and the shortest path list if destination is reachable.
    """
    distances, visited, queue = initialize_dijkstra(grid, start)

    while queue:
        _, current = heappop(queue)
        if visited[current]:
            continue
        visited[current] = True

        for i, j in generate_valid_neighors(*current, diagonal_movement, grid):
            alt_distance = distances[current] + np.hypot(i - current[0], j - current[1])
            if alt_distance < distances[i, j]:
                distances[i, j] = alt_distance
                heappush(queue, (alt_distance, (i, j)))

        if current == destination and grid[current]:
            break

    if destination is not None and grid[destination]:
        shortest_path = get_path(distances, start, destination, grid)
        return distances, shortest_path
    else:
        return distances


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def generate_valid_neighors(
    i: int, j: int, diagonal_movement: bool, grid: np.ndarray
) -> List[Tuple[int, int]]:
    """
    Generate valid neighbors based on the current position, movement rule and grid status.
    """
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    if diagonal_movement:
        directions += [(1, -1), (-1, 1), (1, 1), (-1, -1)]

    neighbors = [(i + di, j + dj) for di, dj in directions]
    neighbors = [
        (i, j)
        for i, j in neighbors
        if 0 <= i < grid.shape[0] and 0 <= j < grid.shape[1]
    ]

    return [(i, j) for i, j in neighbors if grid[i][j] == 1]


def initialize_dijkstra(
    grid: np.ndarray, start: Tuple[int, int]
) -> Tuple[np.ndarray, np.ndarray, List[Tuple[int, int]]]:
    """
    Initialize Dijkstra variables: distances, visited nodes and queue.
    """
    distances = np.full(grid.shape, np.inf)
    distances[start] = 0
    visited = np.zeros((grid.shape), dtype=bool)
    queue = [(0, start)]

    return distances, visited, queue
