import qiskit

import pytest
from qiskit.visualization import plot_histogram
from typing import Optional
from numpy.random import PCG64, Generator
from qiskit import Aer, QuantumCircuit, execute
from quantum.bb84 import *


def test_bb84_no_throw():
    """Test if the function 'bb84' executes without throwing errors."""
    assert bb84() is not None


def test_bb84_return_type():
    """Test whether the function 'bb84' returns a string."""
    assert isinstance(bb84(), str)


def test_bb84_key_len():
    """Test whether the function 'bb84' returns a string of the specified length."""
    key_len = 16
    assert len(bb84(key_len)) == key_len


def test_bb84_seed_consistency():
    """
    Test whether the function 'bb84' produces the consistent outputs with the same seed.
    """
    seed = 0

    # Execute the function twice with the same seed
    key1 = bb84(key_len=16, seed=seed)
    key2 = bb84(key_len=16, seed=seed)

    # The outputs should be identical
    assert key1 == key2


# Include necessary imports here
import numpy as np
