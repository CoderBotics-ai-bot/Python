from electronics.coulombs_law import *
import pytest


def test_couloumbs_law_no_exception():
    assert couloumbs_law(0, 1.0, 1.0, 10) is not None


def test_couloumbs_law_with_force_as_zero():
    result = couloumbs_law(0, 1.0, 1.0, 10)
    assert "force" in result


def test_couloumbs_law_with_charge1_as_zero():
    result = couloumbs_law(1.0, 0, 1.0, 10)
    assert "charge1" in result


def test_couloumbs_law_with_charge2_as_zero():
    result = couloumbs_law(1.0, 1.0, 0, 10)
    assert "charge2" in result


def test_couloumbs_law_with_distance_as_zero():
    result = couloumbs_law(1.0, 1.0, 1.0, 0)
    assert "distance" in result


def test_couloumbs_law_more_than_one_zero_error():
    with pytest.raises(ValueError) as e:
        couloumbs_law(0, 1.0, 0, 10)
    assert "One and only one argument must be 0" in str(e.value)


def test_couloumbs_law_no_zero_error():
    with pytest.raises(ValueError) as e:
        couloumbs_law(1.0, 1.0, 1.0, 10)
    assert "One and only one argument must be 0" in str(e.value)
