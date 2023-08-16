import numpy as np

def power_iteration(
    input_matrix: np.ndarray,
    vector: np.ndarray,
    error_tol: float = 1e-12,
    max_iterations: int = 100,
) -> tuple[float, np.ndarray]:
    """
    Implements the Power Iteration algorithm to find the largest eigenvalue and corresponding eigenvector of a given matrix.

    The Power Iteration method starts with a random vector to eventually converge to the principal eigenvector. Thus the input_matrix is multiplied by this vector iteratively.
    Convergence is determined by either the change in eigenvalue of successive iterations falling below the error_tolerance or exceeding the maximum number of iterations.
    The input matrix must either be a real or a Hermitian matrix.

    Args:
    input_matrix (np.ndarray): The input matrix, must be square and either real or Hermitian. Shape (N,N).
    vector (np.ndarray): The initial random vector in the same space as the matrix. Shape (N,)
    error_tol (float, optional): The error tolerance for the change in the eigenvalue of each iteration. Default is 1e-12.
    max_iterations (int, optional): The maximum number of iterations the algorithm will run. Default is 100.

    Returns:
    tuple: A tuple containing two elements.
            The first element is the largest eigenvalue of the input_matrix as a float.
            The second element is the corresponding eigenvector as a numpy array.

    Raises:
    AssertionError: If input_matrix is not square.
                     If the dimensions of the input_matrix and vector do not match.
                     If the input_matrix and the vector are not both complex or both real.
                     If the complex input_matrix is not a Hermitian matrix.

    Example:
    >>> import numpy as np
    >>> input_matrix = np.array([
    ... [41,  4, 20],
    ... [ 4, 26, 30],
    ... [20, 30, 50]
    ... ])
    >>> vector = np.array([41,4,20])
    >>> power_iteration(input_matrix,vector)
    (79.66086378788381, array([0.44472726, 0.46209842, 0.76725662]))
    """


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
