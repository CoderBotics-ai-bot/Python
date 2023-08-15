import pytest
from data_structures.hashing.number_theory.prime_numbers import *


@pytest.mark.parametrize(
    "number, expected_result",
    [
        (0, False),  # Edge case: Lowest possible int
        (1, False),  # Edge case: not a prime number (has only one distinct factor)
        (2, True),  # Edge case: smallest prime number
        (3, True),  # Prime number
        (27, False),  # Not a prime number
        (563, True),  # Prime number
        (2999, True),  # Prime number
        (67483, False),  # Not a prime number
    ],
)
def test_is_prime(number, expected_result):
    assert is_prime(number) == expected_result
