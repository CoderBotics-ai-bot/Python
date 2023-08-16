import pytest
from electronics.electric_conductivity import *


def test_electric_conductivity_mobility_as_answer():
    assert electric_conductivity(25, 100, 0) == ("mobility", 1.5604519068722301e18)


def test_electric_conductivity_conductivity_as_answer():
    assert electric_conductivity(0, 1600, 200) == ("conductivity", 5.12672e-14)


def test_electric_conductivity_electron_conc_as_answer():
    assert electric_conductivity(1000, 0, 1200) == (
        "electron_conc",
        5.201506356240767e18,
    )


def test_electric_conductivity_zero_zero_input():
    with pytest.raises(
        ValueError, match="You cannot supply more or less than 2 values"
    ):
        electric_conductivity(100, 0, 0)


def test_electric_conductivity_all_zero_input():
    with pytest.raises(
        ValueError, match="You cannot supply more or less than 2 values"
    ):
        electric_conductivity(0, 0, 0)
