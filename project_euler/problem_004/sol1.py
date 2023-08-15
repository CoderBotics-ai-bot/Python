"""
Project Euler Problem 4: https://projecteuler.net/problem=4

Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

References:
    - https://en.wikipedia.org/wiki/Palindromic_number
"""


def solution(n: int = 998001) -> int:
    """
    Returns the largest palindrome made from the product of two 3-digit numbers which is less than n.

    Args:
    n: An integer, representing the upper limit for palindrome search. Defaults to 998001.

    Returns:
    The largest palindrome number, made from the product of two 3-digit numbers which is less than n.

    Raises:
    ValueError: If n is larger than the maximum possible 3 digit number's product.

    Examples:
    >>> solution(20000)
    19591
    >>> solution(30000)
    29992
    >>> solution(40000)
    39893
    >>> solution(10000)
    ValueError: That number is larger than our acceptable range.
    """
    if n > 998001:
        raise ValueError("That number is larger than our acceptable range.")

    for number in range(n - 1, 9999, -1):
        str_number = str(number)

        if str_number == str_number[::-1] and is_three_digit_product(number):
            return number
    return None


if __name__ == "__main__":
    print(f"{solution() = }")

def is_three_digit_product(number: int) -> bool:
    """
    Determine if a number is a product of two 3-digit numbers

    Args:
    number: An integer to be checked

    Returns:
    A boolean value representing whether the number is a product of two 3-digit numbers or not.
    """
    divisor = 999
    while divisor > 99:
        if (number % divisor == 0) and (99 < number // divisor < 1000):
            return True
        divisor -= 1
    return False
