"""
Functions for 2D matrix operations
"""

from __future__ import annotations

from typing import Any
from typing import List


from typing import List
from typing import List, Any, Union


from typing import List, Union


def add(*matrix_s: list[list[int]]) -> list[list[int]]:
    """
    Same docstring as in the original function.
    """
    all_matrices_are_valid = all(_check_not_integer(m) for m in matrix_s)

    if not all_matrices_are_valid:
        raise TypeError("Expected a matrix, got int/list instead")

    for i in matrix_s[1:]:
        _verify_matrix_sizes(matrix_s[0], i)

    return _calculate_sum(matrix_s)

## REFACTORING ATTEMPT


def subtract(
    matrix_a: List[List[Union[int, float]]], matrix_b: List[List[Union[int, float]]]
) -> List[List[Union[int, float]]]:
    """
    Subtract one matrix from another and returns the resulting matrix

    Args:
    matrix_a (List[List[Union[int, float]]): The first matrix.
    matrix_b (List[List[Union[int, float]]): The second matrix.

    Returns:
    List[List[Union[int, float]]]: The resulting matrix after subtraction.

    Raises:
    TypeError: If inputs are not valid matrices.
    ValueError: If matrices have different shapes.
    """
    _validate_matrix(matrix_a)
    _validate_matrix(matrix_b)
    _verify_matrix_sizes(matrix_a, matrix_b)

    return [
        [a - b for a, b in zip(row_a, row_b)]
        for row_a, row_b in zip(matrix_a, matrix_b)
    ]

def multiply(matrix_a: List[List[int]], matrix_b: List[List[int]]) -> List[List[int]]:
    """
    Multiplies two matrices of the same shape.

    The matrices should be two-dimensional (i.e., a list of lists). Each inner list
    represents a row in the matrix. If the matrices are not of the same shape, a
    ValueError will be raised.

    Args:
        matrix_a (List[List[int]]): The first matrix to be multiplied.
        matrix_b (List[List[int]]): The second matrix to be multiplied.

    Returns:
        List[List[int]]: A new matrix which is the product of matrix_a and matrix_b.

    Raises:
        ValueError: If the two matrices are not of the same shape.

    Examples:
        >>> multiply([[1, 2], [3, 4]], [[5, 5], [7, 5]])
        [[19, 15], [43, 35]]
        >>> multiply([[1, 2.5], [3, 4.5]], [[5, 5], [7, 5]])
        [[22.5, 17.5], [46.5, 37.5]]
        >>> multiply([[1, 2, 3]], [[2], [3], [4]])
        [[20]]
    """
    _check_validity_for_multiplication(matrix_a, matrix_b)
    return [
        [sum(m * n for m, n in zip(i, j)) for j in zip(*matrix_b)] for i in matrix_a
    ]


## Associated Subroutines


def _validate_matrix(matrix: Any) -> None:
    """
    Validates the input matrix.

    Args:
    matrix (Any): The matrix to validate.

    Raises:
    TypeError: If the matrix is not valid.
    """
    if not isinstance(matrix, list):
        raise TypeError("Input argument is not a list.")
    for row in matrix:
        if not all(isinstance(n, (int, float)) for n in row):
            raise TypeError("Matrix elements are not numeric.")


def _check_validity_for_multiplication(
    matrix_a: List[List[int]], matrix_b: List[List[int]]
) -> None:
    if _check_not_integer(matrix_a) and _check_not_integer(matrix_b):
        rows, cols = _verify_matrix_sizes(matrix_a, matrix_b)
        if cols[0] != rows[1]:
            msg = (
                "Cannot multiply matrix of dimensions "
                f"({rows[0]},{cols[0]}) and ({rows[1]},{cols[1]})"
            )
            raise ValueError(msg)



def _calculate_sum(elements: List[List[int]]) -> int:
    """Calculate the sum of a given list of matrices."""
    return [[sum(t) for t in zip(*m)] for m in zip(*elements)]


def scalar_multiply(matrix: list[list[int]], n: float) -> list[list[float]]:
    """
    >>> scalar_multiply([[1,2],[3,4]],5)
    [[5, 10], [15, 20]]
    >>> scalar_multiply([[1.4,2.3],[3,4]],5)
    [[7.0, 11.5], [15, 20]]
    """
    return [[x * n for x in row] for row in matrix]

