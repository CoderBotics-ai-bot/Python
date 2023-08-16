from electronics.circular_convolution import *
from typing import Any, List


from collections import deque

import numpy as np
from collections import deque
import pytest


@pytest.fixture
def circular_convolution_fixture() -> CircularConvolution:
    return CircularConvolution()


# Test with float values and equal length inputs
def test_circular_convolution_floats_equal_length(
    circular_convolution_fixture: CircularConvolution,
) -> None:
    circular_convolution_fixture.first_signal = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]
    circular_convolution_fixture.second_signal = [
        0.1,
        0.3,
        0.5,
        0.7,
        0.9,
        1.1,
        1.3,
        1.5,
    ]
    result = circular_convolution_fixture.circular_convolution()
    assert result == [5.2, 6.0, 6.48, 6.64, 6.48, 6.0, 5.2, 4.08]


# Test with inputs of unequal length
def test_circular_convolution_unequal_length(
    circular_convolution_fixture: CircularConvolution,
) -> None:
    circular_convolution_fixture.first_signal = [-1, 1, 2, -2]
    circular_convolution_fixture.second_signal = [0.5, 1, -1, 2, 0.75]
    result = circular_convolution_fixture.circular_convolution()
    assert result == [
        6.25,
        -3.0,
        1.5,
        -2.0,
        -2.75,
    ], "Expected result does not match with the obtained result"


# Edge case: Testing with one of the input signals is empty
def test_circular_convolution_empty_input(
    circular_convolution_fixture: CircularConvolution,
) -> None:
    circular_convolution_fixture.first_signal = []
    circular_convolution_fixture.second_signal = [1, 2, 3]
    result = circular_convolution_fixture.circular_convolution()
    assert result == [
        0.0,
        0.0,
        0.0,
    ], "Expected result does not match with the obtained result"


# Edge case: Testing with all zero input signals
def test_circular_convolution_zeroes(
    circular_convolution_fixture: CircularConvolution,
) -> None:
    circular_convolution_fixture.first_signal = [0, 0, 0, 0]
    circular_convolution_fixture.second_signal = [0, 0, 0, 0]
    result = circular_convolution_fixture.circular_convolution()
    assert result == [
        0.0,
        0.0,
        0.0,
        0.0,
    ], "Expected result does not match with the obtained result"
