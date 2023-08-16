from collections import deque
from electronics.circular_convolution import *

import numpy as np
import pytest


@pytest.fixture
def circular_convolution_class():
    return CircularConvolution()


def test_circular_convolution1(circular_convolution_class):
    circular_convolution_class.first_signal = [2, 1, 2, -1]
    circular_convolution_class.second_signal = [1, 2, 3, 4]
    result = circular_convolution_class.circular_convolution()
    assert result == [10.0, 10.0, 6.0, 14.0]


def test_circular_convolution2(circular_convolution_class):
    circular_convolution_class.first_signal = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]
    circular_convolution_class.second_signal = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
    result = circular_convolution_class.circular_convolution()
    assert result == [5.2, 6.0, 6.48, 6.64, 6.48, 6.0, 5.2, 4.08]


def test_circular_convolution3(circular_convolution_class):
    circular_convolution_class.first_signal = [-1, 1, 2, -2]
    circular_convolution_class.second_signal = [0.5, 1, -1, 2, 0.75]
    result = circular_convolution_class.circular_convolution()
    assert result == [6.25, -3.0, 1.5, -2.0, -2.75]


def test_circular_convolution4(circular_convolution_class):
    circular_convolution_class.first_signal = [1, -1, 2, 3, -1]
    circular_convolution_class.second_signal = [1, 2, 3]
    result = circular_convolution_class.circular_convolution()
    assert result == [8.0, -2.0, 3.0, 4.0, 11.0]
