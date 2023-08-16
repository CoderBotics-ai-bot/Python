from dynamic_programming.minimum_squares_to_represent_a_number import *
import pytest


def test_minimum_squares_to_represent_a_number():
    # Test with square number
    assert minimum_squares_to_represent_a_number(25) == 1

    # Test with non square number
    assert minimum_squares_to_represent_a_number(37) == 2
    assert minimum_squares_to_represent_a_number(21) == 3
    assert minimum_squares_to_represent_a_number(58) == 2

    # Test with zero
    assert minimum_squares_to_represent_a_number(0) == 1

    # Test with negative number
    try:
        minimum_squares_to_represent_a_number(-1)
    except ValueError as ve:
        assert str(ve) == "the value of input must not be a negative number"

    # Test with non integer number
    try:
        minimum_squares_to_represent_a_number(12.34)
    except ValueError as ve:
        assert str(ve) == "the value of input must be a natural number"
