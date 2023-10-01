import pytest
from electronics.ohms_law import *


import pytest


def test_ohms_law_does_not_throw():
    try:
        ohms_law(voltage=5, current=2, resistance=0)
    except Exception:
        pytest.fail("ohms_law() raised Exception unexpectedly!")


def test_ohms_law_with_correct_voltage_calculation():
    assert ohms_law(voltage=0, current=2, resistance=5) == {"voltage": 10.0}


def test_ohms_law_with_correct_current_calculation():
    assert ohms_law(voltage=10, resistance=5, current=0) == {"current": 2.0}


def test_ohms_law_with_correct_resistance_calculation():
    assert ohms_law(resistance=0, voltage=10, current=2) == {"resistance": 5.0}


def test_ohms_law_with_negative_resistance():
    with pytest.raises(ValueError, match="Resistance cannot be negative"):
        ohms_law(voltage=0, current=1, resistance=-2)


def test_ohms_law_with_all_values_zero():
    with pytest.raises(ValueError, match="One and only one argument must be 0"):
        ohms_law(voltage=0, current=0, resistance=0)


def test_ohms_law_with_no_values_zero():
    with pytest.raises(ValueError, match="One and only one argument must be 0"):
        ohms_law(voltage=10, current=2, resistance=5)
