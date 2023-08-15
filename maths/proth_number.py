"""
Calculate the nth Proth number
Source:
    https://handwiki.org/wiki/Proth_number
"""

import math


def proth(number: int) -> int:
    """
    Calculate the nth Proth number. Indexing starts at 1. For example, proth(1) gives
    the first Proth number of 3.

    The Proth number refers to a series of integers of the form k * 2^n + 1 where
    k < 2^n and n > 0.

    A ValueError is raised if the number is less than 1, and a TypeError is raised
    for non-integer inputs.

    Args:
        number (int): The position in the sequence of Proth numbers to return. Must be a
        positive integer. Indexing starts at 1.

    Returns:
        int: The nth Proth number.

    Raises:
        ValueError: If 'number' is less than 1.
        TypeError: If 'number' is not an integer.

    Examples:
        >>> proth(6)
        25
        >>> proth(1)
        3
    """
    validate_inputs(number)
    if number == 1:
        return 3
    elif number == 2:
        return 5

    proth_numbers = [3, 5]
    for _ in range(3, number + 1):
        block = calculate_block_index(number)
        new_proth = 2 ** (block + 1) + proth_numbers[-1]
        proth_numbers.append(new_proth)
    return proth_numbers[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    for number in range(11):
        value = 0
        try:
            value = proth(number)
        except ValueError:
            print(f"ValueError: there is no {number}th Proth number")
            continue

        print(f"The {number}th Proth number: {value}")

def validate_inputs(number: int) -> None:
    """
    Helper function to validate the inputs for the Proth number calculation function.
    This function will raise appropriate exceptions if the input value of 'number' is
    not a positive integer.

    Args:
        number (int): The input value to validate

    Raises:
        ValueError: If 'number' is less than 1.
        TypeError: If 'number' is not an integer.
    """
    if not isinstance(number, int):
        raise TypeError(f"Input value of [number={number}] must be an integer")
    if number < 1:
        raise ValueError(f"Input value of [number={number}] must be > 0")


def calculate_block_index(number: int) -> int:
    """
    Helper function to calculate the block index used in the Proth number calculation.

    Args:
        number (int): The position in the sequence of Proth numbers.

    Returns:
        int: The calculated block index.
    """
    return int(math.log(number // 3 + 2, 2))
