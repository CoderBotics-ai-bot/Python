"""
The number of partitions of a number n into at least k parts equals the number of
partitions into exactly k parts plus the number of partitions into at least k-1 parts.
Subtracting 1 from each part of a partition of n into k parts gives a partition of n-k
into k parts. These two facts together are used for this algorithm.
"""


def partition(m: int) -> int:
    """
    See original function docstring for details.
    """
    memo = create_zero_matrix(m + 1, m)
    initialize_first_column(memo)
    calculate_partitions(memo, m)

    return memo[m][m - 1]


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        try:
            n = int(input("Enter a number: ").strip())
            print(partition(n))
        except ValueError:
            print("Please enter a number.")
    else:
        try:
            n = int(sys.argv[1])
            print(partition(n))
        except ValueError:
            print("Please pass a number.")

def create_zero_matrix(rows: int, columns: int) -> list[list[int]]:
    """
    Create a 2D matrix filled with zeros.

    Args:
        rows: Number of rows in the matrix.
        columns: Number of columns in the matrix.

    Returns:
        A 2D list filled with zeros.
    """
    return [[0 for _ in range(columns)] for _ in range(rows)]


def initialize_first_column(matrix: list[list[int]]) -> None:
    """
    Sets the first column of the matrix to values to 1.

    Args:
        matrix: The 2D matrix

    Returns:
        None
    """
    for i in range(len(matrix)):
        matrix[i][0] = 1


def calculate_partitions(matrix: list[list[int]], m: int) -> None:
    """
    Calculate the total number of partitions for all numbers up to m.

    This modifies the given matrix in place.

    Args:
        matrix: The 2D matrix
        m: The number to partition.

    Returns:
        None
    """
    for n in range(len(matrix)):
        for k in range(1, m):
            matrix[n][k] += matrix[n][k - 1]
            if n - k > 0:
                matrix[n][k] += matrix[n - k - 1][k]
