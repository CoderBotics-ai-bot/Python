# https://en.wikipedia.org/wiki/Coulomb%27s_law

from __future__ import annotations


from typing import List

COULOMBS_CONSTANT = 8.988e9  # units = N * m^s * C^-2

def couloumbs_law(
    force: float, charge1: float, charge2: float, distance: float
) -> dict[str, float]:
    """
    function to calculate missing values using couloumbs law.
    """
    # Guard clauses to early return
    calculate_equal_zero_params(force, charge1, charge2, distance)
    determine_distance(distance)

    # Main function to calculate the missing parameters
    return calculate_missing_parameters(force, charge1, charge2, distance)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def calculate_equal_zero_params(
    force: float, charge1: float, charge2: float, distance: float
) -> None:
    """
    function to validate input parameters. One and only one parameter should be zero.
    """
    if (force, charge1, charge2, distance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")


def determine_distance(distance: float) -> None:
    """
    function to validate distance parameter. It shouldn't be less than zero.
    """
    if distance < 0:
        raise ValueError("Distance cannot be negative")


def calculate_missing_parameters(
    force: float, charge1: float, charge2: float, distance: float
) -> dict[str, float]:
    """
    function to calculate the missing parameters.
    """
    charge_product = abs(charge1 * charge2)
    if force == 0:
        force = calculate_force(charge_product, distance)
        return {"force": force}
    elif charge1 == 0:
        charge1 = calculate_charge1(force, charge2, distance)
        return {"charge1": charge1}
    elif charge2 == 0:
        charge2 = calculate_charge2(force, charge1, distance)
        return {"charge2": charge2}
    elif distance == 0:
        distance = calculate_distance(charge_product, force)
        return {"distance": distance}


def calculate_force(charge_product: float, distance: float) -> float:
    """
    function to calculate force.
    """
    return COULOMBS_CONSTANT * charge_product / (distance**2)


def calculate_charge1(force: float, charge2: float, distance: float) -> float:
    """
    function to calculate charge1.
    """
    return abs(force) * (distance**2) / (COULOMBS_CONSTANT * charge2)


def calculate_charge2(force: float, charge1: float, distance: float) -> float:
    """
    function to calculate charge2.
    """
    return abs(force) * (distance**2) / (COULOMBS_CONSTANT * charge1)


def calculate_distance(charge_product: float, force: float) -> float:
    """
    function to calculate distance.
    """
    return (COULOMBS_CONSTANT * charge_product / abs(force)) ** 0.5
