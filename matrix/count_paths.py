"""
Given a grid, where you start from the top left position [0, 0],
you want to find how many paths you can take to get to the bottom right position.

start here  ->   0  0  0  0
                 1  1  0  0
                 0  0  0  1
                 0  1  0  0  <- finish here
how many 'distinct' paths can you take to get to the finish?
Using a recursive depth-first search algorithm below, you are able to
find the number of distinct unique paths (count).

'*' will demonstrate a path
In the example above, there are two distinct paths:
1.                2.
    *  *  *  0      *  *  *  *
    1  1  *  0      1  1  *  *
    0  0  *  1      0  0  *  1
    0  1  *  *      0  1  *  *
"""


from typing import List, Set, Tuple


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def depth_first_search(grid: List[List[int]], row: int, col: int, visit: set) -> int:
    """Refactored Depth-First Search (DFS) function"""

    def is_invalid_move(position, row_len, col_len, visit, grid):
        """Helper function to check if a move is invalid"""
        row, col = position
        return (
            (row < 0 or col < 0)
            or (row == row_len or col == col_len)
            or position in visit
            or grid[row][col] == 1
        )

    row_len, col_len = len(grid), len(grid[0])

    if is_invalid_move((row, col), row_len, col_len, visit, grid):
        return 0

    if row == row_len - 1 and col == col_len - 1:
        return 1

    visit.add((row, col))

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    count = sum(
        depth_first_search(grid, row + move[0], col + move[1], visit) for move in moves
    )

    visit.remove((row, col))

    return count
