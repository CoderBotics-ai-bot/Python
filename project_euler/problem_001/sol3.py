"""
Project Euler Problem 1: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def solution(n: int = 1000) -> int:
    """
    Calculate the sum of all multiples of 3 or 5 below the given integer.

    This function leverages Python's built-in range function to generate a list of all multiples
    of 3 and 5 under the provided integer. Then, the sum of these multiples is calculated.

    Parameters:
    n (int): The upper bound to calculate the sum of multiples - default 1000.

    Returns:
    int: The sum of all multiples of 3 or 5 below the provided integer.

    Examples:
    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """
    multiples = [i for i in range(n) if i % 3 == 0 or i % 5 == 0]
    return sum(multiples)


if __name__ == "__main__":
    print(f"{solution() = }")
