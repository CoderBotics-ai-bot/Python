from electronics.ind_reactance import *
import pytest


def test_ind_reactance_inductance():
    result = ind_reactance(0, 10e3, 50)
    assert result == {"inductance": 0.0007957747154594767}


def test_ind_reactance_frequency():
    result = ind_reactance(35e-3, 0, 50)
    assert result == {"frequency": 227.36420441699332}


def test_ind_reactance_reactance():
    result = ind_reactance(35e-6, 1e3, 0)
    assert result == {"reactance": 0.2199114857512855}


def test_ind_reactance_negative_inductance():
    with pytest.raises(ValueError) as e:
        ind_reactance(-35e-6, 1e3, 0)
    assert str(e.value) == "Inductance cannot be negative"


def test_ind_reactance_negative_frequency():
    with pytest.raises(ValueError) as e:
        ind_reactance(35e-6, -1e3, 0)
    assert str(e.value) == "Frequency cannot be negative"


def test_ind_reactance_negative_reactance():
    with pytest.raises(ValueError) as e:
        ind_reactance(35e-6, 0, -1)
    assert str(e.value) == "Inductive reactance cannot be negative"


def test_ind_reactance_multiple_zeros():
    with pytest.raises(ValueError) as e:
        ind_reactance(0, 0, 50)
    assert str(e.value) == "One and only one argument must be 0"


def test_ind_reactance_no_zeros():
    with pytest.raises(ValueError) as e:
        ind_reactance(35e-6, 1e3, 50)
    assert str(e.value) == "One and only one argument must be 0"
