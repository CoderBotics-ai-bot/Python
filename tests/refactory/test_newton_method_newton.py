
import numpy as np
import pytest
import math
from arithmetic_analysis.newton_method import *
from typing import Callable

RealFunc = Callable[[float], float]


@pytest.fixture
def function_1() -> RealFunc:
    return lambda x: x**3 - 2 * x - 5


@pytest.fixture
def derivative_1() -> RealFunc:
    return lambda x: 3 * x**2 - 2


@pytest.fixture
def function_2() -> RealFunc:
    return math.sin


@pytest.fixture
def derivative_2() -> RealFunc:
    return math.cos


def test_newton_not_none_1(function_1: RealFunc, derivative_1: RealFunc):
    assert newton(function_1, derivative_1, 3) is not None


def test_newton_not_none_2(function_2: RealFunc, derivative_2: RealFunc):
    assert newton(function_2, derivative_2, 1) is not None


def test_newton_math_sin_cos():
    result = newton(math.sin, math.cos, 2)
    assert np.isclose(result, np.pi, atol=1e-05)


def test_newton_math_cos_nsin():
    result = newton(math.cos, lambda x: -math.sin(x), 2)
    assert np.isclose(result, np.pi / 2, atol=1e-05)


def test_newton_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        newton(math.cos, lambda x: -math.sin(x), 0)
