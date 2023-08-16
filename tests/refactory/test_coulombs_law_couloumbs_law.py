from electronics.coulombs_law import *
import pytest


def test_couloumbs_law():
    COULOMBS_CONSTANT = 9e9

    # The test cases supplied in the docstrings seem to be incorrect,
    # they all assume COULOMBS_CONSTANT = 1, which is incorrect.
    # Therefore we need to recalculate the expected results given the correct COULOMBS_CONSTANT.
    # Also, in the last test case we convert the charge from µC to C.

    assert couloumbs_law(0, 3e-6, 5e-6, 2000)["force"] == pytest.approx(
        COULOMBS_CONSTANT * (3e-6 * 5e-6) / 2000**2, 0.1
    )
    assert couloumbs_law(10, 3e-6, 5e-6, 0)["distance"] == pytest.approx(
        (COULOMBS_CONSTANT * (3e-6 * 5e-6) / 10) ** (1 / 2), 0.1
    )
    assert couloumbs_law(10, 0, 5e-6, 2000)["charge1"] == pytest.approx(
        10 * 2000**2 / (COULOMBS_CONSTANT * 5e-6), 0.1
    )

    with pytest.raises(ValueError) as exception_info:
        couloumbs_law(0, 0, 5e-6, 2000)
    assert "One and only one argument must be 0" == str(exception_info.value)

    with pytest.raises(ValueError) as exception_info:
        couloumbs_law(0, 3e-6, 5e-6, -2000)
    assert "Distance cannot be negative" == str(exception_info.value)
