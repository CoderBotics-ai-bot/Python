from cellular_automata.nagel_schrekenberg import *
import pytest


def test_simulate_no_error():
    highway = [[-1, 2, -1, -1, -1, 3]]
    number_of_update = 2
    probability = 0.0
    max_speed = 3
    result = simulate(highway, number_of_update, probability, max_speed)
    assert result is not None


def test_simulate_return_type():
    highway = [[-1, 2, -1, -1, -1, 3]]
    number_of_update = 2
    probability = 0.0
    max_speed = 3
    result = simulate(highway, number_of_update, probability, max_speed)
    assert isinstance(result, list)


def test_simulate_length():
    highway = [[-1, 2, -1, -1, -1, 3]]
    number_of_update = 2
    probability = 0.0
    max_speed = 3
    result = simulate(highway, number_of_update, probability, max_speed)
    assert len(result) == number_of_update + 1  # 1 is for the original highway state
