from maths.hardy_ramanujanalgo import *
import pytest


def test_exact_prime_factor_count():
    # test with prime number should return 1
    assert exact_prime_factor_count(19) == 1
    # test with number that has multiple of same prime numbers should return 1
    assert exact_prime_factor_count(8) == 1
    # test with number that has different prime numbers should return count of different prime numbers
    assert exact_prime_factor_count(24) == 2
    # test with odd number
    assert exact_prime_factor_count(15) == 2
    # test with 1, should return 0
    assert exact_prime_factor_count(1) == 0
