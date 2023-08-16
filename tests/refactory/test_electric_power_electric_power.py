import pytest
from electronics.electric_power import *


def test_electric_power_voltage_zero():
    assert electric_power(voltage=0, current=2, power=5) == Result(
        name="voltage", value=2.5
    )


def test_electric_power_power_zero():
    assert electric_power(voltage=2, current=2, power=0) == Result(
        name="power", value=4.0
    )


def test_electric_power_power_zero_with_negative_voltage():
    assert electric_power(voltage=-2, current=3, power=0) == Result(
        name="power", value=6.0
    )


def test_electric_power_all_non_zero_values():
    with pytest.raises(ValueError, match="Only one argument must be 0"):
        electric_power(voltage=2, current=4, power=2)


def test_electric_power_all_zero_values():
    with pytest.raises(ValueError, match="Only one argument must be 0"):
        electric_power(voltage=0, current=0, power=0)


def test_electric_power_negative_power():
    with pytest.raises(
        ValueError,
        match="Power cannot be negative in any electrical/electronics system",
    ):
        electric_power(voltage=0, current=2, power=-4)


def test_electric_power_power_zero_with_float_values():
    assert electric_power(voltage=2.2, current=2.2, power=0) == Result(
        name="power", value=4.84
    )
