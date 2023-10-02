"""
Lower–upper (LU) decomposition factors a matrix as a product of a lower
triangular matrix and an upper triangular matrix. A square matrix has an LU
decomposition under the following conditions:
    - If the matrix is invertible, then it has an LU decomposition if and only
    if all of its leading principal minors are non-zero (see
    https://en.wikipedia.org/wiki/Minor_(linear_algebra) for an explanation of
    leading principal minors of a matrix).
    - If the matrix is singular (i.e., not invertible) and it has a rank of k
    (i.e., it has k linearly independent columns), then it has an LU
    decomposition if its first k leading principal minors are non-zero.

This algorithm will simply attempt to perform LU decomposition on any square
matrix and raise an error if no such decomposition exists.

Reference: https://en.wikipedia.org/wiki/LU_decomposition
"""
from __future__ import annotations

import numpy as np


if __name__ == "__main__":
    import doctest

    doctest.testmod()



def lower_upper_decomposition(table: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Perform LU decomposition on a given matrix and raises an error if the matrix
    isn't square or if no such decomposition exists

    :param table: 2D array representing a square matrix
    :type table: np.ndarray
    :return: lower matrix and upper matrix after LU decomposition
    :rtype: tuple[np.ndarray, np.ndarray]
    :raises ValueError: if the table is not a square array
    :raises ArithmeticError: if no LU decomposition exists
    """
    _validate_square_table(table)
    lower, upper = _calculate_lower_upper(table)
    return lower, upper


def _validate_square_table(table: np.ndarray) -> None:
    rows, columns = table.shape
    if rows != columns:
        raise ValueError(
            f"'table' has to be of square shaped array but got a {rows}x{columns} array:\n{table}"
        )


def _calculate_lower_upper(table: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    rows, columns = table.shape
    lower = np.zeros_like(table)
    upper = np.zeros_like(table)

    for i in range(columns):
        _compute_lower(i, table, lower, upper)
        lower[i][i] = 1
        _compute_upper(i, table, lower, upper)

    return lower, upper


def _compute_lower(
    i: int, table: np.ndarray, lower: np.ndarray, upper: np.ndarray
) -> None:
    for j in range(i):
        total = sum(lower[i][k] * upper[k][j] for k in range(j))
        if upper[j][j] == 0:
            raise ArithmeticError("No LU decomposition exists")
        lower[i][j] = (table[i][j] - total) / upper[j][j]


def _compute_upper(
    i: int, table: np.ndarray, lower: np.ndarray, upper: np.ndarray
) -> None:
    for j in range(i, table.shape[1]):
        total = sum(lower[i][k] * upper[k][j] for k in range(j))
        upper[i][j] = table[i][j] - total
