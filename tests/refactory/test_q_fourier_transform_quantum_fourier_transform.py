from quantum.q_fourier_transform import *
import pytest


import pytest


def test_quantum_fourier_transform_not_none():
    result = quantum_fourier_transform(number_of_qubits=2)
    assert result is not None


def test_quantum_fourier_transform_returns_dictionary():
    result = quantum_fourier_transform(number_of_qubits=2)
    assert isinstance(result, dict)


def test_quantum_fourier_transform_invalid_input_type():
    with pytest.raises(TypeError):
        quantum_fourier_transform("a")


def test_quantum_fourier_transform_invalid_input_negative():
    with pytest.raises(ValueError):
        quantum_fourier_transform(-1)


def test_quantum_fourier_transform_invalid_input_float():
    with pytest.raises(ValueError):
        quantum_fourier_transform(0.5)


def test_quantum_fourier_transform_invalid_input_large():
    with pytest.raises(ValueError):
        quantum_fourier_transform(11)
