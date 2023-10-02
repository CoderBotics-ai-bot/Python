"""
Problem source: https://www.hackerrank.com/challenges/the-power-sum/problem
Find the number of ways that a given integer X, can be expressed as the sum
of the Nth powers of unique, natural numbers. For example, if X=13 and N=2.
We have to find all combinations of unique squares adding up to 13.
The only solution is 2^2+3^2. Constraints: 1<=X<=1000, 2<=N<=10.
"""

from math import pow

def backtrack(
    needed_sum: int,
    power: int,
    current_number: int,
    current_sum: int,
    solutions_count: int,
) -> tuple[int, int]:
    """
    Find the count of solutions wherein the sum of the powers
    of the consecutive non-negative integers starting from current_number
    is equal to needed_sum.
    This function uses backtracking to find the above mentioned solutions.
    """
    # Solution is found, increment solutions_count and backtrack
    if current_sum == needed_sum:
        return current_sum, solutions_count + 1

    # Calculate power of the current number
    i_to_n = pow(current_number, power)

    # If current_sum with current number's power is still not greater than needed_sum, proceed and add the number's power to current_sum
    if current_sum + i_to_n <= needed_sum:
        _, solutions_count = backtrack(
            needed_sum, power, current_number + 1, current_sum + i_to_n, solutions_count
        )

    # Regardless of the above condition, if current number's power is still less than needed_sum, proceed without adding the number's power to current_sum
    if i_to_n < needed_sum:
        _, solutions_count = backtrack(
            needed_sum, power, current_number + 1, current_sum, solutions_count
        )

    return current_sum, solutions_count


def solve(needed_sum: int, power: int) -> int:
    """
    >>> solve(13, 2)
    1
    >>> solve(100, 2)
    3
    >>> solve(100, 3)
    1
    >>> solve(800, 2)
    561
    >>> solve(1000, 10)
    0
    >>> solve(400, 2)
    55
    >>> solve(50, 1)
    Traceback (most recent call last):
        ...
    ValueError: Invalid input
    needed_sum must be between 1 and 1000, power between 2 and 10.
    >>> solve(-10, 5)
    Traceback (most recent call last):
        ...
    ValueError: Invalid input
    needed_sum must be between 1 and 1000, power between 2 and 10.
    """
    if not (1 <= needed_sum <= 1000 and 2 <= power <= 10):
        raise ValueError(
            "Invalid input\n"
            "needed_sum must be between 1 and 1000, power between 2 and 10."
        )

    return backtrack(needed_sum, power, 1, 0, 0)[1]  # Return the solutions_count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
