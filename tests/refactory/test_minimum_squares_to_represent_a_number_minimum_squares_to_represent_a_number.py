from dynamic_programming.minimum_squares_to_represent_a_number import *
import pytest


def test_minimum_squares_to_represent_a_number_no_error():
    assert minimum_squares_to_represent_a_number(25) is not None


def test_minimum_squares_to_represent_a_number_negative_input():
    with pytest.raises(ValueError):
        minimum_squares_to_represent_a_number(-1)


def test_minimum_squares_to_represent_a_number_non_integer():
    with pytest.raises(ValueError):
        minimum_squares_to_represent_a_number(12.34)


def test_minimum_squares_to_represent_a_number_zero_case():
    assert minimum_squares_to_represent_a_number(0) == 1


def test_minimum_squares_to_represent_a_number_large_number():
    assert minimum_squares_to_represent_a_number(10000) is not None
