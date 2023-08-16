from matrix.sherman_morrison import *
import pytest


def test_matrix_validate_indices():
    m = Matrix(3, 3, 0)

    # positive test case (within range)
    assert m.validate_indices((1, 1))

    # positive test case (valid input as list)
    assert m.validate_indices([1, 1])

    # negative test case (x too high)
    assert not m.validate_indices((3, 0))

    # negative test case (x too low)
    assert not m.validate_indices((-1, 0))

    # negative test case (y too high)
    assert not m.validate_indices((0, 3))

    # negative test case (y too low)
    assert not m.validate_indices((0, -1))

    # negative test case (both too high)
    assert not m.validate_indices((3, 3))

    # negative test case (not a list or tuple)
    assert not m.validate_indices("0, 0")

    # negative test case (not a pair)
    assert not m.validate_indices((0, 0, 0))
