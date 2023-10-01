

from typing import List, Tuple


def cramers_rule_2x2(equation1: list[int], equation2: list[int]) -> tuple[float, float]:
    """Solves a system of two linear equations in two variables using Cramer's rule."""

    check_validity(equation1, equation2)

    # Extract the coefficients
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2

    determinant, determinant_x, determinant_y = calculate_determinants(
        a1, b1, c1, a2, b2, c2
    )

    check_solution_exists(determinant, determinant_x, determinant_y)

    # Trivial solution (Inconsistent system)
    if determinant_x == determinant_y == 0:
        return (0.0, 0.0)

    # Non-Trivial Solution (Consistent system)
    x = determinant_x / determinant
    y = determinant_y / determinant
    return (x, y)

def check_validity(equation1: list[int], equation2: list[int]) -> None:
    """Checks if the input equations are valid"""
    if len(equation1) != 3 or len(equation2) != 3:
        raise ValueError("Please enter a valid equation.")
    if equation1[0] == equation1[1] == equation2[0] == equation2[1] == 0:
        raise ValueError("Both a & b of two equations can't be zero.")


def calculate_determinants(
    a1: int, b1: int, c1: int, a2: int, b2: int, c2: int
) -> tuple[int, int, int]:
    """Calculates the determinants of the matrices"""
    determinant = a1 * b2 - a2 * b1
    determinant_x = c1 * b2 - c2 * b1
    determinant_y = a1 * c2 - a2 * c1
    return determinant, determinant_x, determinant_y


def check_solution_exists(
    determinant: int, determinant_x: int, determinant_y: int
) -> None:
    """Checks if the system of linear equations has a solution (using Cramer's rule)"""
    if determinant == 0:
        if determinant_x == determinant_y == 0:
            raise ValueError("Infinite solutions. (Consistent system)")
        else:
            raise ValueError("No solution. (Inconsistent system)")
