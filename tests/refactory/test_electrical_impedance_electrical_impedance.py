from electronics.electrical_impedance import *
import pytest


def test_electrical_impedance_no_errors():
    output = electrical_impedance(3, 4, 0)
    assert output is not None


def test_electrical_impedance_negative_case():
    import pytest

    with pytest.raises(ValueError):
        electrical_impedance(3, 4, 5)


def test_electrical_impedance_with_resistance_zero():
    output = electrical_impedance(0, 4, 5)
    assert "resistance" in output


def test_electrical_impedance_with_reactance_zero():
    output = electrical_impedance(3, 0, 5)
    assert "reactance" in output


def test_electrical_impedance_with_impedance_zero():
    output = electrical_impedance(3, 4, 0)
    assert "impedance" in output
