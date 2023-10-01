import sys


from typing import List, Tuple

"""
Dynamic Programming
Implementation of Matrix Chain Multiplication
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

def matrix_chain_order(array: List[int]) -> Tuple[List[List[int]], List[List[int]]]:
    """
    Calculates the optimal order of matrix chain multiplication and the cost of the optimal solution.

    This function uses dynamic programming to solve the problem of matrix chain multiplication. Given a sequence of matrices,
    it determines the most efficient way to multiply these matrices.

    Arguments:
    array: List of matrices dimensions.

    Returns: A tuple containing:
    - A matrix (list of lists) that stores the cost of the minimal cost multiplications.
    - A solution matrix (list of lists) that records which index of matrix achieved optimal cost.


    """

    n = len(array)

    # Initialize matrices
    matrix, sol = initialize_matrices(n)

    # Calculate optimal matrix chain order
    for chain_length in range(2, n):
        for a in range(1, n - chain_length + 1):
            b = a + chain_length - 1
            matrix[a][b], sol[a][b] = get_minimum_cost(array, matrix, a, b)

    return matrix, sol


# Print order of matrix with Ai as Matrix
def print_optiomal_solution(optimal_solution, i, j):
    if i == j:
        print("A" + str(i), end=" ")
    else:
        print("(", end=" ")
        print_optiomal_solution(optimal_solution, i, optimal_solution[i][j])
        print_optiomal_solution(optimal_solution, optimal_solution[i][j] + 1, j)
        print(")", end=" ")


def initialize_matrices(n: int) -> Tuple[List[List[int]], List[List[int]]]:
    """Initialize the matrices with zeros."""
    return [[0 for _ in range(n)] for _ in range(n)], [
        [0 for _ in range(n)] for _ in range(n)
    ]


def get_minimum_cost(
    array: List[int], matrix: List[List[int]], a: int, b: int
) -> Tuple[int, int]:
    """Compute the minimum multiplication cost and the matrix index."""
    min_cost = sys.maxsize

    for c in range(a, b):
        cost = matrix[a][c] + matrix[c + 1][b] + array[a - 1] * array[c] * array[b]
        if cost < min_cost:
            min_cost = cost
            min_index = c

    return min_cost, min_index


def main():
    array = [30, 35, 15, 5, 10, 20, 25]
    n = len(array)
    # Size of matrix created from above array will be
    # 30*35 35*15 15*5 5*10 10*20 20*25
    matrix, optimal_solution = matrix_chain_order(array)

    print("No. of Operation required: " + str(matrix[1][n - 1]))
    print_optiomal_solution(optimal_solution, 1, n - 1)


if __name__ == "__main__":
    main()
