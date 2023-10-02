"""Newton's Method."""


from typing import Callable

# Newton's Method - https://en.wikipedia.org/wiki/Newton%27s_method
from collections.abc import Callable

RealFunc = Callable[[float], float]  # type alias for a real -> real function

def newton(
    function: RealFunc,
    derivative: RealFunc,
    starting_int: int,
) -> float:
    """
    Apply Newton's method to find the root of a real-valued function near a given starting integer using
    an iterative process. If the derivative of the function at the current approximation and the estimate
    is less than the root, the function raises a ZeroDivisionError.

    Args:
        function: Callable function representing the real-valued function of a single variable.
        derivative: Callable function representing the derivative of the `function`.
        starting_int: An integer representing the starting value for the iterative process.

    Returns:
        float: The root of the function near the starting integer.

    Raises:
        ZeroDivisionError: If the derivative of the function at the current approximation
            to the root is zero.

    """
    prev_guess = make_float(starting_int)

    while True:
        next_guess = calculate_next_guess(prev_guess, function, derivative)

        if has_converged(prev_guess, next_guess):
            return next_guess

        prev_guess = next_guess


def f(x: float) -> float:
    return (x**3) - (2 * x) - 5


def make_float(number: int) -> float:
    """Converts the input integer to float"""
    return float(number)


def calculate_next_guess(
    guess: float, function: RealFunc, derivative: RealFunc
) -> float:
    """Calculates the next guess value using Newton's method"""
    try:
        return guess - function(guess) / derivative(guess)
    except ZeroDivisionError:
        raise ZeroDivisionError("Could not find root") from None


def has_converged(prev_guess: float, next_guess: float) -> bool:
    """Checks if the approximation has converged"""
    return abs(prev_guess - next_guess) < 10**-5


def f1(x: float) -> float:
    return 3 * (x**2) - 2


if __name__ == "__main__":
    print(newton(f, f1, 3))
