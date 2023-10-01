"""Electrical impedance is the measure of the opposition that a
circuit presents to a current when a voltage is applied.
Impedance extends the concept of resistance to alternating current (AC) circuits.
Source: https://en.wikipedia.org/wiki/Electrical_impedance
"""

from __future__ import annotations

from math import pow, sqrt


from math import sqrt, pow
from typing import Dict


def electrical_impedance(
    resistance: float, reactance: float, impedance: float
) -> Dict[str, float]:
    """
    This function calculates and provides the missing electrical value using the impedance formula.
    The impedance formula is Impedance = sqrt((Resistance)^2 + (Reactance)^2).
    Therefore, when given the Resistance and Reactance, the function calculates the Impedance, and so on for the other values.

    Args:
        resistance (float): The electrical resistance value.
        reactance (float): The electrical reactance value.
        impedance (float): The electrical impedance value.

    Returns:
        dict[str, float]: A dictionary containing the missing argument as the key and its computed value as the value.

    Raises:
        ValueError: If more than one or no argument value is zero, a ValueError is raised.

    Examples:
        >>> electrical_impedance(3,4,0)
        {'impedance': 5.0}
        >>> electrical_impedance(0,4,5)
        {'resistance': 3.0}
        >>> electrical_impedance(3,0,5)
        {'reactance': 4.0}
        >>> electrical_impedance(3,4,5)
        Traceback (most recent call last)
        ValueError: One and only one argument must be 0
    """
    if (resistance, reactance, impedance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")

    return (
        {"resistance": calculate_resistance(impedance, reactance)}
        if resistance == 0
        else {"reactance": calculate_reactance(impedance, resistance)}
        if reactance == 0
        else {"impedance": calculate_impedance(resistance, reactance)}
        if impedance == 0
        else None
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def calculate_resistance(impedance: float, reactance: float) -> float:
    """Calculate the resistance using the impedance formula."""
    return sqrt(pow(impedance, 2) - pow(reactance, 2))


def calculate_reactance(impedance: float, resistance: float) -> float:
    """Calculate the reactance using the impedance formula."""
    return sqrt(pow(impedance, 2) - pow(resistance, 2))


def calculate_impedance(resistance: float, reactance: float) -> float:
    """Calculate the impedance using the impedance formula."""
    return sqrt(pow(resistance, 2) + pow(reactance, 2))
