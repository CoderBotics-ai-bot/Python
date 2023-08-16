
import pytest
from math import isclose
from maths.binomial_distribution import *


from math import isclose


@pytest.mark.parametrize(
    "successes, trials, prob, expected",
    [
        (3, 5, 0.7, 0.30870000000000003),
        (2, 4, 0.5, 0.375),
        (0, 1, 0.5, 0.5),
        (1, 1, 0.5, 0.5),
        (100, 100, 0.5, 7.888609052210118e-31),
    ],
)
def test_binomial_distribution(successes, trials, prob, expected):
    assert isclose(
        binomial_distribution(successes, trials, prob), expected, rel_tol=1e-9
    )


def test_binomial_distribution_with_successes_greater_than_trials():
    with pytest.raises(ValueError, match=r"successes must be lower or equal to trials"):
        binomial_distribution(6, 5, 0.7)


def test_binomial_distribution_with_negative_successes():
    with pytest.raises(
        ValueError, match=r"the function is defined for non-negative integers"
    ):
        binomial_distribution(-3, 5, 0.7)


def test_binomial_distribution_with_successes_or_trials_as_non_integer():
    with pytest.raises(
        ValueError, match=r"the function is defined for non-negative integers"
    ):
        binomial_distribution(3.5, 5, 0.7)

    with pytest.raises(
        ValueError, match=r"the function is defined for non-negative integers"
    ):
        binomial_distribution(3, 5.5, 0.7)


def test_binomial_distribution_with_prob_not_in_range_1_0():
    with pytest.raises(ValueError, match=r"prob has to be in range of 1 - 0"):
        binomial_distribution(3, 5, 1.7)

    with pytest.raises(ValueError, match=r"prob has to be in range of 1 - 0"):
        binomial_distribution(3, 5, -0.5)
