# Youtube Explanation: https://www.youtube.com/watch?v=lBRtnuxg-gU

from __future__ import annotations


from typing import List

def minimum_cost_path(matrix: List[List[int]]) -> int:
    """
    Given a matrix of integers, this function calculates and returns the minimum cost traced by all possible paths
    from the top left to the bottom right of the matrix. The cost of a path is defined as the sum of integers on that path.
    For movement, only right and down directions are allowed.

    Args:
        matrix (List[List[int]]): A 2D list of integers representing the matrix.

    Returns:
        int: The minimum cost traced by all possible paths in the matrix.

    Examples:
        >>> minimum_cost_path([[2, 1], [3, 1], [4, 2]])
        6

        >>> minimum_cost_path([[2, 1, 4], [2, 1, 3], [3, 2, 1]])
        7
    """
    preprocess_matrix(matrix)
    update_path_cost(matrix)
    return matrix[-1][-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def preprocess_matrix(matrix: List[List[int]]) -> None:
    """
    This function preprocesses the first row and first column of a matrix.

    Args:
        matrix (List[List[int]]): A 2D list of integers representing the matrix.
    """
    for i in range(1, len(matrix[0])):
        matrix[0][i] += matrix[0][i - 1]

    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[i - 1][0]


def update_path_cost(matrix: List[List[int]]) -> None:
    """
    This function updates the path cost for current position of a given matrix.

    Args:
        matrix (List[List[int]]): A 2D list of integers representing the matrix.
    """
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])
