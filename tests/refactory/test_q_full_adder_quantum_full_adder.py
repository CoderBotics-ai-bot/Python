from quantum.q_full_adder import *
import pytest


def test_quantum_full_adder():
    assert quantum_full_adder() is not None


def test_quantum_full_adder_edge_cases_1():
    with pytest.raises(TypeError):
        quantum_full_adder("q", 0, 1)


def test_quantum_full_adder_edge_cases_2():
    with pytest.raises(ValueError):
        quantum_full_adder(1, -4, 1)


def test_quantum_full_adder_edge_cases_3():
    with pytest.raises(ValueError):
        quantum_full_adder(0.5, 0, 1)


def test_quantum_full_adder_edge_cases_4():
    with pytest.raises(ValueError):
        quantum_full_adder(0, 1, 3)
