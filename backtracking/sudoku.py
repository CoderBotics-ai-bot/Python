"""
Given a partially filled 9×9 2D array, the objective is to fill a 9×9
square grid with digits numbered 1 to 9, so that every row, column, and
and each of the nine 3×3 sub-grids contains all of the digits.

This can be solved using Backtracking and is similar to n-queens.
We check to see if a cell is safe or not and recursively call the
function on the next column to see if it returns True. if yes, we
have solved the puzzle. else, we backtrack and place another number
in that cell and repeat this process.
"""
from __future__ import annotations
from typing import List

Matrix = list[list[int]]

# assigning initial values to the grid
initial_grid: Matrix = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

# a grid with no solution
no_solution: Matrix = [
    [5, 0, 6, 5, 0, 8, 4, 0, 3],
    [5, 2, 0, 0, 0, 0, 0, 0, 2],
    [1, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


def is_safe(grid: Matrix, row: int, column: int, n: int) -> bool:
    """
    Check if it's safe to place a number 'n' at the given 'row' and 'column' in the Sudoku 'grid'.

    Args:
        grid (Matrix): A 9x9 2D list representing the Sudoku grid, where grid[i][j]
                       represents the number in the ith row and jth column.
        row (int): The row number where we want to place the number 'n'.
        column (int): The column number where we want to place the number 'n'.
        n (int): The number that we want to place in the grid at the given row and column.

    Returns:
        bool: Returns True if it is safe (duplicate digit is not found) to place the number 'n' at
              the given row and column. Returns False otherwise.
    """
    return (
        not is_in_row(grid, row, n)
        and not is_in_col(grid, column, n)
        and not is_in_box(grid, row, column, n)
    )

def find_empty_location(grid: Matrix) -> tuple[int, int] | None:
    """
    Find the first empty location in the Sudoku grid.

    This function iterates through the given grid and returns a tuple
    representing the row and column indices of the first empty (0) position
    encountered. The iteration starts from the top-left corner (0, 0) and moves
    rightwards and downwards. If no empty position is found, the function returns None.

    Args:
        grid (Matrix): 2D list of integers representing the Sudoku grid.

    Returns:
        tuple[int, int] | None: The row and column index of the first empty position
        encountered or None if no empty position is found.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def sudoku(grid: Matrix) -> Matrix | None:
    """
    Solve a Sudoku puzzle using a backtracking algorithm.

    Args:
        grid (Matrix): A 9x9 2D list representing the Sudoku grid.

    Returns:
        Matrix | None: The solved Sudoku grid, or None if no solution exists.
    """
    # If there is no empty location, the puzzle is solved.
    location = find_empty_location(grid)
    if not location:
        return grid

    row, column = location

    for digit in range(1, 10):
        if is_safe(grid, row, column, digit):
            # Try this digit for the current cell
            grid[row][column] = digit

            # Recur to solve the rest of the grid
            if sudoku(grid):
                return grid

            # If the recursion didn't find a solution, reset the cell and continue with the next digit
            grid[row][column] = 0

    # If no viable digits can be placed, this is a dead end
    return None

def is_in_row(grid: Matrix, row: int, n: int) -> bool:
    """Check if the number n is already present in the given row of the Sudoku grid."""
    return n in grid[row]


def is_in_col(grid: Matrix, col: int, n: int) -> bool:
    """Check if the number n is already present in the given column of the Sudoku grid."""
    return n in [row[col] for row in grid]


def is_in_box(grid: Matrix, row: int, col: int, num: int) -> bool:
    """Check if the number n is already present in the 3x3 square of the Sudoku grid."""
    for i in range(3):
        for j in range(3):
            if grid[i + (row - row % 3)][j + (col - col % 3)] == num:
                return True
    return False


def print_solution(grid: Matrix) -> None:
    """
    A function to print the solution in the form
    of a 9x9 grid
    """
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()


if __name__ == "__main__":
    # make a copy of grid so that you can compare with the unmodified grid
    for example_grid in (initial_grid, no_solution):
        print("\nExample grid:\n" + "=" * 20)
        print_solution(example_grid)
        print("\nExample grid solution:")
        solution = sudoku(example_grid)
        if solution is not None:
            print_solution(solution)
        else:
            print("Cannot find a solution.")
