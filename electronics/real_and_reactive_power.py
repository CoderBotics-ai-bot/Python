import math

def real_power(apparent_power: float, power_factor: float) -> float:
    """
    Calculate real power from apparent power and power factor.

    The real power is the capacity of the electricity for performing work. It
    is a measure of the actual power that is really working, or being consumed,
    at any instant. The real power is computed as the product of the apparent
    power and the power factor.

    Args:
        apparent_power (float): The total power in an AC circuit, both dissipated
            and absorbed or returned. Apparent power is measured in the unit of Volt-Amps (VA).
        power_factor (float): A dimensionless number between -1 and 1. It represents
            the fraction of the electrical power that is dissipated in the load and
            does useful work. A power factor of 1 indicates that the power is fully
            utilized. A power factor of -1 indicates that the power is completely wasted.

    Returns:
        float: The real power in watts (W). It's the product of the apparent power
            and the power factor.

    Raises:
        ValueError: If power_factor is not a valid float or int between -1 and 1.

    Examples:
        >>> real_power(100, 0.9)
        90.0
        >>> real_power(0, 0.8)
        0.0
        >>> real_power(100, -0.9)
        -90.0
    """
    if not isinstance(power_factor, (int, float)) or not -1 <= power_factor <= 1:
        raise ValueError(
            "power_factor must be a valid float or int value between -1 and 1."
        )
    return apparent_power * power_factor

def reactive_power(apparent_power: float, power_factor: float) -> float:
    """
    Calculate the reactive power from the apparent power and power factor.

    Args:
        apparent_power (float): The total power in an AC circuit.
        power_factor (float): The ratio of the actual electrical power dissipated by an AC circuit.

    Returns:
        float: The reactive power in the AC circuit.

    Raises:
        TypeError: If apparent_power is not a float
        ValueError: If power_factor isn't a number or within the range -1 and 1.

    Examples:
        >>> reactive_power(100, 0.9)
        43.58898943540673
        >>> reactive_power(0, 0.8)
        0.0
        >>> reactive_power(100, -0.9)
        43.58898943540673
    """
    if not isinstance(apparent_power, (int, float)):
        raise TypeError("apparent_power must be of type float.")

    if not isinstance(power_factor, (int, float)) or not -1 <= power_factor <= 1:
        raise ValueError("power_factor must be a valid number between -1 and 1.")

    return apparent_power * math.sqrt(1 - power_factor**2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
