

from typing import List, Tuple

def cramers_rule_2x2(equation1: List[int], equation2: List[int]) -> Tuple[float, float]:
    """
    Solve a system of two linear equations using Cramer's Rule.

    Receives two lists containing three elements each representing the coefficients and constant term of a linear equation:

        ax1 + b1y = c1
        ax2 + b2y = c2

    Arguments:
    equation1: List[int] -- the coefficients and constant term (a1, b1, c1) of the first equation.
    equation2: List[int] -- the coefficients and constant term (a2, b2, c2) of the second equation.

    Returns:
    Tuple[float, float] -- the solution set (x, y) of the system of equations.

    Raises:
    ValueError: If the input equations are invalid or if the system does not have a unique solution.

    Example:

    cramers_rule_2x2([2, 3, 0], [5, 1, 0])
    Returns: (0.0, 0.0)

    cramers_rule_2x2([0, 4, 50], [2, 0, 26])
    Returns: (13.0, 12.5)

    cramers_rule_2x2([1, 2, 3], [2, 4, 6])
    Raises: ValueError("Infinite solutions. (Consistent system)")

    cramers_rule_2x2([1, 2, 3], [11, 22])
    Raises: ValueError("Please enter a valid equation.")

    cramers_rule_2x2([0, 0, 6], [0, 0, 3])
    Raises: ValueError("Both a & b of two equations can't be zero.")
    """

    # ... function body remains the same ...
