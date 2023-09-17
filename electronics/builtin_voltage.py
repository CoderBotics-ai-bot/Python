from math import log

from scipy.constants import Boltzmann, physical_constants

T = 300  # TEMPERATURE (unit = K)


def builtin_voltage(
    donor_conc: float, acceptor_conc: float, intrinsic_conc: float
) -> float:
    """
    Calculate the Built-in Voltage (Vbi) of a PN junction diode.
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
    Validate that provided concentrations meet the necessary conditions.
    """
    if donor_conc <= 0 or acceptor_conc <= 0 or intrinsic_conc <= 0:
        raise ValueError("All concentrations should be positive")
    if donor_conc <= intrinsic_conc or acceptor_conc <= intrinsic_conc:
        raise ValueError(
            "Donor and Acceptor concentrations should be greater than intrinsic concentration"
        )
