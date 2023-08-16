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


from typing import List, Set

def depth_first_search(grid: List[List[int]], row: int, col: int, visit: Set) -> int:
    """
    Recursive Backtracking Depth First Search Algorithm for counting the number of valid paths in a matrix.

    This function takes as input a matrix, starting point and a set of visited points,
    and returns the number of valid paths from the top left to bottom right of the matrix.
    The matrix representation is such that:
    1 represents a block (untraversable)
    0 represents a valid space (traversable)

    Parameters:
    grid (List[List[int]]): The input grid represented as a 2-D list.
    row (int): The current row index.
    col (int): The current column index.
    visit (Set): A set storing coordinates of the visited cells.

    Returns:
    int: The number of valid paths from top left to bottom right.

    Numbers represent cells in the matrix. For example, the matrix:

    0  0  0  0
    1  1  0  0
    0  0  0  1
    0  1  0  0

    is represented by the list [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]].
    When passed to this function along with a set(), will return 2, representing two distinct paths from start to finish.
    """
    row_length, col_length = len(grid), len(grid[0])
    if (
        min(row, col) < 0
        or row == row_length
        or col == col_length
        or (row, col) in visit
        or grid[row][col] == 1
    ):
        return 0
    if row == row_length - 1 and col == col_length - 1:
        return 1

    visit.add((row, col))

    count = 0
    count += depth_first_search(grid, row + 1, col, visit)
    count += depth_first_search(grid, row - 1, col, visit)
    count += depth_first_search(grid, row, col + 1, visit)
    count += depth_first_search(grid, row, col - 1, visit)

    visit.remove((row, col))
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
