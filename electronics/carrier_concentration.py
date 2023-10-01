# https://en.wikipedia.org/wiki/Charge_carrier_density
# https://www.pveducation.org/pvcdrom/pn-junctions/equilibrium-carrier-concentration
# http://www.ece.utep.edu/courses/ee3329/ee3329/Studyguide/ToC/Fundamentals/Carriers/concentrations.html

from __future__ import annotations


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def carrier_concentration(
    electron_conc: float,
    hole_conc: float,
    intrinsic_conc: float,
) -> tuple:
    """
    This function can calculate any one of the three -
    1. Electron Concentration
    2. Hole Concentration
    3. Intrinsic Concentration
    given the other two.
    """
    validate_input_values(electron_conc, hole_conc, intrinsic_conc)
    return compute_carrier_concentration(electron_conc, hole_conc, intrinsic_conc)


def validate_input_values(electron_conc, hole_conc, intrinsic_conc):
    if (electron_conc, hole_conc, intrinsic_conc).count(0) != 1:
        raise ValueError("You cannot supply more or less than 2 values")
    for concentration, value in zip(
        ["Electron", "Hole", "Intrinsic"], [electron_conc, hole_conc, intrinsic_conc]
    ):
        if value < 0:
            raise ValueError(
                f"{concentration} concentration cannot be negative in a semiconductor"
            )


def compute_carrier_concentration(electron_conc, hole_conc, intrinsic_conc):
    if electron_conc == 0:
        return "electron_conc", intrinsic_conc**2 / hole_conc
    elif hole_conc == 0:
        return "hole_conc", intrinsic_conc**2 / electron_conc
    elif intrinsic_conc == 0:
        return "intrinsic_conc", (electron_conc * hole_conc) ** 0.5
