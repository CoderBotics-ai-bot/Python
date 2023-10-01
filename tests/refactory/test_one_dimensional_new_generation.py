from cellular_automata.one_dimensional import *
import pytest


def test_new_generation_no_error():
    cells = [[1, 0, 1], [0, 1, 0]]
    rule = [0, 1, 1, 1, 1, 0, 0, 0]
    time = 1
    result = new_generation(cells, rule, time)
    assert result is not None, "The function should return a result"


def test_new_generation_correct_shapes():
    cells = [[1, 0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1]]
    rule = [0, 1, 1, 1, 1, 0, 0, 0]
    time = 1
    result = new_generation(cells, rule, time)
    assert len(result) == len(
        cells[0]
    ), "The new generation should have the same shape as the previous ones"


def test_new_generation_works_with_empty_input():
    cells = [[]]
    rule = [0, 1, 1, 1, 1, 0, 0, 0]
    time = 0
    result = new_generation(cells, rule, time)
    assert result == [], "The new generation should be empty if the previous one was"
