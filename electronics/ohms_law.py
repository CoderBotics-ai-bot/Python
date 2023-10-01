# https://en.wikipedia.org/wiki/Ohm%27s_law
from __future__ import annotations


def ohms_law(voltage: float, current: float, resistance: float) -> dict[str, float]:
    """
    Apply the Ohm's Law.

    Calculate and return the unknown electrical quantity which can be voltage, current, or resistance.

    Args:
        voltage (float): The voltage value.
        current (float): The current value.
        resistance (float): The resistance value.

    Returns:
        dict[str; float]: A dictionary with the name and the value of the calculated electrical quantity.

    Raises:
        ValueError: If more than one or no arguments are set to 0.
        ValueError: If the resistance input is negative.
    """
    _raise_error_if_incorrect_input(voltage, current, resistance)

    if voltage == 0:
        return {"voltage": current * resistance}
    if current == 0:
        return {"current": voltage / resistance}
    return {"resistance": voltage / current}


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def _raise_error_if_incorrect_input(
    voltage: float, current: float, resistance: float
) -> None:
    """
    Check if the input to ohms_law function is correct.

    Raise a ValueError if:

    - More than one or no arguments are set to 0.
    - The resistance input is negative.

    Args:
        voltage (float): The voltage value.
        current (float): The current value.
        resistance (float): The resistance value.

    Returns:


    Raises:
        ValueError: If more than one or no arguments are set to 0.
        ValueError: If the resistance input is negative.
    """
    if (voltage, current, resistance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if resistance < 0:
        raise ValueError("Resistance cannot be negative")
