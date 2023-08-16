# https://en.wikipedia.org/wiki/Electrical_reactance#Inductive_reactance
from __future__ import annotations

from math import pi

def ind_reactance(
    inductance: float, frequency: float, reactance: float
) -> dict[str, float]:
    """
    Calculate inductive reactance, frequency or inductance from two given electrical
    properties then return name/value pair of the zero value in a Python dict.

    Parameters
    ----------
    inductance : float with units in Henries

    frequency : float with units in Hertz

    reactance : float with units in Ohms

    Returns
    -------
    dict : dictionary containing the calculated value of the property that was input as zero.
           The key is the name of the property and the value is the calculated value.

    Raises
    ------
    ValueError : if more than one or none of the input properties are zero or negative.

    Examples
    --------
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

    >>> ind_reactance(0, 10e3, 50)
    {'inductance': 0.0007957747154594767}

    >>> ind_reactance(35e-3, 0, 50)
    {'frequency': 227.36420441699332}

    >>> ind_reactance(35e-6, 1e3, 0)
    {'reactance': 0.2199114857512855}
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
