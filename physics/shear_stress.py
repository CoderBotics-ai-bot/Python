from __future__ import annotations

"""
Shear stress is a component of stress that is coplanar to the material cross-section.
It arises due to a shear force, the component of the force vector parallel to the
material cross-section.

https://en.wikipedia.org/wiki/Shear_stress
"""


def shear_stress(
    stress: float,
    tangential_force: float,
    area: float,
) -> tuple[str, float]:
    """
    Compute either Shear Stress, Tangential Force or Cross-sectional Area based on the other two inputs.
    For detailed functionality, refer to docstring of calculate_stress_force_area and validate_inputs function.
    """
    validate_inputs(stress, tangential_force, area)
    return calculate_stress_force_area(stress, tangential_force, area)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def calculate_stress_force_area(
    stress: float, tangential_force: float, area: float
) -> tuple[str, float]:
    """
    Handle the computation of Shear Stress, Tangential Force or Cross-sectional Area.
    Arguments are same as function shear_stress.

    Returns:
    (result_type (str) , result_value (float)): Tuple where result type can be "stress", "tangential_force", or "area"
    which indicates the calculated value and result value is the calculated float value.
    """
    if stress == 0:
        return "stress", tangential_force / area
    elif tangential_force == 0:
        return "tangential_force", stress * area
    else:
        return "area", tangential_force / stress


def validate_inputs(stress: float, tangential_force: float, area: float) -> None:
    """
    Validate inputs for the shear stress computation.
    Arguments are same as function shear_stress.

    Raises:
    ValueError: if more or less than one of stress, tangential_force, and area are 0, or if any of the given values are negative.
    """
    conditions_exceptions = {
        (stress, tangential_force, area).count(0)
        != 1: "You cannot supply more or less than two values.",
        stress < 0: "Stress cannot be negative.",
        tangential_force < 0: "Tangential Force cannot be negative.",
        area < 0: "Area cannot be negative.",
    }
    for condition, exception in conditions_exceptions.items():
        if condition:
            raise ValueError(exception)
