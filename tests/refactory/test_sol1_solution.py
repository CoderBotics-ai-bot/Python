
import pytest


import math
from itertools import permutations
from project_euler.problem_041.sol1 import *


# `is_prime` and `solution` functions should be defined here
def is_prime(number: int) -> bool:
    if number == 1 or (number % 2 == 0 and number > 2):
        return False
    return all([(number % i) for i in range(3, int(math.sqrt(number)) + 1, 2)])


def solution(n: int = 7) -> int:
    pandigital_str = "".join(str(i) for i in range(1, n + 1))
    perm_list = [int("".join(i)) for i in permutations(pandigital_str, n)]
    pandigitals = [num for num in perm_list if is_prime(num)]
    return max(pandigitals) if pandigitals else 0


def test_solution():
    # Test with various values of n
    assert solution(2) == 0, "Expected max pandigital prime for length 2 to be 0"
    assert solution(4) == 4231, "Expected max pandigital prime for length 4 to be 4231"
    assert (
        solution(7) == 7652413
    ), "Expected max pandigital prime for length 7 to be 7652413"

    # Test with maximum possible n
    assert solution(9) == 0, "Expected max pandigital prime for length 9 to be 0"

    # Testing input outside valid range
    with pytest.raises(ValueError):
        solution(-3)
    with pytest.raises(ValueError):
        solution(0)
