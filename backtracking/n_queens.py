"""

 The nqueens problem is of placing N queens on a N * N
 chess board such that no queen can attack any other queens placed
 on that chess board.
 This means that one queen cannot have any other queen on its horizontal, vertical and
 diagonal lines.

"""
from __future__ import annotations

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


def solve(board: list[list[int]], row: int) -> bool:
    """
    It creates a state space tree and calls the safe function until it receives a
    False Boolean and terminates that branch and backtracks to the next
    possible solution branch.
    """
    if row >= len(board):
        """
        If the row number exceeds N we have board with a successful combination
        and that combination is appended to the solution list and the board is printed.

        """
        solution.append(board)
        printboard(board)
        print()
        return True
    for i in range(len(board)):
        """
        For every row it iterates through each column to check if it is feasible to
        place a queen there.
        If all the combinations for that particular branch are successful the board is
        reinitialized for the next possible combination.
        """
        if is_safe(board, row, i):
            board[row][i] = 1
            solve(board, row + 1)
            board[row][i] = 0
    return False

def is_in_row(board: list[list[int]], row: int) -> bool:
    """Check if a queen exists in the given row of the board."""
    return 1 in board[row]


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


def printboard(board: list[list[int]]) -> None:
    """
    Prints the boards that have a successful combination.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# n=int(input("The no. of queens"))
n = 8
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("The total no. of solutions are :", len(solution))
