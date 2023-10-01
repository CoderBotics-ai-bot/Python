from financial.interest import *
import pytest


def test_simple_interest_no_error():
    """The most important test. Run the function with default parameters and check if it doesn't throw and errors."""
    result = simple_interest(18000.0, 0.06, 3)
    assert result is not None, "The function should return a value"


def test_simple_interest_zero_interest_rate():
    """Test when the interest rate is 0.0."""
    result = simple_interest(18000.0, 0.0, 3)
    assert result == 0.0


def test_simple_interest_negative_days_between_payments():
    """Test when the days_between_payments is negative."""
    with pytest.raises(ValueError):
        simple_interest(5500.0, 0.01, -5)


def test_simple_interest_negative_rate():
    """Test when the daily_interest_rate is negative."""
    with pytest.raises(ValueError):
        simple_interest(10000.0, -0.06, 3)


def test_simple_interest_negative_principal():
    """Test when the principal is negative."""
    with pytest.raises(ValueError):
        simple_interest(-10000.0, 0.06, 3)
