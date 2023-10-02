"""

 The nqueens problem is of placing N queens on a N * N
 chess board such that no queen can attack any other queens placed
 on that chess board.
 This means that one queen cannot have any other queen on its horizontal, vertical and
 diagonal lines.

"""
from __future__ import annotations


from typing import List

solution = []


def is_safe(board: list[list[int]], row: int, column: int) -> bool:
    """
    Check if it's safe to place a queen at given position on the board.

    Parameters
    ----------
    board : list[list[int]]
        A nested list representing the current state of the chess board.
        '1' indicates there's a queen at that cell and '0' indicates the cell is empty.
    row : int
        The row index of the board where the safety for placing a queen is being checked.
    column : int
        The column index of the board where the safety for placing a queen is being checked.

    Returns
    -------
    bool
        `True` if it's safe to place a queen at the (row, column),
        `False` otherwise.
    """
    return not (
        is_in_row(board, row)
        or is_in_column(board, column)
        or is_in_diagonal(board, row, column)
    )

def solve(board: List[List[int]], row: int) -> bool:
    """Solve the N-Queens problem using backtracking."""
    if _all_rows_completed(board, row):
        _handle_solution(board)
        return True

    for i in range(len(board)):
        if is_safe(board, row, i):
            _process_domain_value(board, row, i)

    return False

def is_in_row(board: list[list[int]], row: int) -> bool:
    """Check if a queen exists in the given row of the board."""
    return 1 in board[row]

def printboard(board: List[List[int]]) -> None:
    """
    Prints the board that has a successful combination.

    Args:
    board (List[List[int]]): The N x N board where queens are currently placed.

    Returns:
    None
    """
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row), end=" ")
        print()


def _all_rows_completed(board: List[List[int]], row: int) -> bool:
    """Check if all rows have been filled."""
    return row >= len(board)


def _handle_solution(board: List[List[int]]) -> None:
    """Handle the successful completion of a board configuration."""
    solution.append(board)
    printboard(board)
    print()


def _process_domain_value(board: List[List[int]], row: int, i: int) -> None:
    """Act on a potential domain value."""
    board[row][i] = 1
    solve(board, row + 1)
    board[row][i] = 0


def is_in_column(board: list[list[int]], column: int) -> bool:
    """Check if a queen exists in the given column of the board."""
    return 1 in [row[column] for row in board]


def is_in_diagonal(board: list[list[int]], row: int, column: int) -> bool:
    """Check if a queen exists in any of the diagonals for the given position."""
    return any(
        board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(column, -1, -1))
    ) or any(
        board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(column, len(board)))
    )


# n=int(input("The no. of queens"))
n = 8
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("The total no. of solutions are :", len(solution))
