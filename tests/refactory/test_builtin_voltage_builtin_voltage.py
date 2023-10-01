import pytest
from electronics.builtin_voltage import *


import pytest


def test_builtin_voltage():
    # Defining the input values
    donor_conc = 1e17
    acceptor_conc = 1e17
    intrinsic_conc = 1e10

    # Run without exceptions
    result = builtin_voltage(donor_conc, acceptor_conc, intrinsic_conc)
    assert result is not None


def test_builtin_voltage_zero_donor_conc():
    # Expect ValueError because donor_conc is zero
    donor_conc = 0
    acceptor_conc = 1600
    intrinsic_conc = 200
    with pytest.raises(ValueError, match="Donor concentration should be positive"):
        builtin_voltage(donor_conc, acceptor_conc, intrinsic_conc)


def test_builtin_voltage_zero_acceptor_conc():
    # Expect ValueError because acceptor_conc is zero
    donor_conc = 1000
    acceptor_conc = 0
    intrinsic_conc = 1200
    with pytest.raises(ValueError, match="Acceptor concentration should be positive"):
        builtin_voltage(donor_conc, acceptor_conc, intrinsic_conc)


def test_builtin_voltage_zero_intrinsic_conc():
    # Expect ValueError because intrinsic_conc is zero
    donor_conc = 1000
    acceptor_conc = 1000
    intrinsic_conc = 0
    with pytest.raises(ValueError, match="Intrinsic concentration should be positive"):
        builtin_voltage(donor_conc, acceptor_conc, intrinsic_conc)


def test_builtin_voltage_donator_less_than_intrinsic_conc():
    # Expect ValueError because donor_conc is less than intrinsic_conc
    donor_conc = 1000
    acceptor_conc = 3000
    intrinsic_conc = 2000
    with pytest.raises(
        ValueError,
        match="Donor concentration should be greater than intrinsic concentration",
    ):
        builtin_voltage(donor_conc, acceptor_conc, intrinsic_conc)


def test_builtin_voltage_acceptor_less_than_intrinsic_conc():
    # Expect ValueError because acceptor_conc is less than intrinsic_conc
    donor_conc = 3000
    acceptor_conc = 1000
    intrinsic_conc = 2000
    with pytest.raises(
        ValueError,
        match="Acceptor concentration should be greater than intrinsic concentration",
    ):
        builtin_voltage(donor_conc, acceptor_conc, intrinsic_conc)
