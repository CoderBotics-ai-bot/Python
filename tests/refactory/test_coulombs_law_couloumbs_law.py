from electronics.coulombs_law import *


import pytest
import pytest

COULOMBS_CONSTANT = 8.987_551_792_3 * 10**9  # in N.m^2.C^-2


def test_couloumbs_law_force_zero():
    result = couloumbs_law(force=0, charge1=3, charge2=5, distance=2000)
    assert isinstance(result, dict)
    assert "force" in result
    assert isinstance(result["force"], float)
    force = COULOMBS_CONSTANT * abs(3 * 5) / (2000**2)
    assert result["force"] == pytest.approx(force, 0.1)


def test_couloumbs_law_distance_zero():
    result = couloumbs_law(force=10, charge1=3, charge2=5, distance=0)
    assert isinstance(result, dict)
    assert "distance" in result
    assert isinstance(result["distance"], float)
    distance = (COULOMBS_CONSTANT * abs(3 * 5) / abs(10)) ** 0.5
    assert result["distance"] == pytest.approx(distance, 0.1)


def test_couloumbs_law_charge1_zero():
    result = couloumbs_law(force=10, charge1=0, charge2=5, distance=2000)
    assert isinstance(result, dict)
    assert "charge1" in result
    assert isinstance(result["charge1"], float)
    charge1 = abs(10) * (2000**2) / (COULOMBS_CONSTANT * 5)
    assert result["charge1"] == pytest.approx(charge1, 0.1)


def test_couloumbs_law_more_than_one_zero():
    with pytest.raises(ValueError, match=r"One and only one argument must be 0"):
        couloumbs_law(force=0, charge1=0, charge2=5, distance=2000)


def test_couloumbs_law_distance_negative():
    with pytest.raises(ValueError, match=r"Distance cannot be negative"):
        couloumbs_law(force=0, charge1=3, charge2=5, distance=-2000)
