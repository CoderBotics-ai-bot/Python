"""
Given an two dimensional binary matrix grid. An island is a group of 1's (representing
land) connected 4-directionally (horizontal or vertical.) You may assume all four edges
of the grid are surrounded by water.  The area of an island is the number of cells with
a value 1 in the island. Return the maximum area of an island in a grid. If there is no
island, return 0.
"""


from typing import List, Set

matrix = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]


def is_safe(row: int, col: int, rows: int, cols: int) -> bool:
    """
    Checking whether coordinate (row, col) is valid or not.

    >>> is_safe(0, 0, 5, 5)
    True
    >>> is_safe(-1,-1, 5, 5)
    False
    """
    return 0 <= row < rows and 0 <= col < cols

def depth_first_search(row: int, col: int, seen: set, mat: list[list[int]]) -> int:
    """
    Uses Depth-First Search (DFS) algorithm to compute the size of an island in a matrix.
    The island is defined as a group of '1's connected either horizontally or vertically (not diagonally).
    The function begins the search from a specific point (specified by 'row' and 'col' arguments),
    exploring as far as possible along each branch before backtracking.

    Args:
    row (int): Row index from where the DFS should start.
    col (int): Column index from where the DFS should start.
    seen (set): A set storing all the matrix positions ((row, col) tuples) that have been visited.
    mat (list[list[int]]): 2D list of integers representing the matrix (1 represents land, 0 represents water).

    Returns:
    int: The size of the island.

    Examples:
    >>> depth_first_search(0, 0, set(), [[0, 0, 1, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1]])
    1
    >>> depth_first_search(1, 1, set(), [[0, 0, 1, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1]])
    4
    """
    rows = len(mat)
    cols = len(mat[0])

    if not is_safe(row, col, rows, cols) or (row, col) in seen or mat[row][col] != 1:
        return 0

    seen.add((row, col))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return 1 + sum(
        depth_first_search(row + dr, col + dc, seen, mat) for dr, dc in directions
    )


def find_max_area(mat: list[list[int]]) -> int:
    """
    Finds the area of all islands and returns the maximum area.

    >>> find_max_area(matrix)
    6
    """
    seen: set = set()

    max_area = 0
    for row, line in enumerate(mat):
        for col, item in enumerate(line):
            if item == 1 and (row, col) not in seen:
                # Maximizing the area
                max_area = max(max_area, depth_first_search(row, col, seen, mat))
    return max_area


if __name__ == "__main__":
    import doctest

    print(find_max_area(matrix))  # Output -> 6

    """
    Explanation:
    We are allowed to move in four directions (horizontal or vertical) so the possible
    in a matrix if we are at x and y position the possible moving are

    Directions are [(x, y+1), (x, y-1), (x+1, y), (x-1, y)] but we need to take care of
    boundary cases as well which are x and y can not be smaller than 0 and greater than
    the number of rows and columns respectively.

    Visualization
    mat = [
        [0,0,A,0,0,0,0,B,0,0,0,0,0],
        [0,0,0,0,0,0,0,B,B,B,0,0,0],
        [0,C,C,0,D,0,0,0,0,0,0,0,0],
        [0,C,0,0,D,D,0,0,E,0,E,0,0],
        [0,C,0,0,D,D,0,0,E,E,E,0,0],
        [0,0,0,0,0,0,0,0,0,0,E,0,0],
        [0,0,0,0,0,0,0,F,F,F,0,0,0],
        [0,0,0,0,0,0,0,F,F,0,0,0,0]
    ]

    For visualization, I have defined the connected island with letters
    by observation, we can see that
        A island is of area 1
        B island is of area 4
        C island is of area 4
        D island is of area 5
        E island is of area 6 and
        F island is of area 5

    it has 6 unique islands of mentioned areas
    and the maximum of all of them is 6 so we return 6.
    """

    doctest.testmod()
