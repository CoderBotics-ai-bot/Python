# https://en.wikipedia.org/wiki/Charge_carrier_density
# https://www.pveducation.org/pvcdrom/pn-junctions/equilibrium-carrier-concentration
# http://www.ece.utep.edu/courses/ee3329/ee3329/Studyguide/ToC/Fundamentals/Carriers/concentrations.html

from __future__ import annotations

def carrier_concentration(
    electron_conc: float,
    hole_conc: float,
    intrinsic_conc: float,
) -> tuple:
    """
    Calculates the carrier concentration in semiconductors.

    Given 2 out of 3 parameters (electron concentration, hole concentration, intrinsic concentration),
    this function calculates the omitted parameter. Only two parameters should be provided, the remaining one should be set to 0.
    Note that none of the input parameters can be negative.

    Args:
        electron_conc (float): Electron concentration. Set this to 0 if this is the value to be calculated.
        hole_conc (float): Hole concentration. Set this to 0 if this is the value to be calculated.
        intrinsic_conc (float): Intrinsic concentration. Set this to 0 if this is the value to be calculated.

    Returns:
        tuple: A tuple where the first element is the name of the calculated parameter ('electron_conc', 'hole_conc', 'intrinsic_conc')
               and the second element is the calculated value.

    Raises:
        ValueError: If more than or less than 1 input parameter is 0.
        ValueError: If any of the input parameters is negative.

    Examples -
        >>> carrier_concentration(electron_conc=25, hole_conc=100, intrinsic_conc=0)
        ('intrinsic_conc', 50.0)
        >>> carrier_concentration(electron_conc=0, hole_conc=1600, intrinsic_conc=200)
        ('electron_conc', 25.0)
        >>> carrier_concentration(electron_conc=1000, hole_conc=0, intrinsic_conc=1200)
        ('hole_conc', 1440.0)
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
