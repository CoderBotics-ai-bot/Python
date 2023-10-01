import pytest
from matrix.cramers_rule_2x2 import *


import pytest


def test_cramers_rule_2x2():
    # Test cases where system of linear equations has a valid solution
    result = cramers_rule_2x2([2, 3, 0], [5, 1, 0])
    assert result is not None
    result = cramers_rule_2x2([0, 4, 50], [2, 0, 26])
    assert result is not None

    # Test cases where the system is inconsistent and has no solution
    with pytest.raises(ValueError, match="No solution."):
        cramers_rule_2x2([1, 2, 3], [2, 4, 7])

    # Test cases where two equations are the same causing an infinite number of solutions
    with pytest.raises(ValueError, match="Infinite solutions."):
        cramers_rule_2x2([1, 2, 3], [1, 2, 3])

    # Test cases where equation inputs are invalid
    with pytest.raises(ValueError, match="Please enter a valid equation."):
        cramers_rule_2x2([1, 2, 3], [11, 22])

    # Test edge case where both equations have a and b coefficients as zero, causing a ValueError
    with pytest.raises(ValueError, match="Both a & b of two equations can't be zero."):
        cramers_rule_2x2([0, 0, 6], [0, 0, 3])
