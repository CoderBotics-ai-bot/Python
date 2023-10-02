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
    board: list[list[int]], pos: tuple[int, int], curr: int
) -> bool:
    """
    Helper function to solve knight tour problem.
    """

    if is_complete(board):
        return True

    for position in get_valid_pos(pos, len(board)):
        y, x = position

        if board[y][x] == 0:
            board[y][x] = curr + 1
            if open_knight_tour_helper(board, position, curr + 1):
                return True
            board[y][x] = 0

    return False


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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
