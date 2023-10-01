# https://en.wikipedia.org/wiki/Coulomb%27s_law

from __future__ import annotations

COULOMBS_CONSTANT = 8.988e9  # units = N * m^s * C^-2

def couloumbs_law(
    force: float, charge1: float, charge2: float, distance: float
) -> dict[str, float]:
    """
    (... same docstring...)
    """
    _validate_inputs(force, charge1, charge2, distance)

    if force == 0:
        return {"force": _calculate_force(charge1, charge2, distance)}
    elif charge1 == 0:
        return {"charge1": _calculate_charge(force, charge2, distance)}
    elif charge2 == 0:
        return {"charge2": _calculate_charge(force, charge1, distance)}
    elif distance == 0:
        return {"distance": _calculate_distance(force, charge1, charge2)}


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def _calculate_force(charge1: float, charge2: float, distance: float) -> float:
    return COULOMBS_CONSTANT * abs(charge1 * charge2) / (distance**2)


def _calculate_charge(force: float, charge: float, distance: float) -> float:
    return abs(force) * (distance**2) / (COULOMBS_CONSTANT * charge)


def _calculate_distance(force: float, charge1: float, charge2: float) -> float:
    return (COULOMBS_CONSTANT * abs(charge1 * charge2) / abs(force)) ** 0.5


def _validate_inputs(
    force: float, charge1: float, charge2: float, distance: float
) -> None:
    if (force, charge1, charge2, distance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if distance < 0:
        raise ValueError("Distance cannot be negative")