def inverse(matrix: List[List[int]]) -> Union[List[List[float]], None]:
    """
    Returns the inverse of the given matrix.

    Args:
        matrix (List[List[int]]): A 2D list representing the input matrix.

    Returns:
        Union[List[List[float]], None]: A 2D list representing the inverse of the
        input matrix. If the determinant of the input matrix is zero, the
        function returns None because the matrix is not invertible.

    Raises:
        ValueError: If the input is not a matrix or if the matrix is not square.
    """
    det = determinant(matrix)
    if det == 0:
        return None

    matrix_minor = calculate_minor_matrix(matrix)
    cofactors = calculate_cofactor_matrix(matrix_minor)
    adjugate = list(transpose(cofactors))
    return scalar_multiply(adjugate, 1 / det)


def identity(n: int) -> list[list[int]]:
    """
    :param n: dimension for nxn matrix
    :type n: int
    :return: Identity matrix of shape [n, n]
    >>> identity(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    n = int(n)
    return [[int(row == column) for column in range(n)] for row in range(n)]


def calculate_minor_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Calculate the minor of the provided matrix.

    Args:
        matrix (List[List[int]]): A 2D list representing the input matrix.

    Returns:
        List[List[int]]: A 2D list representing the minor of the input matrix.
    """
    return [
        [determinant(minor(matrix, i, j)) for j in range(len(matrix))]
        for i in range(len(matrix))
    ]


def calculate_cofactor_matrix(matrix_minor: List[List[int]]) -> List[List[int]]:
    """
    Calculate the cofactor of the provided minor matrix.

    Args:
        matrix_minor (List[List[int]]): A 2D list representing the minor matrix.

    Returns:
        List[List[int]]: A 2D list representing the cofactor of the minor matrix.
    """
    return [
        [x * (-1) ** (row + col) for col, x in enumerate(matrix_minor[row])]
        for row in range(len(matrix_minor))
    ]


def transpose(
    matrix: list[list[int]], return_map: bool = True
) -> list[list[int]] | map[list[int]]:
    """
    >>> transpose([[1,2],[3,4]]) # doctest: +ELLIPSIS
    <map object at ...
    >>> transpose([[1,2],[3,4]], return_map=False)
    [[1, 3], [2, 4]]
    >>> transpose([1, [2, 3]])
    Traceback (most recent call last):
      ...
    TypeError: Expected a matrix, got int/list instead
    """
    if _check_not_integer(matrix):
        if return_map:
            return map(list, zip(*matrix))
        else:
            return list(map(list, zip(*matrix)))
    raise TypeError("Expected a matrix, got int/list instead")


def minor(matrix: list[list[int]], row: int, column: int) -> list[list[int]]:
    """
    >>> minor([[1, 2], [3, 4]], 1, 1)
    [[1]]
    """
    minor = matrix[:row] + matrix[row + 1 :]
    return [row[:column] + row[column + 1 :] for row in minor]


def determinant(matrix: list[list[int]]) -> Any:
    """
    >>> determinant([[1, 2], [3, 4]])
    -2
    >>> determinant([[1.5, 2.5], [3, 4]])
    -1.5
    """
    if len(matrix) == 1:
        return matrix[0][0]

    return sum(
        x * determinant(minor(matrix, 0, i)) * (-1) ** i
        for i, x in enumerate(matrix[0])
    )


def _check_not_integer(matrix: list[list[int]]) -> bool:
    return not isinstance(matrix, int) and not isinstance(matrix[0], int)


def _shape(matrix: list[list[int]]) -> tuple[int, int]:
    return len(matrix), len(matrix[0])


def _verify_matrix_sizes(
    matrix_a: list[list[int]], matrix_b: list[list[int]]
) -> tuple[tuple[int, int], tuple[int, int]]:
    shape = _shape(matrix_a) + _shape(matrix_b)
    if shape[0] != shape[3] or shape[1] != shape[2]:
        msg = (
            "operands could not be broadcast together with shape "
            f"({shape[0], shape[1]}), ({shape[2], shape[3]})"
        )
        raise ValueError(msg)
    return (shape[0], shape[2]), (shape[1], shape[3])


def main() -> None:
    matrix_a = [[12, 10], [3, 9]]
    matrix_b = [[3, 4], [7, 4]]
    matrix_c = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
    matrix_d = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    print(f"Add Operation, {add(matrix_a, matrix_b) = } \n")
    print(f"Multiply Operation, {multiply(matrix_a, matrix_b) = } \n")
    print(f"Identity: {identity(5)}\n")
    print(f"Minor of {matrix_c} = {minor(matrix_c, 1, 2)} \n")
    print(f"Determinant of {matrix_b} = {determinant(matrix_b)} \n")
    print(f"Inverse of {matrix_d} = {inverse(matrix_d)}\n")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
