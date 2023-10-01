from random import random

import pytest
from cellular_automata.nagel_schrekenberg import *
from typing import List


def test_update_no_error():
    highway = [-1, -1, -1, -1, -1, 2, -1, -1, -1, -1, 3]
    probability = 0.0
    max_speed = 5
    result = update(highway, probability, max_speed)
    assert result is not None


def test_update_type():
    highway = [-1, -1, -1, -1, -1, 2, -1, -1, -1, -1, 3]
    probability = 0.0
    max_speed = 5
    result = update(highway, probability, max_speed)
    assert isinstance(result, list)


def test_update_length():
    highway = [-1, -1, -1, -1, -1, 2, -1, -1, -1, -1, 3]
    probability = 0.0
    max_speed = 5
    result = update(highway, probability, max_speed)
    assert len(result) == len(highway)


@pytest.mark.parametrize(
    "highway,probability,max_speed",
    [
        ([-1, -1, -1, -1, -1, 2, -1, -1, -1, -1, 3], 0.0, 5),
        ([-1, -1, -1, -1, -1, 2, -1, -1, -1, -1, 3], 0.1, 5),
        ([-1, -1, -1, -1, -1, 2, -1, -1, -1, -1, 3], 0.5, 5),
    ],
)
def test_update_probability_change(highway, probability, max_speed):
    result = update(highway, probability, max_speed)
    assert result is not None
