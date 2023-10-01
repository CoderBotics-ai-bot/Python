import pytest
from electronics.real_and_reactive_power import *


import pytest


def test_reactive_power_no_errors():
    apparent_power = 100
    power_factor = 0.9
    result = reactive_power(apparent_power, power_factor)
    assert result is not None


def test_reactive_power_zero_apparent_power():
    apparent_power = 0
    power_factor = 0.8
    result = reactive_power(apparent_power, power_factor)
    assert result == 0


def test_reactive_power_invalid_power_factor_type_str():
    apparent_power = 100
    power_factor = "string"
    with pytest.raises(ValueError):
        reactive_power(apparent_power, power_factor)


def test_reactive_power_invalid_power_factor_value_2():
    apparent_power = 100
    power_factor = 2
    with pytest.raises(ValueError):
        reactive_power(apparent_power, power_factor)


def test_reactive_power_invalid_power_factor_value_minus_2():
    apparent_power = 100
    power_factor = -2
    with pytest.raises(ValueError):
        reactive_power(apparent_power, power_factor)


def test_reactive_power_negative_power_factor():
    apparent_power = 100
    power_factor = -0.9
    result = reactive_power(apparent_power, power_factor)
    assert result is not None
