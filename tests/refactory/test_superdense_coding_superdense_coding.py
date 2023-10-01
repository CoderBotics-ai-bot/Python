import qiskit
import pytest
from qiskit import Aer, execute
from quantum.superdense_coding import *


import pytest


def test_superdense_coding():
    # Check that function doesn't throw an error and returns something when it's executed
    assert superdense_coding() is not None


def test_superdense_coding_typing_string():
    # Check that function throws a TypeError when either of the inputs is a string
    with pytest.raises(TypeError):
        superdense_coding(1, "j")


def test_superdense_coding_non_positive_input():
    # Check that function throws a ValueError when any of the inputs is negative
    with pytest.raises(ValueError):
        superdense_coding(-1, 0)


def test_superdense_coding_non_integer_input():
    # Check that function throws a ValueError when the inputs are not exact integers
    with pytest.raises(ValueError):
        superdense_coding(1, 0.5)


def test_superdense_coding_input_greater_than_one():
    # Check that function throws a ValueError when any of the inputs is greater than 1
    with pytest.raises(ValueError):
        superdense_coding(2, 1)


def test_superdense_coding_different_inputs():
    # Check that function runs successfully and returns expected results for various input values
    assert superdense_coding(0, 0) == {"00": 1000}
    assert superdense_coding(0, 1) == {"01": 1000}
    assert superdense_coding(1, 0) == {"10": 1000}
    assert superdense_coding(1, 1) == {"11": 1000}
