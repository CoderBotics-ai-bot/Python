from math import log

from scipy.constants import Boltzmann, physical_constants

T = 300  # TEMPERATURE (unit = K)


def builtin_voltage(
    donor_conc: float, acceptor_conc: float, intrinsic_conc: float
) -> float:
    """
    Calculate the Builtin Voltage of a pn junction diode from given donor concentration, acceptor concentration, and intrinsic concentration.

    Constrains: donor concentration and acceptor concentration should be greater than intrinsic concentration.

    Args:
        donor_conc (float): Donor concentration.
        acceptor_conc (float): Acceptor concentration.
        intrinsic_conc (float): Intrinsic concentration.

    Returns:
        float: Builtin Voltage of a pn junction diode.

    Examples:
        >>> builtin_voltage(1e17, 1e17, 1e10)
        0.28786680267288535
    """
    validate_concentrations(donor_conc, acceptor_conc, intrinsic_conc)

    return (
        Boltzmann
        * T
        * log((donor_conc * acceptor_conc) / intrinsic_conc**2)
        / physical_constants["electron volt"][0]
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def validate_concentrations(
    donor_conc: float, acceptor_conc: float, intrinsic_conc: float
) -> None:
    """
    Validate the provided concentrations.

    Args:
        donor_conc (float): Donor concentration. Should be a positive value and greater than intrinsic concentration.
        acceptor_conc (float): Acceptor concentration. Should be a positive value and greater than intrinsic concentration.
        intrinsic_conc (float): Intrinsic concentration. Should be a positive value and less than donor and acceptor concentrations.

    Raises:
        ValueError: If donor concentration, acceptor concentration, or intrinsic concentration is not positive.
        ValueError: If donor concentration or acceptor concentration is not greater than intrinsic concentration.
    """
    if donor_conc <= 0:
        raise ValueError("Donor concentration should be positive")
    if acceptor_conc <= 0:
        raise ValueError("Acceptor concentration should be positive")
    if intrinsic_conc <= 0:
        raise ValueError("Intrinsic concentration should be positive")
    if donor_conc <= intrinsic_conc:
        raise ValueError(
            "Donor concentration should be greater than intrinsic concentration"
        )
    if acceptor_conc <= intrinsic_conc:
        raise ValueError(
            "Acceptor concentration should be greater than intrinsic concentration"
        )
