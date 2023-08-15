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
    Check if a provided matrix is valid.

    This function considers a valid matrix to be a list of lists,
    where each sub list (row) has the same number of elements.

    Args:
        matrix (List[List[int]]): The matrix to be checked.

    Returns:
        bool: True if the matrix is valid, False otherwise.
    """
    # Guard clause to check if matrix is None or not a list
    if matrix is None or not isinstance(matrix, list):
        return False

    try:
        # Check if all rows in matrix are lists and have the same length
        matrix_length = len(matrix[0])
        return all(
            isinstance(row, list) and len(row) == matrix_length for row in matrix
        )
    except (TypeError, IndexError):
        return False

def spiral_print_clockwise(matrix: List[List[int]]) -> None:
    """
    Prints the elements of a given 2D matrix in a clockwise spiral pattern.

    Args:
        matrix (List[List[int]]): The 2D list (matrix) whose elements are to be printed.

    Returns:
        None
    """
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        print("Not a valid matrix.")
        return

    while matrix:
        # Print the first row
        for element in matrix.pop(0):
            print(element)
        # Print right side
        for row in matrix:
            if row:
                print(row.pop())
        # If any row left, print it in reverse order
        if matrix:
            for element in matrix.pop()[::-1]:
                print(element)
        # Print the left side, if any row left
        for row in matrix[::-1]:
            if row:
                print(row.pop(0))


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
