#!/usr/bin/env python3
"""
    module to operations with prime numbers
"""

import math

def is_prime(number: int) -> bool:
    """
    Check if the provided number is a prime number.

    A prime number (or a prime) is a natural number greater
    than 1 that is not a product of two smaller natural numbers.
    In other words, it is a number that has exactly two distinct
    natural number divisors: 1 and itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a prime number, otherwise False.

    Raises:
        AssertionError: If the input is not a positive integer.

    Examples:
        >>> is_prime(0)
        False
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(27)
        False
        >>> is_prime(87)
        False
        >>> is_prime(563)
        True
        >>> is_prime(2999)
        True
        >>> is_prime(67483)
        False

    """
    assert isinstance(number, int) and (
        number >= 0
    ), "'number' must been an int and positive"

    if 1 < number < 4:
        return True
    elif number < 2 or not number % 2:
        return False

    odd_numbers = range(3, int(math.sqrt(number) + 1), 2)
    return not any(not number % i for i in odd_numbers)


def next_prime(value, factor=1, **kwargs):
    value = factor * value
    first_value_val = value

    while not is_prime(value):
        value += 1 if not ("desc" in kwargs and kwargs["desc"] is True) else -1

    if value == first_value_val:
        return next_prime(value + 1, **kwargs)
    return value
