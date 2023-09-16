# https://en.m.wikipedia.org/wiki/Electric_power
from __future__ import annotations

from typing import NamedTuple


class Result(NamedTuple):
    name: str
    value: float

def electric_power(voltage: float, current: float, power: float) -> Result:
    """
    Function to calculate the missing value out of Voltage, Current, and Power.
    Given two of these values, the function will calculate the third one.
    This is based on the fundamental of electrical power calculation.
    Power(P) = Voltage(V) * Current(I)

    Args:
        voltage (float): The voltage in volts. If unknown, input 0.
        current (float): The current in amperes. If unknown, input 0.
        power (float): The power in watts. If unknown, input 0.

    Returns:
        Result: NamedTuple containing the name of the calculated parameter (voltage, current or power) and its calculated value.

    Raises:
        ValueError: Raises an exception when more than one or none argument is 0.
        ValueError: Raises an exception when power is negative.

    Examples:
        >>> electric_power(voltage=0, current=2, power=5)
        Result(name='voltage', value=2.5)
        >>> electric_power(voltage=2, current=0, power=4)
        Result(name='current', value=2.0)
        >>> electric_power(voltage=2, current=2, power=0)
        Result(name='power', value=4.0)
    """
    check_input_validity(voltage, current, power)
    if voltage == 0:
        return Result("voltage", safe_division(power, current))
    if current == 0:
        return Result("current", safe_division(power, voltage))
    if power == 0:
        return Result("power", round(abs(voltage * current), 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def check_input_validity(voltage: float, current: float, power: float):
    """
    Function to check the validity of the input parameters.

    Args:
        voltage (float): The voltage in volts.               If unknown, input 0.
        current (float): The current in amperes.             If unknown, input 0.
        power (float): The power in watts.                   If unknown, input 0.

    Raises:
        ValueError: Raises an exception when more than one or none argument is 0.
        ValueError: Raises an exception when power is negative. If power is negative.
    """
    if (voltage, current, power).count(0) != 1:
        raise ValueError("Only one argument must be 0")
    if power < 0:
        raise ValueError(
            "Power cannot be negative in any electrical/electronics system"
        )


def safe_division(num1: float, num2: float) -> float:
    """
    Performs division of two numbers with error handling.
    Args:
        num1 (float): Numerator.
        num2 (float): Denominator.
    Returns:
        float: Result of division.
    Raises:
        ValueError: If the denominator is zero.
    """
    if num2 == 0:
        raise ValueError("Division by Zero is not allowed")
    return round(num1 / num2, 2)
