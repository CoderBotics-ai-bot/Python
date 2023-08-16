# https://en.m.wikipedia.org/wiki/Electric_power
from __future__ import annotations

from typing import NamedTuple


class Result(NamedTuple):
    name: str
    value: float



def electric_power(voltage: float, current: float, power: float) -> Result:
    """
    This function calculates either voltage, current or power depending on the input parameters
    where exactly one of them should be 0.

    Args:
        - voltage (float): The electrical voltage. Set this to 0 if voltage is the value to be calculated.
        - current (float): The electrical current. Set this to 0 if current is the value to be calculated.
        - power (float): The electrical power. Set this to 0 if power is the value to be calculated.

    Returns:
        Result: NamedTuple with "name" being the name of the calculated field and
                "value" being the calculated value.

    Examples:
        >>> electric_power(voltage=0, current=2, power=5)
        Result(name='voltage', value=2.5)
        >>> electric_power(voltage=2, current=2, power=0)
        Result(name='power', value=4.0)
        >>> electric_power(voltage=-2, current=3, power=0)
        Result(name='power', value=6.0)

    Raises:
        ValueError: If less than or more than one argument is set to 0.
        ValueError: If power is set to a negative value even if it is the value to be calculated.

    """
    if (voltage, current, power).count(0) != 1:
        raise ValueError("Exactly one argument must be set to 0.")
    elif power < 0:
        raise ValueError(
            "Power cannot be negative in any electrical/electronics system."
        )
    elif voltage == 0:
        return Result("voltage", power / current)
    elif current == 0:
        return Result("current", power / voltage)
    elif power == 0:
        return Result("power", round(abs(voltage * current), 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
