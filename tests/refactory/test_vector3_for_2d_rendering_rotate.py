import pytest
from graphics.vector3_for_2d_rendering import *


def test_rotate_positive_case():
    result = rotate(1.0, 2.0, 3.0, "y", 90.0)
    assert len(result) == 3
    assert math.isclose(result[0], 3.130524675073759, rel_tol=1e-6)
    assert math.isclose(result[1], 2.0, rel_tol=1e-6)
    assert math.isclose(result[2], 0.4470070007889556, rel_tol=1e-6)


@pytest.mark.parametrize("axis,angle", [("z", 180), ("x", -90), ("x", 450)])
def test_rotate_valid_inputs(axis: str, angle: float):
    result = rotate(1.0, 2.0, 3.0, axis, angle)
    assert len(result) == 3


def test_rotate_invalid_types():
    with pytest.raises(
        TypeError, match="Input values except axis must either be float or int:"
    ):
        rotate("1", 2, 3, "z", 90.0)


def test_rotate_invalid_axis():
    with pytest.raises(
        ValueError, match="not a valid axis, choose one of 'x', 'y', 'z'"
    ):
        rotate(1, 2, 3, "n", 90)
