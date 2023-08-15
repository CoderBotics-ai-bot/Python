"""
Project Euler Problem 77: https://projecteuler.net/problem=77

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over
five thousand different ways?
"""
from __future__ import annotations

from functools import lru_cache
from math import ceil


from typing import Set

NUM_PRIMES = 100

primes = set(range(3, NUM_PRIMES, 2))
primes.add(2)
prime: int

for prime in range(3, ceil(NUM_PRIMES**0.5), 2):
    if prime not in primes:
        continue
    primes.difference_update(set(range(prime * prime, NUM_PRIMES, prime)))


@lru_cache(maxsize=100)
def partition(number_to_partition: int) -> Set[int]:
    """
    Returns a set of integers corresponding to unique prime partitions of a given number.

    Each unique prime partition can be represented as a unique prime decomposition.
    For example, (7+3) represents 7*3 = 21 and (3+3+2+2) represents 3*3*2*2 = 36

    Args:
        number_to_partition (int): The number to partition into prime numbers.

    Returns:
        Set[int]: A set of all unique prime decompositions of the input number.
    """
    if number_to_partition < 0:
        return set()
    elif number_to_partition == 0:
        return {1}

    return get_prime_partitions(number_to_partition, primes)


def solution(number_unique_partitions: int = 5000) -> int | None:
    """
    Return the smallest integer that can be written as the sum of primes in over
    m unique ways.
    >>> solution(4)
    10
    >>> solution(500)
    45
    >>> solution(1000)
    53
    """
    for number_to_partition in range(1, NUM_PRIMES):
        if len(partition(number_to_partition)) > number_unique_partitions:
            return number_to_partition
    return None

def get_prime_partitions(number: int, primes_set: set) -> set:
    """
    Calculate products of all unique prime partitions of the input number.

    Args:
        number (int): The number for which the partitions are to be calculated.
        primes_set (set): The set of prime numbers using which the partitions are to be generated

    Returns:
        set: A set of unique prime partitions of the input number.
    """

    if number in primes_set:
        prime_partitions = {number}
    else:
        prime_partitions = set()

    for prime in primes_set:
        if prime > number:
            break
        for partition in partition(number - prime):
            prime_partitions.add(partition * prime)

    return prime_partitions


if __name__ == "__main__":
    print(f"{solution() = }")
