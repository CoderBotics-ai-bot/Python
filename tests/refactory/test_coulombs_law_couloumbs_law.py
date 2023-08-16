

from typing import Any
from electronics.coulombs_law import *
from typing import Any

import pytest


@pytest.mark.parametrize(
    "force,charge1,charge2,distance,output",
    [
        (0, 1, 1, 1, {"force": COULOMBS_CONSTANT}),
        (COULOMBS_CONSTANT, 0, 1, 1, {"charge1": 1}),
        (COULOMBS_CONSTANT, 1, 0, 1, {"charge2": 1}),
        (COULOMBS_CONSTANT, 1, 1, 0, {"distance": 1}),
    ],
)
def test_couloumbs_law_normal_cases(
    force: float,
    charge1: float,
    charge2: float,
    distance: float,
    output: dict[str, Any],
):
    assert (
        couloumbs_law(force=force, charge1=charge1, charge2=charge2, distance=distance)
        == output
    )


def test_couloumbs_law_no_zeros():
    with pytest.raises(ValueError, match="One and only one argument must be 0"):
        couloumbs_law(1, 1, 1, 1)

    with pytest.raises(ValueError, match="One and only one argument must be 0"):
        couloumbs_law(0, 0, 1, 1)


def test_couloumbs_law_negative_distance():
    with pytest.raises(ValueError, match="Distance cannot be negative"):
        couloumbs_law(0, 1, 1, -1)
