"""
Project Euler Problem 7: https://projecteuler.net/problem=7

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10001st prime number?

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""

from math import sqrt

def is_prime(number: int) -> bool:
    """
    Checks if a given number is prime.

    Args:
        number: The number to be checked for primality.

    Returns:
        True if the number is prime, else False.
    """
    if number < 4:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    return is_not_factor_present(number)


def solution(nth: int = 10001) -> int:
    """
    Returns the n-th prime number.

    >>> solution(6)
    13
    >>> solution(1)
    2
    >>> solution(3)
    5
    >>> solution(20)
    71
    >>> solution(50)
    229
    >>> solution(100)
    541
    """

    count = 0
    number = 1
    while count != nth and number < 3:
        number += 1
        if is_prime(number):
            count += 1
    while count != nth:
        number += 2
        if is_prime(number):
            count += 1
    return number


def is_not_factor_present(number: int) -> bool:
    """
    Checks if a there exists a factor for the given number.

    Args:
        number: The number to be checked for its factors

    Returns:
        False if factor exists else True
    """
    check_limit = int(sqrt(number) + 1)
    return all(
        number % i
        for i in range(5, check_limit, 6)
        if number % i == 0 or number % (i + 2) == 0
    )


if __name__ == "__main__":
    print(f"{solution() = }")
