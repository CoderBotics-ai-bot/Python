from electronics.carrier_concentration import *
import pytest


def test_carrier_concentration_no_errors():
    assert (
        carrier_concentration(electron_conc=25, hole_conc=100, intrinsic_conc=0)
        is not None
    )
    assert (
        carrier_concentration(electron_conc=0, hole_conc=1600, intrinsic_conc=200)
        is not None
    )
    assert (
        carrier_concentration(electron_conc=1000, hole_conc=0, intrinsic_conc=1200)
        is not None
    )


def test_carrier_concentration_edge_cases():
    with pytest.raises(
        ValueError, match="You cannot supply more or less than 2 values"
    ):
        carrier_concentration(electron_conc=1000, hole_conc=400, intrinsic_conc=1200)

    with pytest.raises(
        ValueError, match="Electron concentration cannot be negative in a semiconductor"
    ):
        carrier_concentration(electron_conc=-1000, hole_conc=0, intrinsic_conc=1200)

    with pytest.raises(
        ValueError, match="Hole concentration cannot be negative in a semiconductor"
    ):
        carrier_concentration(electron_conc=0, hole_conc=-400, intrinsic_conc=1200)

    with pytest.raises(
        ValueError,
        match="Intrinsic concentration cannot be negative in a semiconductor",
    ):
        carrier_concentration(electron_conc=0, hole_conc=400, intrinsic_conc=-1200)
