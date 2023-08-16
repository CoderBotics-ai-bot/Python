import pytest
from linear_algebra.src.power_iteration import *


def test_power_iteration():
    input_matrix = np.array([[41, 4, 20], [4, 26, 30], [20, 30, 50]])
    vector = np.array([41, 4, 20])
    eigenv, eigvec = power_iteration(input_matrix, vector)
    assert np.isclose(eigenv, 79.66086378788381, atol=1e-6)
    assert np.allclose(
        eigvec, np.array([0.44472726, 0.46209842, 0.76725662]), atol=1e-6
    )


def test_power_iteration_non_square():
    with pytest.raises(AssertionError):
        power_iteration(np.array([[1, 2, 3], [4, 5, 6]]), np.array([1, 1]))


def test_power_iteration_dimension_mismatch():
    with pytest.raises(AssertionError):
        power_iteration(np.array([[1, 2], [3, 4]]), np.array([1, 1, 1]))


def test_power_iteration_complex_reality_mismatch():
    with pytest.raises(AssertionError):
        power_iteration(np.array([[1 + 1j, 2], [3, 4]]), np.array([1, 1]))


def test_power_iteration_hermitian():
    with pytest.raises(AssertionError):
        power_iteration(
            np.array([[1 + 1j, 2 + 1j], [3 + 1j, 4]]), np.array([1 + 1j, 1])
        )
