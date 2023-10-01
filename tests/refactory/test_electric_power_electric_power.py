from electronics.electric_power import *
import pytest


import pytest


def test_electric_power_no_errors():
    """
    Ensure that the function does not throw errors when provided with valid arguments
    and returns a non-None value.
    """
    voltage = 2.2
    current = 2.2
    power = 0
    result = electric_power(voltage, current, power)
    assert result is not None


def test_electric_power_voltage_zero():
    """
    Testing when the voltage is zero.
    """
    voltage = 0
    current = 2
    power = 5
    result = electric_power(voltage, current, power)
    assert result.name == "voltage"
    assert result.value == 2.5


def test_electric_power_current_zero():
    """
    Testing when the current is zero.
    """
    voltage = 2
    current = 0
    power = 4
    result = electric_power(voltage, current, power)
    assert result.name == "current"
    assert result.value == 2


def test_electric_power_power_zero():
    """
    Testing when the power is zero.
    """
    voltage = 2
    current = 2
    power = 0
    result = electric_power(voltage, current, power)
    assert result.name == "power"
    assert result.value == 4


def test_electric_power_invalid_values():
    """
    Testing when the inputs are invalid.
    """
    with pytest.raises(ValueError, match=r"Only one argument must be 0"):
        electric_power(2, 2, 2)
    with pytest.raises(
        ValueError,
        match=r"Power cannot be negative in any electrical/electronics system",
    ):
        electric_power(0, 2, -4)
