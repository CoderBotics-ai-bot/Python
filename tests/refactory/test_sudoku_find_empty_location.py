import pytest
from backtracking.sudoku import *


def test_find_empty_location_no_errors():
    """
    This test checks if the function find_empty_location doesn't throw
    an error when it's executed.
    """
    # Initialize a grid
    grid = [[0 for _ in range(9)] for _ in range(9)]

    # Call the function
    result = find_empty_location(grid)

    # Check the result is not None
    assert result is not None


def test_find_empty_location_return():
    """
    This test checks if the function find_empty_location correctly
    returns the position of the first empty cell.
    """
    # Initialize a grid
    grid = [[1 for _ in range(9)] for _ in range(9)]
    grid[3][6] = 0

    # Call the function
    result = find_empty_location(grid)

    # Check the result is equal to the position of the empty cell
    assert result == (3, 6)


def test_find_empty_location_full_grid():
    """
    This test checks if the function find_empty_location correctly
    returns None when there are no empty cells.
    """
    # Initialize a grid
    grid = [[1 for _ in range(9)] for _ in range(9)]

    # Call the function
    result = find_empty_location(grid)

    # Check the result is None
    assert result is None
