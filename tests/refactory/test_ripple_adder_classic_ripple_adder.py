import pytest
from quantum.ripple_adder_classic import *


import pytest


def test_ripple_adder_no_error_on_execution() -> None:
    """
    Test if the function executes without throwing an error
    """
    try:
        ripple_adder(5, 5)
    except Exception as e:
        pytest.fail(f"Test failed due to an error thrown: {e}")


def test_ripple_adder_return_value_type() -> None:
    """
    Test if the function return's value is of the correct type
    """
    assert isinstance(ripple_adder(5, 5), int)


def test_ripple_adder_negative_integers() -> None:
    """
    Test if the function raises ValueError when a negative integer is provided
    """
    with pytest.raises(ValueError):
        ripple_adder(-5, 5)


def test_ripple_adder_zero_values() -> None:
    """
    Test if the function correctly handles a scenario where both input values are zero
    """
    assert ripple_adder(0, 0) == 0


def test_ripple_adder_large_values() -> None:
    """
    Test if the function correctly handles a scenario where large input values are provided
    """
    assert isinstance(ripple_adder(100000, 100000), int)
