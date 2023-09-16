# https://en.wikipedia.org/wiki/Ohm%27s_law
from __future__ import annotations


from typing import List


def ohms_law(voltage: float, current: float, resistance: float) -> dict[str, float]:
    """
    Calculate the unknown electrical quantity (voltage, current, or resistance) using Ohm's Law.

    This method follows Ohm's law formula that connects voltage (U), current (I) and resistance (R).
    In order to use this method, exactly one of the parameters (voltage, current, resistance) should be equal to 0.
    The method then calculates the value of the zero parameter.

    Ohm's Law is as follows:
    U = I * R
    where:
    U = Voltage (in volts),
    I = Current (in amperes),
    R = Resistance (in ohms)

    Args:
        voltage (float): The voltage in Volts.
        current (float): The current in Amperes.
        resistance (float): The resistance in ohms.

    Returns:
        dict[str, float]: The unknown (input 0) quantity with its calculated value.

    Raises:
        ValueError: If none or more than one arguments are 0.
        ValueError: If resistance is less than zero.

    Example:
        ohms_law(voltage=10, current=0, resistance=5)
        >>> {'current': 2.0}
    """

    validate_parameters([voltage, current, resistance])

    if voltage == 0:
        return {"voltage": float(current * resistance)}
    if current == 0:
        return {"current": voltage / resistance}
    if resistance == 0:
        return {"resistance": voltage / current}


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def validate_parameters(parameters: List[float]) -> None:
    """
    Validates the parameters for the ohms_law function.

    Args:
        parameters (List[float]): The parameters for the ohms_law function.

    Raises:
        ValueError: If none or more than one arguments are 0.
        ValueError: If resistance is less than zero.
    """
    if parameters.count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if parameters[2] < 0:
        raise ValueError("Resistance cannot be negative")
