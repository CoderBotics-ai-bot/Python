from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    """
    Function as before....
    """

    if not grid or not grid[0]:
        raise TypeError("The grid must be a populated 2D List.")

    calculate_initial_row(grid)
    calculate_grid_rows(grid)

    return grid[-1][-1]


def fill_row(current_row: list, row_above: list) -> list:
    """
    >>> fill_row([2, 2, 2], [1, 2, 3])
    [3, 4, 5]
    """

    current_row[0] += row_above[0]
    for cell_n in range(1, len(current_row)):
        current_row[cell_n] += min(current_row[cell_n - 1], row_above[cell_n])

    return current_row

def calculate_initial_row(grid: List[List[int]]) -> None:
    """
    Calculate the initial row values in the grid by accumulating the values
    """
    for cell_n in range(1, len(grid[0])):
        grid[0][cell_n] += grid[0][cell_n - 1]


def calculate_grid_rows(grid: List[List[int]]) -> None:
    """
    Calculate the rest of the grid row values based on the minimum path sum algorithm
    """
    for row_n in range(1, len(grid)):
        current_row = grid[row_n]
        grid[row_n] = fill_row(current_row, grid[row_n - 1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
