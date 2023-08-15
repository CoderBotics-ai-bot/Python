from collections.abc import Callable


from typing import Callable, Optional


def bisection(function: Callable[[float], float], a: float, b: float) -> float:
    """
    The bisection method is a root-finding method that applies to any continuous function
    for which one knows two values with opposite signs.
    The method consists of repeatedly bisecting the interval defined by these values and
    then selecting the subinterval in which the function changes sign, and therefore must contain a root.

    Args:
        function: The function for which the root is to be determined.
        a: The lower limit of the interval.
        b: The upper limit of the interval.

    Returns:
        The root of the input function within the interval [a, b].

    Raises:
        ValueError: If the function does not have a root in the given interval.
    """
    root = validate_interval(function, a, b)
    if root is not None:
        return root
    return find_root(function, a, b)


def f(x: float) -> float:
    return x**3 - 2 * x - 5

def validate_interval(
    function: Callable[[float], float], a: float, b: float
) -> Optional[float]:
    """
    Validates the interval [a, b] for potential roots of `function`.

    Args:
        function: The function for which the root is to be determined.
        a: The lower limit of the interval.
        b: The upper limit of the interval.

    Returns:
        The value of `a` or `b` if either is a root of `function`,
        None if no guarantee of a root within the interval.

    Raises:
        ValueError: If the function does not have a root in the given interval.
    """
    if function(a) * function(b) > 0:
        raise ValueError("Could not find root in given interval.")
    if function(a) == 0:
        return a
    if function(b) == 0:
        return b
    return None


def find_root(
    function: Callable[[float], float], a: float, b: float, threshold: float = 10**-7
) -> float:
    """
    Finds a root of `function` within the interval [a, b] using the bisection method.

    Args:
        function: The function for which the root is to be determined.
        a: The lower limit of the interval.
        b: The upper limit of the interval.
        threshold: The precision level required for the root.

    Returns:
        The root of the function within the interval [a, b].
    """
    mid = a + (b - a) / 2.0
    while abs(a - mid) > threshold:
        mid = a + (b - a) / 2.0
        if function(mid) == 0:
            return mid
        if function(mid) * function(a) < 0:
            b = mid
        else:
            a = mid
    return mid


if __name__ == "__main__":
    print(bisection(f, 1, 1000))

    import doctest

    doctest.testmod()
