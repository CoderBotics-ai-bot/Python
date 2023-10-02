import pytest
from backtracking.sudoku import *


@pytest.fixture
def initial_grid() -> Matrix:
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


@pytest.fixture
def no_solution() -> Matrix:
    return [
        [5, 3, 0, 0, 7, 0, 5, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 3, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 4, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


def test_sudoku_no_errors(initial_grid: Matrix):
    """
    Test if the function runs without throwing an error
    """
    try:
        sudoku(initial_grid)
    except Exception as e:
        pytest.fail(
            f"sudoku() raised {type(e).__name__} Exception with message: {str(e)}"
        )


def test_sudoku_not_none(initial_grid: Matrix):
    """
    Test if the function returns a value and is not None
    """
    assert sudoku(initial_grid) is not None


def test_sudoku_no_solution(no_solution: Matrix):
    """
    Test if the function returns None when no solution is possible
    """
    assert sudoku(no_solution) is None


def test_sudoku_type(initial_grid: Matrix):
    """
    Test if the return type matches the expected type
    """
    result = sudoku(initial_grid)
    assert isinstance(result, (type(None), list))


pytest
