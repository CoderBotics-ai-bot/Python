

from typing import List


def points_to_polynomial(coordinates: List[List[int]]) -> str:
    """
    Takes a two-dimensional list containing x, y pairs of coordinates, maps them to an x-to-y power polynomial expression,
    and returns this expression as a string.

    Parameters
    ----------
    coordinates : list of list of int
        A two-dimensional list containing pairs of x, y integer coordinates.

    Returns
    -------
    str
        A string representing the polynomial expression obtained from the coordinates.

    Examples
    --------
    >>> points_to_polynomial([[1, 1], [2, 2], [3, 3]])
    'f(x)=x^2*0.0+x^1*1.0+x^0*0.0'

    >>> points_to_polynomial([[1, 3], [2, 6], [3, 11]])
    'f(x)=x^2*1.0+x^1*-0.0+x^0*2.0'
    """
    validate_coordinates(coordinates)

    len_coordinates = len(coordinates)
    polynomial_str = f"f(x)="
    for i in range(len_coordinates):
        a, b = coordinates[i][0], coordinates[i][1]
        power_to_coefficient = b / pow(a, len_coordinates)
        polynomial_str += f"x^{len_coordinates-i}*{power_to_coefficient}"
        if i != len_coordinates - 1:
            polynomial_str += "+"
    return polynomial_str


if __name__ == "__main__":
    print(points_to_polynomial([]))
    print(points_to_polynomial([[]]))
    print(points_to_polynomial([[1, 0], [2, 0], [3, 0]]))
    print(points_to_polynomial([[1, 1], [2, 1], [3, 1]]))
    print(points_to_polynomial([[1, 3], [2, 3], [3, 3]]))
    print(points_to_polynomial([[1, 1], [2, 2], [3, 3]]))
    print(points_to_polynomial([[1, 1], [2, 4], [3, 9]]))
    print(points_to_polynomial([[1, 3], [2, 6], [3, 11]]))
    print(points_to_polynomial([[1, -3], [2, -6], [3, -11]]))
    print(points_to_polynomial([[1, 5], [2, 2], [3, 9]]))

def validate_coordinates(coordinates: List[List[int]]) -> None:
    """
    Validates if the given coordinates are valid for polynomial transformation or not.

    Parameters
    ----------
    coordinates : list of list of int
        A two-dimensional list containing pairs of x, y integer coordinates.

    Raises
    ------
    ValueError
        If the supplied list is empty or contains entries that are not pairs.
        If the supplied list contains duplicate entries.
    """
    if not coordinates:
        raise ValueError("Empty coordinates list.")

    for i, coord in enumerate(coordinates):
        if len(coord) != 2:
            raise ValueError(f"Entry {coord} at index {i} is not a pair.")
        if coordinates.count(coord) > 1:
            raise ValueError(f"Duplicate entry {coord} at index {i}.")
