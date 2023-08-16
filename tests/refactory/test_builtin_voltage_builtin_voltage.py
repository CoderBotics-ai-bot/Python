
import pytest
from math import isclose
from scipy.constants import physical_constants


from math import isclose
from electronics.builtin_voltage import *

T = 27 + 273
# Constants
donor_conc_positive = 1e17
acceptor_conc_positive = 1e17
intrinsic_conc_positive = 1e10

# Expected outputs
expected_builtin_voltage = 0.833370010652644


def test_builtin_voltage_values():
    assert isclose(
        builtin_voltage(
            donor_conc=donor_conc_positive,
            acceptor_conc=acceptor_conc_positive,
            intrinsic_conc=intrinsic_conc_positive,
        ),
        expected_builtin_voltage,
        rel_tol=1e-9,
    )


def test_builtin_voltage_zero_donor_conc():
    with pytest.raises(ValueError) as excinfo:
        builtin_voltage(
            donor_conc=0,
            acceptor_conc=acceptor_conc_positive,
            intrinsic_conc=intrinsic_conc_positive,
        )
    assert str(excinfo.value) == "Donor concentration should be positive"


def test_builtin_voltage_zero_acceptor_conc():
    with pytest.raises(ValueError) as excinfo:
        builtin_voltage(
            donor_conc=donor_conc_positive,
            acceptor_conc=0,
            intrinsic_conc=intrinsic_conc_positive,
        )
    assert str(excinfo.value) == "Acceptor concentration should be positive"


def test_builtin_voltage_zero_intrinsic_conc():
    with pytest.raises(ValueError) as excinfo:
        builtin_voltage(
            donor_conc=donor_conc_positive,
            acceptor_conc=acceptor_conc_positive,
            intrinsic_conc=0,
        )
    assert str(excinfo.value) == "Intrinsic concentration should be positive"


def test_builtin_voltage_donor_conc_less_than_intrinsic_conc():
    with pytest.raises(ValueError) as excinfo:
        builtin_voltage(
            donor_conc=1,
            acceptor_conc=acceptor_conc_positive,
            intrinsic_conc=intrinsic_conc_positive,
        )
    assert (
        str(excinfo.value)
        == "Donor concentration should be greater than intrinsic concentration"
    )


def test_builtin_voltage_acceptor_conc_less_than_intrinsic_conc():
    with pytest.raises(ValueError) as excinfo:
        builtin_voltage(
            donor_conc=donor_conc_positive,
            acceptor_conc=1,
            intrinsic_conc=intrinsic_conc_positive,
        )
    assert (
        str(excinfo.value)
        == "Acceptor concentration should be greater than intrinsic concentration"
    )
