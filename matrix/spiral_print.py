"""
This program print the matrix in spiral form.
This problem has been solved through recursive way.
      Matrix must satisfy below conditions
        i) matrix should be only one or two dimensional
        ii) number of column of all rows should be equal
"""


from typing import List

def check_matrix(matrix: List[List[int]]) -> bool:
    """
    Validate the input matrix.

    This function verifies whether the input matrix is a list of equal-length lists (rows).

    Args:
        matrix (List[List[int]]): The matrix to check.

    Returns:
        bool: True if the matrix is valid. Otherwise, False.
    """
    if not isinstance(matrix, list) or not matrix or not isinstance(matrix[0], list):
        return False

    return all(len(row) == len(matrix[0]) for row in matrix)

def spiral_print_clockwise(a: List[List[int]]) -> None:
    """Prints a given matrix in a clockwise spiral manner."""
    if not a or not check_matrix(a):
        print("Not a valid matrix")
        return

    a = copy_2d_array(a)
    spiral_print(a)


# Other Easy to understand Approach


def spiral_traversal(matrix: list[list]) -> list[int]:
    """
    >>> spiral_traversal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    Example:
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    Algorithm:
        Step 1. first pop the 0 index list. (which is [1,2,3,4] and concatenate the
                output of [step 2])
        Step 2. Now perform matrix’s Transpose operation (Change rows to column
                and vice versa) and reverse the resultant matrix.
        Step 3. Pass the output of [2nd step], to same recursive function till
                base case hits.
    Dry Run:
    Stage 1.
    [1, 2, 3, 4] +   spiral_traversal([
        [8, 12], [7, 11], [6, 10], [5, 9]]
     ])
    Stage 2.
    [1, 2, 3, 4, 8, 12] + spiral_traversal([
        [11, 10, 9], [7, 6, 5]
    ])
    Stage 3.
    [1, 2, 3, 4, 8, 12, 11, 10, 9] + spiral_traversal([
        [5], [6], [7]
    ])
    Stage 4.
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5] + spiral_traversal([
        [5], [6], [7]
    ])
    Stage 5.
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5] + spiral_traversal([[6, 7]])
    Stage 6.
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7] + spiral_traversal([])
    """
    if matrix:
        return list(matrix.pop(0)) + spiral_traversal(list(zip(*matrix))[::-1])
    else:
        return []


def copy_2d_array(arr: List[List[int]]) -> List[List[int]]:
    """Copies a 2-dimensional array."""
    return [list(row) for row in arr]


def spiral_print(a: List[List[int]]) -> None:
    """Prints the 2D matrix in a spiral order."""
    print_top_row(a)
    print_right_column(a)
    print_bottom_row(a)
    print_left_column(a)

    # Keep recursively printing the remaining parts.
    if a:
        spiral_print(a)


def valid_dimensions(arr: List[List[int]]) -> bool:
    """Checks whether the 2D array has valid dimensions for spiral printing."""
    n_rows = len(arr)
    n_cols = len(arr[0]) if n_rows > 0 else 0
    return n_rows > 1 and n_cols > 0


def print_top_row(a: List[List[int]]) -> None:
    """Prints the top row and removes it."""
    for e in a.pop(0):
        print(e)


def print_right_column(a: List[List[int]]) -> None:
    """Prints the right column and removes it."""
    for row in a:
        print(row.pop())


def print_bottom_row(a: List[List[int]]) -> None:
    """Prints the bottom row in reverse order and removes it."""
    if a:
        for e in reversed(a.pop()):
            print(e)


def print_left_column(a: List[List[int]]) -> None:
    """Prints the left column in reverse order and removes it."""
    if a:
        for row in reversed(a):
            print(row.pop(0))


# driver code
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    spiral_print_clockwise(a)
