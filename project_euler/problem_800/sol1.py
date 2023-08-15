"""
Project Euler Problem 800: https://projecteuler.net/problem=800

An integer of the form p^q q^p with prime numbers p != q is called a hybrid-integer.
For example, 800 = 2^5 5^2 is a hybrid-integer.

We define C(n) to be the number of hybrid-integers less than or equal to n.
You are given C(800) = 2 and C(800^800) = 10790

Find C(800800^800800)
"""

from math import isqrt, log2
from typing import List


from typing import List
from math import isqrt


def calculate_prime_numbers(max_number: int) -> List[int]:
    """
    Returns a list of prime numbers up to the given maximum number.

    Args:
    max_number (int): The upper limit for generating prime numbers. Only numbers below this value will be generated.

    Returns:
    List[int]: A list of prime numbers less than the max_number.
    """

    is_prime = [True] * max_number
    upper_bound = isqrt(max_number - 1) + 1

    for number in range(2, upper_bound):
        if is_prime[number]:
            _mark_multiples_as_non_prime(is_prime, number, max_number)

    return _generate_prime_numbers(is_prime, max_number)


def solution(base: int = 800800, degree: int = 800800) -> int:
    """
    Returns the number of hybrid-integers less than or equal to base^degree

    >>> solution(800, 1)
    2

    >>> solution(800, 800)
    10790
    """

    upper_bound = degree * log2(base)
    max_prime = int(upper_bound)
    prime_numbers = calculate_prime_numbers(max_prime)

    hybrid_integers_count = 0
    left = 0
    right = len(prime_numbers) - 1
    while left < right:
        while (
            prime_numbers[right] * log2(prime_numbers[left])
            + prime_numbers[left] * log2(prime_numbers[right])
            > upper_bound
        ):
            right -= 1
        hybrid_integers_count += right - left
        left += 1

    return hybrid_integers_count



def _mark_multiples_as_non_prime(
    is_prime: List[bool], prime: int, max_number: int
) -> None:
    """
    Mark all multiples of a given "prime" number as non-prime (False).
    Mutates the provided "is_prime" list.

    Args:
    is_prime (List[bool]): List denoting which indices are prime.
    prime (int): Prime number used to mark its multiples as non-prime.
    max_number (int): Max number up to which primes are checked.

    Returns:
    This function does not return anything, It modifies the 'is_prime' list in-place.

    """
    for i in range(prime**2, max_number, prime):
        is_prime[i] = False


def _generate_prime_numbers(is_prime: List[bool], max_number: int) -> List[int]:
    """
    Generate a list of prime numbers based on given 'is_prime' list.

    Args:
    is_prime (List[bool]): List denoting which indices are prime.
    max_number (int): Max number up to which primes are checked.

    Returns:
    List of prime numbers.
    """
    return [i for i in range(2, max_number) if is_prime[i]]


if __name__ == "__main__":
    print(f"{solution() = }")
