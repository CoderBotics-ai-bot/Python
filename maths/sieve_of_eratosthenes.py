"""
Sieve of Eratosthones

The sieve of Eratosthenes is an algorithm used to find prime numbers, less than or
equal to a given value.
Illustration:
https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif
Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

doctest provider: Bruno Simas Hadlich (https://github.com/brunohadlich)
Also thanks to Dmitry (https://github.com/LizardWizzard) for finding the problem
"""
from __future__ import annotations

import math


def prime_sieve(num: int) -> list[int]:
    """
    Generate all prime numbers up to a given number.

    Args:
        num (int): The upper limit for prime number generation.

    Returns:
        list[int]: A list containing all prime numbers up to the input number 'num'.

    Raises:
        ValueError: If the input number is less than or equal to 0.
    """
    if num <= 0:
        msg = f"{num}: Invalid input, please enter a positive integer."
        raise ValueError(msg)

    sieve = [True] * (num + 1)
    end = int(math.sqrt(num))

    for start in range(2, end + 1):
        if sieve[start] is True:
            sieve = mark_multiples(sieve, num, start)

    prime = append_primes(sieve, end + 1, num)

    return prime


if __name__ == "__main__":
    print(prime_sieve(int(input("Enter a positive integer: ").strip())))



def mark_multiples(sieve: list[bool], num: int, start: int) -> list[bool]:
    """
    Mark multiples of a given number within the sieve list as False

    Args:
        sieve (list[bool]): The sieve list to be modified
        num (int): Total numbers used for sieve
        start (int): The starting number from which multiples will be marked as False

    Returns:
        list[bool]: The updated sieve list
    """
    for i in range(start * start, num + 1, start):
        if sieve[i] is True:
            sieve[i] = False
    return sieve


def append_primes(sieve: list[bool], start: int, end: int) -> list[int]:
    """
    Append all primes (i.e., True values) within a range into a list

    Args:
        sieve (list[bool]): The sieve list to use for checking primes
        start (int): The starting number from which to check for primes
        end (int): The ending number until which to check for primes

    Returns:
        list[int]: List of primes within the given range
    """
    prime = []
    for num in range(start, end + 1):
        if sieve[num] is True:
            prime.append(num)
    return prime
