import pytest
from electronics.ind_reactance import *

import pytest


from math import isclose


def test_ind_reactance_all_positive_parameters():
    result = ind_reactance(35e-6, 1e3, 0)
    assert isclose(result.get("reactance", 0), 0.2199114857512855, rel_tol=1e-8)


def test_ind_reactance_two_zero_parameters():
    with pytest.raises(ValueError, match="One and only one argument must be 0"):
        ind_reactance(0, 0, 10)


def test_ind_reactance_no_zero_parameters():
    with pytest.raises(ValueError, match="One and only one argument must be 0"):
        ind_reactance(4, 5, 10)


def test_ind_reactance_negative_inductance():
    with pytest.raises(ValueError, match="Inductance cannot be negative"):
        ind_reactance(-35e-6, 1e3, 0)


def test_ind_reactance_negative_frequency():
    with pytest.raises(ValueError, match="Frequency cannot be negative"):
        ind_reactance(35e-6, -1e3, 0)


def test_ind_reactance_calculate_inductance():
    result = ind_reactance(0, 10e3, 50)
    assert isclose(result.get("inductance", 0), 0.0007957747154594767, rel_tol=1e-8)


def test_ind_reactance_calculate_frequency():
    result = ind_reactance(35e-3, 0, 50)
    assert isclose(result.get("frequency", 0), 227.36420441699332, rel_tol=1e-8)


def test_ind_reactance_calculate_reactance():
    result = ind_reactance(35e-6, 1e3, 0)
    assert isclose(result.get("reactance", 0), 0.2199114857512855, rel_tol=1e-8)
