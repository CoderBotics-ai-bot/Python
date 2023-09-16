from electronics.real_and_reactive_power import *
import math

import pytest


@pytest.mark.parametrize(
    "apparent_power, power_factor, expected",
    [
        (100, 0.9, 90.0),
        (0, 0.8, 0.0),
        (100, -0.9, -90.0),
        (123.45, 0, 0),
        (123.45, 1, 123.45),
        (-123.45, 1, -123.45),
    ],
)
def test_real_power(apparent_power, power_factor, expected):
    assert math.isclose(
        real_power(apparent_power, power_factor), expected, rel_tol=1e-9
    )


def test_real_power_invalid_power_factor():
    with pytest.raises(ValueError) as exc_info:
        real_power(100, 1.1)
    assert (
        str(exc_info.value)
        == "power_factor must be a valid float value between -1 and 1."
    )

    with pytest.raises(ValueError) as exc_info:
        real_power(100, -1.1)
    assert (
        str(exc_info.value)
        == "power_factor must be a valid float value between -1 and 1."
    )

    with pytest.raises(ValueError) as exc_info:
        real_power(100, "invalid")
    assert (
        str(exc_info.value)
        == "power_factor must be a valid float value between -1 and 1."
    )
