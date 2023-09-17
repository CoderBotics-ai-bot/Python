# https://en.wikipedia.org/wiki/Charge_carrier_density
# https://www.pveducation.org/pvcdrom/pn-junctions/equilibrium-carrier-concentration
# http://www.ece.utep.edu/courses/ee3329/ee3329/Studyguide/ToC/Fundamentals/Carriers/concentrations.html

from __future__ import annotations


def carrier_concentration(
    electron_conc: float,
    hole_conc: float,
    intrinsic_conc: float,
) -> tuple:
    check_input_count(electron_conc, hole_conc, intrinsic_conc)
    check_negative_values(electron_conc, hole_conc, intrinsic_conc)

    concentration_type = ""
    calculated_value = 0.0

    if electron_conc == 0:
        concentration_type = "electron_conc"
        calculated_value = intrinsic_conc**2 / hole_conc
    elif hole_conc == 0:
        concentration_type = "hole_conc"
        calculated_value = intrinsic_conc**2 / electron_conc
    elif intrinsic_conc == 0:
        concentration_type = "intrinsic_conc"
        calculated_value = (electron_conc * hole_conc) ** 0.5

    return (concentration_type, calculated_value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def check_input_count(
    electron_conc: float, hole_conc: float, intrinsic_conc: float
) -> None:
    """
    Check the number of inputs supplied by the user.
    """
    if (electron_conc, hole_conc, intrinsic_conc).count(0) != 1:
        raise ValueError("You cannot supply more or less than 2 values")


def check_negative_values(
    electron_conc: float, hole_conc: float, intrinsic_conc: float
) -> None:
    """
    Check the sign of inputs supplied by the user.
    """
    if electron_conc < 0:
        raise ValueError("Electron concentration cannot be negative in a semiconductor")
    elif hole_conc < 0:
        raise ValueError("Hole concentration cannot be negative in a semiconductor")
    elif intrinsic_conc < 0:
        raise ValueError(
            "Intrinsic concentration cannot be negative in a semiconductor"
        )
