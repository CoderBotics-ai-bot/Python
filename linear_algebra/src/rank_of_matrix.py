"""
Calculate the rank of a matrix.

See: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
"""


from typing import List, Union, Tuple

def rank_of_matrix(matrix: List[List[Union[int, float]]]) -> int:
    """Calculate the rank of a matrix using Gaussian row-reduction."""

    rank, row_pointer = initialize_rank_and_pointer(matrix)

    while row_pointer < rank:
        if matrix[row_pointer][row_pointer]:
            eliminate_elements_below(matrix, rank, row_pointer)

        else:
            is_swapped, rank = search_and_swap(matrix, rank, row_pointer)
            if not is_swapped:
                row_pointer -= 1

        row_pointer += 1

    return rank


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def initialize_rank_and_pointer(
    matrix: List[List[Union[int, float]]]
) -> Tuple[int, int]:
    num_rows, num_columns = len(matrix), len(matrix[0])
    rank = min(num_rows, num_columns)
    row_pointer = 0
    return rank, row_pointer


def eliminate_elements_below(
    matrix: List[List[Union[int, float]]], rank: int, row_pointer: int
) -> None:
    for i in range(row_pointer + 1, rank):
        scale_factor = matrix[i][row_pointer] / matrix[row_pointer][row_pointer]

        for j in range(row_pointer, rank):
            matrix[i][j] -= scale_factor * matrix[row_pointer][j]


def search_and_swap(
    matrix: List[List[Union[int, float]]], rank: int, row_pointer: int
) -> Tuple[bool, int]:
    for i in range(row_pointer + 1, rank):
        if matrix[i][row_pointer]:
            matrix[row_pointer], matrix[i] = matrix[i], matrix[row_pointer]
            return True, rank

    rank -= 1
    matrix[row_pointer], matrix[rank] = matrix[rank], matrix[row_pointer]
    return False, rank
