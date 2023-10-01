from qiskit import QuantumCircuit

import pytest

from qiskit import QuantumCircuit
from quantum.ripple_adder_classic import *
from typing import Tuple


from typing import Tuple


def test_store_two_classics() -> None:
    """Test store_two_classics doesn't throw errors and returns the correct types."""
    circuit, x, y = store_two_classics(10, 5)
    assert circuit is not None
    assert isinstance(circuit, QuantumCircuit)
    assert isinstance(x, str)
    assert isinstance(y, str)


def test_store_two_classics_return_same_len_strs():
    """Test store_two_classics returns binary strings of the same length."""
    _, x, y = store_two_classics(13, 2)
    assert len(x) == len(y)


def test_store_two_classics_returns_correct_len_circuit():
    """Test store_two_classics returns circuit with correct qubit and classical register sizes."""
    x_val, y_val = 10, 5
    circuit, _, _ = store_two_classics(x_val, y_val)
    expected_qubits = max(x_val.bit_length(), y_val.bit_length()) * 3 + 1
    expected_clbits = max(x_val.bit_length(), y_val.bit_length()) + 1
    assert circuit.num_qubits == expected_qubits
    assert circuit.num_clbits == expected_clbits


def test_store_two_classics_zero_values():
    """Test handling of zero values."""
    _, x, y = store_two_classics(0, 0)
    assert x == "0"
    assert y == "0"


def test_store_two_classics_large_values():
    """Test handling of large value inputs."""
    circuit, x, y = store_two_classics(1023, 2046)
    assert circuit.num_qubits == len(x) * 3 + 1
    assert circuit.num_clbits == len(x) + 1
