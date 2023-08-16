import pytest
from project_euler.problem_009.sol1 import *


def test_solution():
    # Test normal functionality.
    assert solution() == 31875000

    # Test annotation
    assert solution.__annotations__ == {"return": int}

    # Check docstrings
    expected_docstring = (
        "\n"
        "    Returns the product of a,b,c which are Pythagorean Triplet that satisfies\n"
        "    the following:\n"
        "      1. a < b < c\n"
        "      2. a**2 + b**2 = c**2\n"
        "      3. a + b + c = 1000\n"
        "\n"
        "    >>> solution()\n"
        "    31875000\n"
        "    "
    )
    assert solution.__doc__ == expected_docstring
