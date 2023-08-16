# https://en.wikipedia.org/wiki/Ohm%27s_law
from __future__ import annotations

def ohms_law(voltage: float, current: float, resistance: float) -> dict[str, float]:
    """
    Given two electrical values and a zero, calculate the missing value using Ohm's Law.

    Ohm's Law states:
    V = I * R
    Where:
    V = voltage
    I = current
    R = resistance

    Calculate the missing value when given the other two and precisely one of the inputs is 0.

    Args:
        voltage (float):  Voltage in volts. Set to 0 if unknown.
        current (float):  Current in amperes. Set to 0 if unknown.
        resistance (float): Resistance in ohms. Set to 0 if unknown.

    Returns:
        dict[str, float]: A dictionary containing the name and value of the calculated electrical property.

    Raises:
        ValueError: If more than one or no inputs are 0.
        ValueError: If a negative resistance value is passed.

    Examples:
        >>> ohms_law(voltage=10, resistance=5, current=0)
        {'current': 2.0}
        >>> ohms_law(voltage=0, current=0, resistance=10)
        Traceback (most recent call last):
            ...
        ValueError: One and only one argument must be 0
        >>> ohms_law(voltage=0, current=1, resistance=-2)
        Traceback (most recent call last):
            ...
        ValueError: Resistance cannot be negative
    """
    if (voltage, current, resistance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if resistance < 0:
        raise ValueError("Resistance cannot be negative")
    if voltage == 0:
        return {"voltage": float(current * resistance)}
    elif current == 0:
        return {"current": voltage / resistance}
    elif resistance == 0:
        return {"resistance": voltage / current}
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
