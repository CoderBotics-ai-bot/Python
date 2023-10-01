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
    Perform matrix multiplication of two 2D lists.

    Args:
        matrix_a (list[list[int]]): 2D list of integers representing the first matrix to be multiplied.
        matrix_b (list[list[int]]): 2D list of integers representing the second matrix to be multiplied.

    Returns:
        list[list[int]]: A 2D list of integers resulting from the multiplication of 'matrix_a' and 'matrix_b'
    """

    def compute_element(i: int, j: int) -> int:
        """
        Compute the (i,j)th element of the resulting matrix from the multiplication.

        Args:
            i (int): The row index
            j (int): The column index

        Returns:
            int: The computed element.
        """
        return sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_a)))

    return [
        [compute_element(i, j) for j in range(len(matrix_a))]
        for i in range(len(matrix_a))
    ]


def identity(n: int) -> list[list[int]]:
    return [[int(row == column) for column in range(n)] for row in range(n)]

def nth_fibonacci_matrix(n: int) -> int:
    """
    Calculate the nth Fibonacci number using matrix exponentiation.

    This function calculates the nth Fibonacci number by raising a second-degree
    Fibonacci matrix to the nth power. It deals with negative inputs by immediately
    returning them, and optimizes for large positive inputs by applying the
    exponentiation by squaring method to the Fibonacci matrix.

    Args:
        n (int): The position in the Fibonacci sequence for which the respective
        Fibonacci number is to be calculated. For negative values, the function returns
        the input value.

    Returns:
        int: The nth Fibonacci number. For negative values of n, the function
        returns n.
    """
    # as the first two numbers are 0 and 1, so we can return the number itself for n <= 1
    if n <= 1:
        return n
    # the first two numbers are at position 0 and 1
    n = n - 1
    res_matrix = identity(2)
    fibonacci_matrix = [[1, 1], [1, 0]]
    res_matrix, fibonacci_matrix = fibonacci_helper(n, res_matrix, fibonacci_matrix)
    return res_matrix[0][0]


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


def fibonacci_helper(
    n: int, res_matrix: List[List[int]], fibonacci_matrix: List[List[int]]
) -> tuple:
    """
    Helper function to perform the square matrix multiplication to find Fibonacci number.

    This function multiplies the result matrix with fibonacci matrix for odd n, and double multiplies
    the fibonacci matrix then reduce n by half until n becomes zero.

    Args:
        n (int): The position in the Fibonacci sequence.
        res_matrix (list[list[int]]): The result matrix which store the fibonacci number.
        fibonacci_matrix (list[list[int]]): The matrix which represents the Fibonacci numbers.

    Returns:
        tuple: The result matrix and fibonacci matrix after all the operations done.
    """
    while n > 0:
        if n % 2 == 1:
            res_matrix = multiply(res_matrix, fibonacci_matrix)
        fibonacci_matrix = multiply(fibonacci_matrix, fibonacci_matrix)
        n = int(n / 2)
    return res_matrix, fibonacci_matrix


def main() -> None:
    """
    Test and compares the performance of the 'nth_fibonacci_matrix' and 'nth_fibonacci_bruteforce' functions.
    """
    for ordinal in "0th 1st 2nd 3rd 10th 100th 1000th".split():
        n = parse_ordinal_number(ordinal)
        print_fibonacci_results(n, nth_fibonacci_matrix(n), nth_fibonacci_bruteforce(n))
    # Uncomment these when running timing tests.
    # from timeit import timeit
    # print(timeit("nth_fibonacci_matrix(1000000)", "from main import nth_fibonacci_matrix", number=5))
    # print(timeit("nth_fibonacci_bruteforce(1000000)", "from main import nth_fibonacci_bruteforce", number=5))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

def parse_ordinal_number(ordinal_number: str) -> int:
    """
    Convert an ordinal number string (like "1st", "2nd") to an integer.

    Args:
        ordinal_number: String representing the ordinal number.

    Returns:
        Integer representation of the ordinal number.
    """
    return int("".join(c for c in ordinal_number if c in "0123456789"))


def print_fibonacci_results(
    n: int, nth_fibonacci_matrix: int, nth_fibonacci_bruteforce: int
) -> None:
    """
    Print the fibonacci results obtained by different methods.

    Args:
        n: Integer input for calculating fibonacci.
        nth_fibonacci_matrix: Result from the matrix method.
        nth_fibonacci_bruteforce: Result from the brute force method.
    """
    print(
        f"Fibonacci number for {n} using matrix exponentiation is {nth_fibonacci_matrix}"
        f" and using bruteforce is {nth_fibonacci_bruteforce}\n"
    )
