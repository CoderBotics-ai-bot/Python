"""
Project Euler Problem 10: https://projecteuler.net/problem=10

Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""
import math
from collections.abc import Iterator
from itertools import takewhile

def is_prime(number: int) -> bool:
    """
    Checks if a given number is a prime number. A prime number is a natural number greater
    than 1 that is not a product of two smaller natural numbers.

    Args:
        number(int): The number to check for primality.

    Returns:
        bool: True if the number is a prime number, False if not.
    """
    if number < 2 or any(number % i == 0 for i in range(2, int(math.sqrt(number) + 1))):
        return False
    return True


def prime_generator() -> Iterator[int]:
    """
    Generate a list sequence of prime numbers
    """

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def solution(n: int = 2000000) -> int:
    """
    Returns the sum of all the primes below n.

    >>> solution(1000)
    76127
    >>> solution(5000)
    1548136
    >>> solution(10000)
    5736396
    >>> solution(7)
    10
    """

    return sum(takewhile(lambda x: x < n, prime_generator()))


if __name__ == "__main__":
    print(f"{solution() = }")
