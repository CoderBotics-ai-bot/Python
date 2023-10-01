from other.graham_scan import *
import pytest


import pytest


def test_graham_scan_does_not_throw_and_returns():
    # This test simply checks if the function can run without throwing an exception
    # and that it returns something (not None). We don't care about the return value.
    points = [(0, 0), (1, 1), (2, 2), (3, 3), (-1, 2)]
    result = graham_scan(points)
    assert result is not None


def test_graham_scan_with_less_than_three_points():
    # This test checks if the function throws an error with less than three points
    # as the current implementation expects at least 3 points
    points = [(0, 0), (1, 1)]
    with pytest.raises(ValueError):
        graham_scan(points)


def test_graham_scan_with_three_points():
    # This test checks if the function can handle exactly three points
    # without any further validations, as it is expected behaviour of the code
    points = [(0, 0), (1, 1), (2, 2)]
    result = graham_scan(points)
    assert result is not None


def test_graham_scan_with_duplicate_points():
    # This test checks if the function can handle points that are same
    # as it is currently not clear how it handles
    points = [(1, 1), (1, 1), (1, 1), (2, 2)]
    result = graham_scan(points)
    assert result is not None
