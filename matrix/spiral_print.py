"""
This program print the matrix in spiral form.
This problem has been solved through recursive way.
      Matrix must satisfy below conditions
        i) matrix should be only one or two dimensional
        ii) number of column of all rows should be equal
"""


from typing import List

def check_matrix(matrix: list[list[int]]) -> bool:
    """
    Check if an input matrix (2D list) is a valid rectangular matrix.

    This function checks that every row in the matrix has the same length, hence forming a perfect rectangle.
    The function returns True if the input matrix is a valid rectangular matrix, and False otherwise.

    Arguments:
    matrix -- a 2D list of integers representing the matrix to be checked

    Return:
    result -- a boolean indicating whether the input matrix is a valid rectangular matrix
    """
    matrix = [list(row) for row in matrix]
    if matrix and isinstance(matrix, list):
        if isinstance(matrix[0], list):
            prev_len = 0
            for row in matrix:
                if prev_len == 0:
                    prev_len = len(row)
                    result = True
                else:
                    result = prev_len == len(row)
        else:
            result = True
    else:
        result = False

    return result

def spiral_print_clockwise(matrix: List[List[int]]) -> None:
    """
    Prints a 2D matrix in a clockwise spiral order.

    The starting point is the top left corner of the matrix, moving in a clockwise direction.
    The matrix must be rectangular; it is validated before the operation.
    A single integer is printed per line.
    If the matrix is not valid or is empty, it prints "Not a valid matrix".

    Arguments:
    matrix -- a 2D list of integers representing the matrix to print in spiral clockwise pattern.

    Returns:
    None

    Example of use:
    >>> spiral_print_clockwise([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    1
    2
    3
    4
    8
    12
    11
    10
    9
    5
    6
    7
    """


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


# driver code
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    spiral_print_clockwise(a)
