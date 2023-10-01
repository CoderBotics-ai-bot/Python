import pytest
from other.guess_the_number_search import *


import pytest


def test_temp_input_value_no_errors():
    assert temp_input_value() is not None
    assert temp_input_value(50, 100, True) is not None
    assert temp_input_value(50, 100, False) is not None


def test_temp_input_value_return_values():
    assert temp_input_value(50, 100, True) == 50
    assert temp_input_value(50, 100, False) == 100


def test_temp_input_value_exceptions():
    with pytest.raises(AssertionError):
        temp_input_value("50", 100, True)
    with pytest.raises(AssertionError):
        temp_input_value(50, "100", True)
    with pytest.raises(AssertionError):
        temp_input_value(50, 100, "True")

    with pytest.raises(ValueError):
        temp_input_value(500, 100, True)
    with pytest.raises(ValueError):
        temp_input_value(50, -100, True)
