import pytest
from matrix.cramers_rule_2x2 import *


def test_cramers_rule_2x2_unique_sol():
    assert cramers_rule_2x2([2, 3, 0], [5, 1, 0]) == (0.0, 0.0)
    assert cramers_rule_2x2([0, 4, 50], [2, 0, 26]) == (13.0, 12.5)
    assert cramers_rule_2x2([11, 2, 30], [1, 0, 4]) == (4.0, -7.0)
    assert cramers_rule_2x2([4, 7, 1], [1, 2, 0]) == (2.0, -1.0)


def test_cramers_rule_2x2_infinite_sol():
    with pytest.raises(ValueError):
        cramers_rule_2x2([1, 2, 3], [2, 4, 6])

    with pytest.raises(ValueError):
        cramers_rule_2x2([1, 2, 3], [1, 2, 3])


def test_cramers_rule_2x2_no_sol():
    with pytest.raises(ValueError):
        cramers_rule_2x2([1, 2, 3], [2, 4, 7])

    with pytest.raises(ValueError):
        cramers_rule_2x2([0, 1, 6], [0, 0, 3])

    with pytest.raises(ValueError):
        cramers_rule_2x2([0, 4, 50], [0, 3, 99])


def test_cramers_rule_2x2_invalid_equation():
    with pytest.raises(ValueError):
        cramers_rule_2x2([1, 2, 3], [11, 22])


def test_cramers_rule_2x2_all_zero():
    with pytest.raises(ValueError):
        cramers_rule_2x2([0, 0, 6], [0, 0, 3])
