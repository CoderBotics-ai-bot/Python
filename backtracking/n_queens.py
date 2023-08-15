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
    Check if it is safe to place a queen at the given location on the board.

    This function checks if there is any queen in the same row, column or diagonals
    from the given location. If there is no queen in the same row, column or diagonals,
    it returns True indicating it is safe to place a queen. Otherwise, it returns False.

    Parameters:
    board: A 2-D list representing the current state of the game.
    row: The row index of the location (0-indexed).
    column: The column index of the location (0-indexed).

    Returns:
    bool: True if it is safe to place a queen at the given location, False otherwise.

    Exception:
    None

    Side effect:
    This function does not change the state of the board.
    """
    return (
        is_row_safe(board, row)
        and is_column_safe(board, column)
        and is_diag_safe(board, row, column)
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

def is_row_safe(board: list[list[int]], row: int) -> bool:
    return not any(board[row])


def is_column_safe(board: list[list[int]], column: int) -> bool:
    return not any(row[column] for row in board)


def is_diag_safe(board: list[list[int]], row: int, column: int) -> bool:
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, len(board))):
        if board[i][j] == 1:
            return False
    return True


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
