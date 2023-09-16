"""
Implementation of finding nth fibonacci number using matrix exponentiation.
Time Complexity is about O(log(n)*8), where 8 is the complexity of matrix
multiplication of size 2 by 2.
And on the other hand complexity of bruteforce solution is O(n).
As we know
    f[n] = f[n-1] + f[n-1]
Converting to matrix,
    [f(n),f(n-1)] = [[1,1],[1,0]] * [f(n-1),f(n-2)]
->  [f(n),f(n-1)] = [[1,1],[1,0]]^2 * [f(n-2),f(n-3)]
    ...
    ...
->  [f(n),f(n-1)] = [[1,1],[1,0]]^(n-1) * [f(1),f(0)]
So we just need the n times multiplication of the matrix [1,1],[1,0]].
We can decrease the n times multiplication by following the divide and conquer approach.
"""


from typing import List

def multiply(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    """
    Multiplies two matrices matrix_a and matrix_b.

    The multiplication is performed element wise by taking the scalar
    product of each row of matrix_a with each column of matrix_b.

    Args:
        matrix_a (list[list[int]]): The first matrix for the multiplication operation.
            It's a 2D list of integers where each list represents a row in the matrix.
        matrix_b (list[list[int]]): The second matrix for the multiplication operation.
            It's a 2D list of integers where each list represents a row in the matrix.

    Returns:
        result (list[list[int]]): The result of multiplying both matrices.
            It's a 2D list of integers where each list represents a row in the new matrix.

    Note:
        - The function assumes that both matrices have the same dimensions.
        - The function does not check for the validity of the input.
    """
    matrix_size = len(matrix_a)
    result = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

    for i in range(matrix_size):
        for j in range(matrix_size):
            result[i][j] = sum(
                matrix_a[i][k] * matrix_b[k][j] for k in range(matrix_size)
            )

    return result


def identity(n: int) -> list[list[int]]:
    return [[int(row == column) for column in range(n)] for row in range(n)]

def nth_fibonacci_matrix(n: int) -> int:
    """
    Calculate the nth term of the Fibonacci sequence using the matrix exponentiation method.

    Args:
        n (int): The position of the term in the Fibonacci sequence to calculate.

    Returns:
        int: The nth term of the Fibonacci sequence.

    Raises:
        ValueError: If `n` is less than 0.
    """

    def matrix_power(matrix: List[List[int]], exponent: int) -> List[List[int]]:
        """
        Compute power of a matrix.

        Args:
            matrix (list): The input matrix.
            exponent (int): The exponent to raise the matrix to.

        Returns:
            list: The resulting matrix after raising it to the given exponent.
        """
        result = identity(2)
        while exponent > 0:
            if exponent % 2 == 1:
                result = multiply(result, matrix)
            matrix = multiply(matrix, matrix)
            exponent = exponent // 2
        return result

    if n < 0:
        raise ValueError("Argument `n` must be greater than or equal to 0.")

    if n <= 1:
        return n

    fibonacci_matrix = [[1, 1], [1, 0]]
    fibonacci_matrix = matrix_power(fibonacci_matrix, n - 1)
    return fibonacci_matrix[0][0]


def nth_fibonacci_bruteforce(n: int) -> int:
    """
    >>> nth_fibonacci_bruteforce(100)
    354224848179261915075
    >>> nth_fibonacci_bruteforce(-100)
    -100
    """
    if n <= 1:
        return n
    fib0 = 0
    fib1 = 1
    for _ in range(2, n + 1):
        fib0, fib1 = fib1, fib0 + fib1
    return fib1

def main() -> None:
    """
    Main method to display comparison between `nth_fibonacci_matrix` and `nth_fibonacci_bruteforce`.
    Comparison is performed for various Fibonacci terms and execution speed.
    Fibonacci terms include: 0th, 1st, 2nd, 3rd, 10th, 100th, 1000th.
    """
    for ordinal in extract_ordinal_numbers():
        compute_and_display_comparison(ordinal)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()


def extract_ordinal_numbers() -> List[str]:
    """
    Helper function to Extract Ordinal Numbers
    """
    return "0th 1st 2nd 3rd 10th 100th 1000th".split()


def compute_and_display_comparison(ordinal: str) -> None:
    """
    Helper function to Compute and Display Comparison
    """
    n = convert_ordinal_to_int(ordinal)
    matrix_result = nth_fibonacci_matrix(n)
    bruteforce_result = nth_fibonacci_bruteforce(n)
    print(
        f"{ordinal} fibonacci number using matrix exponentiation is "
        f"{matrix_result} and using bruteforce is "
        f"{bruteforce_result}\n"
    )


def convert_ordinal_to_int(ordinal: str) -> int:
    """
    Helper function to Convert Ordinal to Integer.
    """
    return int("".join(c for c in ordinal if c in "0123456789"))  # 1000th --> 1000
