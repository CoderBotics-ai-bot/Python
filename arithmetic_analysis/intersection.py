import math
from collections.abc import Callable


from typing import Callable


def intersection(function: Callable[[float], float], x0: float, x1: float) -> float:
    """
    Calculate the intersection point (root) of a function using the secant method.
    """
    x_current = x0
    x_prev = x1
    while True:
        x_next = calculate_next_root(function, x_current, x_prev)
        if has_converged(x_current, x_next):
            return x_next

        x_prev = x_current
        x_current = x_next


def f(x: float) -> float:
    return math.pow(x, 3) - (2 * x) - 5

def calculate_next_root(
    function: Callable[[float], float], x_current: float, x_prev: float
) -> float:
    """Calculate the next approximation of the root.

    Args:
        function (Callable[[float], float]): The function for which the root is to be calculated.
        x_current (float): The current approximation of the root.
        x_prev (float): The previous approximation of the root.

    Returns:
        float: The next approximation of the root.

    Raises:
        ZeroDivisionError: If a root cannot be found due to division by zero during the iteration process.
    """
    try:
        return x_current - (
            function(x_current)
            / ((function(x_current) - function(x_prev)) / (x_current - x_prev))
        )
    except ZeroDivisionError:
        raise ZeroDivisionError("float division by zero, root not found")


def has_converged(x_current: float, x_next: float) -> bool:
    """Check if the calculation has converged.

    Args:
        x_current (float): The current approximation of the root.
        x_next (float): The next approximation of the root.

    Returns:
        bool: True if the calculation has converged, False otherwise.
    """
    return abs(x_next - x_current) < 10**-5


if __name__ == "__main__":
    print(intersection(f, 3, 3.5))
