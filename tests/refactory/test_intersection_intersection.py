import pytest
from arithmetic_analysis.intersection import *


import math

import pytest
from typing import Callable


def test_intersection_no_errors():
    f = lambda x: x**3 - 1
    try:
        intersection(f, -5, 5)
    except Exception as e:
        pytest.fail(f"Unexpected Error Occured: {e}")

    assert intersection(f, -5, 5) is not None


def test_intersection_zero_division():
    f = lambda x: x**2 - 4 * x + 3
    with pytest.raises(ZeroDivisionError):
        intersection(f, 2, 2)


def test_intersection_returns_zero():
    assert math.isclose(intersection(math.sin, -math.pi, math.pi), 0.0)


def test_intersection_cos_fails():
    with pytest.raises(ZeroDivisionError):
        intersection(math.cos, -math.pi, math.pi)


def test_intersection_cos_fails_2():
    with pytest.raises(ZeroDivisionError):
        intersection(math.cos, 0.0, 0.0)
