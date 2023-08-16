"""
render 3d points for 2d surfaces.
"""

from __future__ import annotations

import math

__version__ = "2020.9.26"
__author__ = "xcodz-dot, cclaus, dhruvmanila"


def convert_to_2d(
    x: float, y: float, z: float, scale: float, distance: float
) -> tuple[float, float]:
    """
    Converts 3d point to a 2d drawable point

    >>> convert_to_2d(1.0, 2.0, 3.0, 10.0, 10.0)
    (7.6923076923076925, 15.384615384615385)

    >>> convert_to_2d(1, 2, 3, 10, 10)
    (7.6923076923076925, 15.384615384615385)

    >>> convert_to_2d("1", 2, 3, 10, 10)  # '1' is str
    Traceback (most recent call last):
        ...
    TypeError: Input values must either be float or int: ['1', 2, 3, 10, 10]
    """
    if not all(isinstance(val, (float, int)) for val in locals().values()):
        msg = f"Input values must either be float or int: {list(locals().values())}"
        raise TypeError(msg)
    projected_x = ((x * distance) / (z + distance)) * scale
    projected_y = ((y * distance) / (z + distance)) * scale
    return projected_x, projected_y

def rotate(
    x: float, y: float, z: float, axis: str, angle: float
) -> tuple[float, float, float]:
    """
    Rotates a point around a certain axis by a certain angle.

    Args:
        x (float): x-coordinate of the point.
        y (float): y-coordinate of the point.
        z (float): z-coordinate of the point.
        axis (str): The axis around which the point will be rotated. Should be one of 'x', 'y', or 'z'.
        angle (float): The angle in degrees by which the point will be rotated.

    Returns:
        tuple[float, float, float]: The new coordinates of the point after rotation.

    Raises:
        TypeError: If the input values except axis are not float or int.
        ValueError: If the input axis is not one of 'x', 'y', or 'z'.

    The function first converts the input angle to radians and then based on the axis of rotation,
    calculates the new (x, y, z) coordinates of the point.

    >>> rotate(1.0, 2.0, 3.0, 'y', 90.0)
    (3.130524675073759, 2.0, 0.4470070007889556)

    >>> rotate(1, 2, 3, "z", 180)
    (0.999736015495891, -2.0001319704760485, 3)
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{convert_to_2d(1.0, 2.0, 3.0, 10.0, 10.0) = }")
    print(f"{rotate(1.0, 2.0, 3.0, 'y', 90.0) = }")
