# Knight Tour Intro: https://www.youtube.com/watch?v=ab_dY3dZFHM

from __future__ import annotations


from typing import List, Tuple

def get_valid_pos(position: tuple[int, int], n: int) -> list[tuple[int, int]]:
    """
    Given a position on a knight's tour chessboard, compute all the valid movements a knight can make.

    Args:
        position (tuple): Represents the current position of the knight. Contains integers row and column.
        n (int): The size of the chessboard (n x n).

    Returns:
        list: Contains valid positions where the knight can move to from the current position.
    """
    y, x = position
    movements = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    valid_positions = []
    for move in movements:
        move_y, move_x = move
        new_y, new_x = y + move_y, x + move_x
        if 0 <= new_y < n and 0 <= new_x < n:
            valid_positions.append((new_y, new_x))

    return valid_positions


def is_complete(board: list[list[int]]) -> bool:
    """
    Check if the board (matrix) has been completely filled with non-zero values.

    >>> is_complete([[1]])
    True

    >>> is_complete([[1, 2], [3, 0]])
    False
    """

    return not any(elem == 0 for row in board for elem in row)

def open_knight_tour_helper(
    board: List[List[int]], pos: Tuple[int, int], curr: int
) -> bool:
    """
    Recursive helper function to solve the open knight's tour problem. This function works by checking
    if the board traversal is complete, if it's complete it returns True immediately. If not, it continues
    to check and mark each valid move from the current position to find a solution path. If none found, it
    backtracks by resetting the current position to zero.

    Args:
        board (List[List[int]]): A 2D list representing the chessboard, containing numbers indicating the visit order
        pos (Tuple[int, int]): Current position of the knight
        curr (int): The current step number of the knight.

    Returns:
        bool: Returns True if a solution is found, otherwise False.
    """
    if is_complete(board):
        return True

    return try_next_positions(board, pos, curr)


def open_knight_tour(n: int) -> list[list[int]]:
    """
    Find the solution for the knight tour problem for a board of size n. Raises
    ValueError if the tour cannot be performed for the given size.

    >>> open_knight_tour(1)
    [[1]]

    >>> open_knight_tour(2)
    Traceback (most recent call last):
        ...
    ValueError: Open Kight Tour cannot be performed on a board of size 2
    """

    board = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            board[i][j] = 1
            if open_knight_tour_helper(board, (i, j), 1):
                return board
            board[i][j] = 0

    msg = f"Open Kight Tour cannot be performed on a board of size {n}"
    raise ValueError(msg)


def try_next_positions(board: List[List[int]], pos: Tuple[int, int], curr: int) -> bool:
    """
    Helper function to try and mark all valid positions from the current position. If a solution path
    is found, returns True, else it backtracks by unmarking the current position and returning False

    Args:
        board (List[List[int]]): A 2D list representing the chessboard, containing numbers indicating the visit order
        pos (Tuple[int, int]): Current position of the knight
        curr (int): The current step number of the knight.

    Returns:
        bool: Returns True if a solution is found, otherwise False.
    """

    for position in get_valid_pos(pos, len(board)):
        y, x = position

        if board[y][x] == 0:
            board[y][x] = curr + 1
            if open_knight_tour_helper(board, position, curr + 1):
                return True
            board[y][x] = 0

    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
