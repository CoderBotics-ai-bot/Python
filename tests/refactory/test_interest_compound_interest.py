from financial.interest import *
import pytest


def test_compound_interest_no_error():
    """Test compound_interest with standard values, checks for no errors"""
    result = compound_interest(10000.0, 0.05, 3)
    assert result is not None


def test_compound_interest_negative_principal():
    """Test compound_interest with negative principal value, expects ValueError"""
    with pytest.raises(ValueError):
        compound_interest(-5500.0, 0.01, 5)


def test_compound_interest_negative_interest_rate():
    """Test compound_interest with negative interest rate, expects ValueError"""
    with pytest.raises(ValueError):
        compound_interest(10000.0, -3.5, 3.0)


def test_compound_interest_negative_periods():
    """Test compound_interest with negative number of compounding periods, expects ValueError"""
    with pytest.raises(ValueError):
        compound_interest(10000.0, 0.06, -4)
