"""
Question:
Given a binary matrix mat of size n * m, find out the maximum size square
sub-matrix with all 1s.

---
Example 1:

Input:
n = 2, m = 2
mat = [[1, 1],
       [1, 1]]

Output:
2

Explanation: The maximum size of the square
sub-matrix is 2. The matrix itself is the
maximum sized sub-matrix in this case.
---
Example 2

Input:
n = 2, m = 2
mat = [[0, 0],
       [0, 0]]
Output: 0

Explanation: There is no 1 in the matrix.


Approach:
We initialize another matrix (dp) with the same dimensions
as the original one initialized with all 0’s.

dp_array(i,j) represents the side length of the maximum square whose
bottom right corner is the cell with index (i,j) in the original matrix.

Starting from index (0,0), for every 1 found in the original matrix,
we update the value of the current element as

dp_array(i,j)=dp_array(dp(i−1,j),dp_array(i−1,j−1),dp_array(i,j−1)) + 1.
"""


from typing import List


from typing import List, Tuple


def largest_square_area_in_matrix_top_down_approch(
    rows: int, cols: int, mat: list[list[int]]
) -> int:
    """
    Function updates the largest_square_area[0], if recursive call found
    square with maximum area.

    We aren't using dp_array here, so the time complexity would be exponential.

    >>> largest_square_area_in_matrix_top_down_approch(2, 2, [[1,1], [1,1]])
    2
    >>> largest_square_area_in_matrix_top_down_approch(2, 2, [[0,0], [0,0]])
    0
    """

    def update_area_of_max_square(row: int, col: int) -> int:
        # BASE CASE
        if row >= rows or col >= cols:
            return 0

        right = update_area_of_max_square(row, col + 1)
        diagonal = update_area_of_max_square(row + 1, col + 1)
        down = update_area_of_max_square(row + 1, col)

        if mat[row][col]:
            sub_problem_sol = 1 + min([right, diagonal, down])
            largest_square_area[0] = max(largest_square_area[0], sub_problem_sol)
            return sub_problem_sol
        else:
            return 0

    largest_square_area = [0]
    update_area_of_max_square(0, 0)
    return largest_square_area[0]


def largest_square_area_in_matrix_top_down_approch_with_dp(
    rows: int, cols: int, mat: list[list[int]]
) -> int:
    """
    Function updates the largest_square_area[0], if recursive call found
    square with maximum area.

    We are using dp_array here, so the time complexity would be O(N^2).

    >>> largest_square_area_in_matrix_top_down_approch_with_dp(2, 2, [[1,1], [1,1]])
    2
    >>> largest_square_area_in_matrix_top_down_approch_with_dp(2, 2, [[0,0], [0,0]])
    0
    """

    def update_area_of_max_square_using_dp_array(
        row: int, col: int, dp_array: list[list[int]]
    ) -> int:
        if row >= rows or col >= cols:
            return 0
        if dp_array[row][col] != -1:
            return dp_array[row][col]

        right = update_area_of_max_square_using_dp_array(row, col + 1, dp_array)
        diagonal = update_area_of_max_square_using_dp_array(row + 1, col + 1, dp_array)
        down = update_area_of_max_square_using_dp_array(row + 1, col, dp_array)

        if mat[row][col]:
            sub_problem_sol = 1 + min([right, diagonal, down])
            largest_square_area[0] = max(largest_square_area[0], sub_problem_sol)
            dp_array[row][col] = sub_problem_sol
            return sub_problem_sol
        else:
            return 0

    largest_square_area = [0]
    dp_array = [[-1] * cols for _ in range(rows)]
    update_area_of_max_square_using_dp_array(0, 0, dp_array)

    return largest_square_area[0]

## REFACTORED CODE:


def largest_square_area_in_matrix_bottom_up(
    rows: int, cols: int, mat: List[List[int]]
) -> int:
    """
    Find the largest square area of 1s in a given binary matrix using a bottom-up approach.

    Args:
        rows (int): The number of rows in the input matrix.
        cols (int): The number of columns in the input matrix.
        mat (list[list[int]]): The input matrix as a 2D list of binary integers.

    Returns:
        int: The side length of the largest square of 1's in the input matrix.
    """
    if not rows or not cols:
        return 0

    dp_array = [[0] * (cols + 1) for _ in range(rows + 1)]
    largest_square_area = 0

    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            if mat[row][col] == 1:
                right = dp_array[row][col + 1]
                diagonal = dp_array[row + 1][col + 1]
                bottom = dp_array[row + 1][col]

                dp_array[row][col] = 1 + min(right, diagonal, bottom)
                largest_square_area = max(dp_array[row][col], largest_square_area)

    return largest_square_area


def largest_square_area_in_matrix_bottom_up_space_optimization(
    rows: int, cols: int, mat: List[List[int]]
) -> int:
    """
    Calculate largest square area in a binary matrix using a bottom-up approach with space optimization.
    """

    current_row = [0] * (cols + 1)
    next_row = [0] * (cols + 1)
    largest_square_area = 0

    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            square_area, current_row = calculate_square_area(
                mat, row, col, current_row, next_row
            )
            largest_square_area = max(square_area, largest_square_area)
        next_row = current_row

    return largest_square_area


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(largest_square_area_in_matrix_bottom_up(2, 2, [[1, 1], [1, 1]]))

def calculate_square_area(
    mat: List[List[int]],
    row: int,
    col: int,
    current_row: List[int],
    next_row: List[int],
) -> Tuple[int, List[int]]:
    """
    Calculates the square area at the provided cell and updates corresponding rows.

    Args:
        mat (List[List[int]]): The binary matrix.
        row (int): Index of current row.
        col (int): Index of current column.
        current_row (List[int]): Current row values for dynamic programming.
        next_row (List[int]): Next row values for dynamic programming.

    Returns:
        Tuple[int, List[int]]: Updated square area and current row.
    """
    right = current_row[col + 1]
    diagonal = next_row[col + 1]
    bottom = next_row[col]

    if mat[row][col] == 1:
        current_row[col] = 1 + min(right, diagonal, bottom)
        square_area = current_row[col]
    else:
        current_row[col] = 0
        square_area = 0

    return square_area, current_row
