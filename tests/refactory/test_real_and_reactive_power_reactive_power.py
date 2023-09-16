

from math import sqrt

import pytest
from electronics.real_and_reactive_power import *
import pytest


def test_reactive_power_valid_inputs():
    assert reactive_power(100, 0.9) == pytest.approx(43.58898, 0.001)
    assert reactive_power(0, 0.8) == 0.0
    assert reactive_power(100, -0.9) == pytest.approx(43.58898, 0.001)


def test_reactive_power_edge_cases():
    assert reactive_power(123.45, 0) == pytest.approx(
        123.45, 0.001
    )  # power_factor=0, full reactive power
    assert reactive_power(123.45, 1) == 0.0  # power_factor=1, no reactive power
    assert (
        reactive_power(-123.45, 1) == 0.0
    )  # negative apparent_power but power_factor=1, no reactive power


def test_reactive_power_invalid_power_factor():
    with pytest.raises(
        ValueError, match="power_factor must be a valid float value between -1 and 1."
    ):
        reactive_power(100, 1.5)  # power_factor>1
    with pytest.raises(
        ValueError, match="power_factor must be a valid float value between -1 and 1."
    ):
        reactive_power(100, -1.5)  # power_factor<-1
    with pytest.raises(
        ValueError, match="power_factor must be a valid float value between -1 and 1."
    ):
        reactive_power(100, "abc")  # power_factor not a number
