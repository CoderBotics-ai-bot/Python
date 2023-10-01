"""
Functions for 2D matrix operations
"""

from __future__ import annotations

from typing import Any
from typing import List


from typing import List


from typing import Any, List
from typing import List, Union
from itertools import zip_longest


from typing import List, Union
from itertools import zip_longest


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

def subtract(
    matrix_a: List[List[float]], matrix_b: List[List[float]]
) -> List[List[float]]:
    """
    Subtracts one matrix from another and returns the resulting matrix.

    Parameters:
        matrix_a (List[List[int]]) : The first matrix.
        matrix_b (List[List[int]]) : The second matrix.

    Returns:
        List[List[int]] : The resulting matrix after subtraction.

    Raises:
        TypeError : If inputs are not of type List[List[int]].
        ValueError : If matrices have different sizes.
    """

    _validate_input(matrix_a, matrix_b)

    return [
        [a - b for a, b in zip(row_a, row_b)]
        for row_a, row_b in zip(matrix_a, matrix_b)
    ]



def multiply(
    matrix_a: List[List[Union[int, float]]], matrix_b: List[List[Union[int, float]]]
) -> List[List[Union[int, float]]]:
    """
    Multiplies two matrices if they are compatible for multiplication.

    Args:
        matrix_a (List[List[Union[int, float]]]): First matrix.
        matrix_b (List[List[Union[int, float]]]): Second matrix.

    Returns:
        List[List[Union[int, float]]]: The product of matrix_a and matrix_b.

    Raises:
        ValueError: If the numbers of columns in the first matrix
                    doesn't match the number of rows in the second matrix
        ValueError: If a value in the matrices is not a float or an integer.

    Examples:
        >>> multiply([[1,2],[3,4]],[[5,5],[7,5]])
        [[19, 15], [43, 35]]
        >>> multiply([[1,2.5],[3,4.5]],[[5,5],[7,5]])
        [[22.5, 17.5], [46.5, 37.5]]
        >>> multiply([[1, 2, 3]], [[2], [3], [4]])
        [[20]]
    """
    _check_elements_type(matrix_a)
    _check_elements_type(matrix_b)

    rows_a, cols_a = _get_matrix_sizes(matrix_a)
    rows_b, cols_b = _get_matrix_sizes(matrix_b)

    if cols_a != rows_b:
        raise ValueError(
            f"Cannot multiply matrices of dimensions ({rows_a},{cols_a}) and ({rows_b},{cols_b})"
        )

    return _calculate_matrix_product(matrix_a, matrix_b)


# Newly created (sub-)functions
def _validate_input(matrix_a: Any, matrix_b: Any) -> None:
    _validate_matrix(matrix_a)
    _validate_matrix(matrix_b)

    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Both matrices should have the same dimensions.")


def _check_elements_type(matrix: List[List[Union[int, float]]]) -> None:
    for row in matrix:
        if not all(isinstance(val, (int, float)) for val in row):
            raise ValueError("Matrix values must be integers or floats.")


def _get_matrix_sizes(matrix: List[List[Union[int, float]]]) -> tuple[int, int]:
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    return (rows, cols)


def _calculate_matrix_product(
    matrix_a: List[List[Union[int, float]]], matrix_b: List[List[Union[int, float]]]
) -> List[List[Union[int, float]]]:
    transposed_b = list(map(list, zip_longest(*matrix_b, fillvalue=0)))
    return [
        [sum(a * b for a, b in zip(row_a, row_b)) for row_b in transposed_b]
        for row_a in matrix_a
    ]


def _validate_matrix(matrix: Any) -> None:
    if not (
        isinstance(matrix, (list, tuple))
        and all(
            isinstance(row, (list, tuple))
            and all(isinstance(item, (int, float)) for item in row)
            for row in matrix
        )
    ):
        raise TypeError("All elements of the matrix should be of type int/float.")



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


def inverse(matrix: list[list[int]]) -> list[list[float]] | None:
    """
    >>> inverse([[1, 2], [3, 4]])
    [[-2.0, 1.0], [1.5, -0.5]]
    >>> inverse([[1, 1], [1, 1]])
    """
    # https://stackoverflow.com/questions/20047519/python-doctests-test-for-none
    det = determinant(matrix)
    if det == 0:
        return None

    matrix_minor = [
        [determinant(minor(matrix, i, j)) for j in range(len(matrix))]
        for i in range(len(matrix))
    ]

    cofactors = [
        [x * (-1) ** (row + col) for col, x in enumerate(matrix_minor[row])]
        for row in range(len(matrix))
    ]
    adjugate = list(transpose(cofactors))
    return scalar_multiply(adjugate, 1 / det)


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
