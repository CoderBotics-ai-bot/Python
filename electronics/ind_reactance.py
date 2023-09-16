# https://en.wikipedia.org/wiki/Electrical_reactance#Inductive_reactance
from __future__ import annotations

from math import pi

def ind_reactance(
    inductance: float, frequency: float, reactance: float
) -> dict[str, float]:
    """
    Calculate the frequency, inductive reactance, or inductance, given the just two out of three arguments.

    In the domain of electrical properties, these parameters are interrelated. The function calculates the
    missing electrical property value when two are given. In case any of these values are negatives or more
    than one argument is zero, it raises a ValueError.

    Parameters:
    ----------
    inductance : float - Inductance in Henries.
    Should be given along with either frequency or reactance.

    frequency : float - Frequency in Hertz.
    Should be given along with either inductance or reactance.

    reactance : float - Inductive reactance in Ohms.
    Should be given along with either inductance or frequency.

    Returns:
    ----------
    dict : A dictionary with the calculated value. The key of the dictionary is the calculated property(Inductance, Frequency or Reactance)
       and the value is the calculated quantity.

    Exceptions Raised:
    ----------
    ValueError : In case the parameters are negative or more than one variable is zero.

    Examples:
    ----------
    Calculate inductance when frequency and reactance are given.
    >>> ind_reactance(0, 10e3, 50)
    {'inductance': 0.0007957747154594767}

    Calculate frequency when inductance and reactance are given.
    >>> ind_reactance(35e-3, 0, 50)
    {'frequency': 227.36420441699332}

    Calculate reactance when inductance and frequency are given.
    >>> ind_reactance(35e-6, 1e3, 0)
    {'reactance': 0.2199114857512855}

    Try to calculate with negative values.
    >>> ind_reactance(-35e-6, 1e3, 0)
    Traceback (most recent call last):
        ...
    ValueError: Inductance cannot be negative

    >>> ind_reactance(35e-6, -1e3, 0)
    Traceback (most recent call last):
        ...
    ValueError: Frequency cannot be negative

    >>> ind_reactance(35e-6, 0, -1)
    Traceback (most recent call last):
        ...
    ValueError: Inductive reactance cannot be negative
    """

    zero_count = (inductance, frequency, reactance).count(0)
    negative_values = (inductance < 0, frequency < 0, reactance < 0)

    if zero_count > 1 or any(negative_values):
        raise ValueError("Invalid input parameters")

    if inductance == 0:
        return {"inductance": reactance / (2 * pi * frequency)}
    if frequency == 0:
        return {"frequency": reactance / (2 * pi * inductance)}
    return {"reactance": 2 * pi * frequency * inductance}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
