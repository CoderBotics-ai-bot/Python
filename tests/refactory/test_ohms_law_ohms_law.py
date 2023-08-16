import pytest


import pytest
from electronics.ohms_law import *


def test_ohms_law():
    assert ohms_law(voltage=10, resistance=5, current=0) == {"current": 2.0}
    assert ohms_law(voltage=0, current=-1.5, resistance=2) == {"voltage": -3.0}
    assert ohms_law(resistance=0, voltage=-10, current=1) == {"resistance": -10.0}


def test_ohms_law_no_values():
    with pytest.raises(ValueError) as excinfo:
        ohms_law(voltage=0, current=0, resistance=10)
    assert "One and only one argument must be 0" in str(excinfo.value)


def test_ohms_law_negative_resistance():
    with pytest.raises(ValueError) as excinfo:
        ohms_law(voltage=0, current=1, resistance=-2)
    assert "Resistance cannot be negative" in str(excinfo.value)


def test_ohms_law_multiple_values():
    with pytest.raises(ValueError) as excinfo:
        ohms_law(voltage=10, current=2, resistance=5)
    assert "One and only one argument must be 0" in str(excinfo.value)
