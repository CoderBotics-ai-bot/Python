import pytest
from project_euler.problem_041.sol1 import *


def test_is_prime():
    """
    Tests method for verifying if a number is prime
    """
    # Test on edge case zero
    assert is_prime(0) == False, "Expected 0 not to be a prime number"

    # Test on edge case one
    assert is_prime(1) == False, "Expected 1 not to be a prime number"

    # Test on first prime number
    assert is_prime(2) == True, "Expected 2 to be a prime number"

    # Test on an odd number that is not prime
    assert is_prime(9) == False, "Expected 9 not to be a prime number"

    # Test on moderately large prime number
    assert is_prime(89) == True, "Expected 89 to be a prime number"

    # Test on large non-prime odd number
    assert is_prime(999) == False, "Expected 999 not to be a prime number"

    # Test on large non-prime even number
    assert is_prime(1000) == False, "Expected 1000 not to be a prime number"

    # Test on large prime number
    assert is_prime(23789) == True, "Expected 23789 to be a prime number"
