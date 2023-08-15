import numpy as np

def power_iteration(
    input_matrix: np.ndarray,
    vector: np.ndarray,
    error_tol: float = 1e-12,
    max_iterations: int = 100,
) -> tuple[float, np.ndarray]:
    eigenvalue_old = 0.0

    for _ in range(max_iterations):
        vector = np.dot(input_matrix, vector)
        vector_norm = np.linalg.norm(vector)
        vector = vector / vector_norm

        # New eigenvalue
        eigenvalue = np.dot(vector.T, np.dot(input_matrix, vector))

        # Check for convergence
        if np.abs(eigenvalue - eigenvalue_old) < error_tol:
            break

        eigenvalue_old = eigenvalue

    return eigenvalue, vector

def test_power_iteration() -> None:
    """
    Test the power_iteration function.

    This test case compares the output of power_iteration function against
    numpy's built-in function np.linalg.eigh for computing eigenvalues and
    corresponding eigenvectors of real and complex matrices.

    The function checks if the computed maximum eigenvalue and corresponding
    eigenvector from power_iteration is approximately equivalent to the one
    returned by np.linalg.eigh.

    Raises:
        AssertionError: If the computed eigenvalue / eigenvector of the matrix
                        by power_iteration does not closely match numpy's
                        eigenvalue / eigenvector.

    >>> test_power_iteration()  # self running tests
    """
    matrix = np.random.rand(3, 3)
    max_eigenvalue, eigenvector = power_iteration(matrix)

    _, numpy_eigenvectors = np.linalg.eigh(matrix)
    numpy_max_eigenvalue = max(numpy_eigenvectors)

    np.testing.assert_almost_equal(max_eigenvalue, numpy_max_eigenvalue, decimal=5)
    np.testing.assert_almost_equal(eigenvector, numpy_eigenvectors[:, -1], decimal=5)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_power_iteration()
