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
    >>> test_power_iteration()  # self running tests
    """
    real_input_matrix = np.array([[41, 4, 20], [4, 26, 30], [20, 30, 50]])
    real_vector = np.array([41, 4, 20])
    complex_input_matrix = real_input_matrix.astype(np.complex128)
    imag_matrix = np.triu(1j * complex_input_matrix, 1)
    complex_input_matrix += imag_matrix
    complex_input_matrix += -1 * imag_matrix.T
    complex_vector = np.array([41, 4, 20]).astype(np.complex128)

    for problem_type in ["real", "complex"]:
        if problem_type == "real":
            input_matrix = real_input_matrix
            vector = real_vector
        elif problem_type == "complex":
            input_matrix = complex_input_matrix
            vector = complex_vector

        # Our implementation.
        eigen_value, eigen_vector = power_iteration(input_matrix, vector)

        # Numpy implementation.

        # Get eigenvalues and eigenvectors using built-in numpy
        # eigh (eigh used for symmetric or hermetian matrices).
        eigen_values, eigen_vectors = np.linalg.eigh(input_matrix)
        # Last eigenvalue is the maximum one.
        eigen_value_max = eigen_values[-1]
        # Last column in this matrix is eigenvector corresponding to largest eigenvalue.
        eigen_vector_max = eigen_vectors[:, -1]

        # Check our implementation and numpy gives close answers.
        assert np.abs(eigen_value - eigen_value_max) <= 1e-6
        # Take absolute values element wise of each eigenvector.
        # as they are only unique to a minus sign.
        assert np.linalg.norm(np.abs(eigen_vector) - np.abs(eigen_vector_max)) <= 1e-6


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_power_iteration()
