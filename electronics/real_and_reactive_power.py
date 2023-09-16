import math

def real_power(apparent_power: float, power_factor: float) -> float:
    """
    Calculate the real power from the apparent power and power factor.

    The real power is the power that is actually being used, or dissipated, in the circuit.
    It is given by the product of the apparent power and the power factor.

    Args:
      apparent_power (float): The total power in an AC circuit,
        both dissipated and absorbed or returned. This is the "vector" sum of the real and reactive power.
      power_factor (float): A parameter that is a dimensionless number between -1 and 1.
        When power factor is equal to 0, the energy flow is entirely reactive, and stored energy in the load
        returns to the source on each cycle. When the power factor is 1, all the energy supplied by the source
        is consumed by the load.

    Returns:
        float: The real power in the circuit.

    Raises:
        ValueError: If power_factor is not a float between -1 and 1.

    Examples:
        >>> real_power(100, 0.9)
        90.0
        >>> real_power(0, 0.8)
        0.0
        >>> real_power(100, -0.9)
        -90.0
    """

    if not isinstance(power_factor, (float, int)) or not -1 <= power_factor <= 1:
        raise ValueError("power_factor must be a valid float value between -1 and 1.")

    return apparent_power * power_factor


def reactive_power(apparent_power: float, power_factor: float) -> float:
    """
    Calculate reactive power from apparent power and power factor.

    Examples:
    >>> reactive_power(100, 0.9)
    43.58898943540673
    >>> reactive_power(0, 0.8)
    0.0
    >>> reactive_power(100, -0.9)
    43.58898943540673
    """
    if (
        not isinstance(power_factor, (int, float))
        or power_factor < -1
        or power_factor > 1
    ):
        raise ValueError("power_factor must be a valid float value between -1 and 1.")
    return apparent_power * math.sqrt(1 - power_factor**2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
