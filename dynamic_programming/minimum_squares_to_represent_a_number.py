import math
import sys


from typing import List


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def minimum_squares_to_represent_a_number(number: int) -> int:
    """
    Counts the minimum number of squares needed to represent a number.

    Args:
        number (int): The input number.

    Returns:
        int: The minimum number of squares needed to represent the number.

    Raises:
        ValueError: If number is not a natural number.
    """
    validate_input(number)

    min_squares = [0]
    for i in range(1, number + 1):
        min_squares.append(compute_min_squares(i, min_squares))

    return min_squares[number] if number != 0 else 1


def compute_min_squares(num: int, min_squares: list) -> int:
    min_val = num
    j = 1
    while j * j <= num:
        min_val = min(min_val, 1 + min_squares[num - j * j])
        j += 1
    return min_val


def validate_input(number: int):
    if type(number) != int:
        raise ValueError("the value of input must be a natural number")
    elif number < 0:
        raise ValueError("the value of input must not be a negative number")
