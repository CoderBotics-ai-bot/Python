# https://en.m.wikipedia.org/wiki/Electric_power
from __future__ import annotations

from typing import NamedTuple


class Result(NamedTuple):
    name: str
    value: float


def electric_power(voltage: float, current: float, power: float) -> Result:
    validate_arguments(voltage, current, power)

    if voltage == 0:
        return calculate_voltage(power, current)
    if current == 0:
        return calculate_current(power, voltage)
    if power == 0:
        return calculate_power(voltage, current)


if __name__ == "__main__":
    import doctest

    doctest.testmod()



def validate_arguments(voltage: float, current: float, power: float) -> None:
    if (voltage, current, power).count(0) != 1:
        raise ValueError("Only one argument must be 0")
    if power < 0:
        raise ValueError(
            "Power cannot be negative in any electrical/electronics system"
        )


def calculate_voltage(power: float, current: float) -> Result:
    return Result("voltage", power / current)


def calculate_current(power: float, voltage: float) -> Result:
    return Result("current", power / voltage)


def calculate_power(voltage: float, current: float) -> Result:
    return Result("power", float(round(abs(voltage * current), 2)))
