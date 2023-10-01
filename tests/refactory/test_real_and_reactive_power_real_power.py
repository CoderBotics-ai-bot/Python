import pytest
from electronics.real_and_reactive_power import *


def test_real_power_no_errors():
    """Test the function real_power for basic functionality."""
    assert real_power(100, 0.9) is not None


def test_real_power_negative_power_factor():
    """Test the function real_power with negative power factor."""
    assert real_power(100, -0.9) == -90.0


def test_real_power_zero_apparent_power():
    """Test the function real_power with zero apparent power."""
    assert real_power(0, 0.8) == 0.0


def test_real_power_invalid_power_factor_type_str():
    """Test the function real_power with a string as power factor."""
    with pytest.raises(ValueError):
        real_power(100, "0.9")


def test_real_power_invalid_power_factor_value_2():
    """Test the function real_power with a power factor greater than 1"""
    with pytest.raises(ValueError):
        real_power(100, 2)


def test_real_power_invalid_power_factor_value_minus_2():
    """Test the function real_power with a power factor less than -1"""
    with pytest.raises(ValueError):
        real_power(100, -2)
