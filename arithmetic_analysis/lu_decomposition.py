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

def lower_upper_decomposition(table: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    verify_square_matrix(table)

    rows, columns = np.shape(table)
    lower = np.zeros((rows, columns))
    upper = np.zeros((rows, columns))

    for i in range(columns):
        calculate_lower_matrix(lower, upper, table, i)
        lower[i][i] = 1
        calculate_upper_matrix(lower, upper, table, i)

    return lower, upper


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def verify_square_matrix(table: np.ndarray):
    rows, columns = np.shape(table)
    if rows != columns:
        msg = (
            "'table' has to be of square shaped array but got a "
            f"{rows}x{columns} array:\n{table}"
        )
        raise ValueError(msg)


def calculate_lower_matrix(
    lower: np.ndarray, upper: np.ndarray, table: np.ndarray, i: int
):
    for j in range(i):
        total = sum(lower[i][k] * upper[k][j] for k in range(j))
        if upper[j][j] == 0:
            raise ArithmeticError("No LU decomposition exists")
        lower[i][j] = (table[i][j] - total) / upper[j][j]


def calculate_upper_matrix(
    lower: np.ndarray, upper: np.ndarray, table: np.ndarray, i: int
):
    for j in range(i, len(upper[i])):
        total = sum(lower[i][k] * upper[k][j] for k in range(i))
        upper[i][j] = table[i][j] - total
