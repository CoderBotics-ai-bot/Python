

def multiplicative_persistence(num: int) -> int:
    """
    Computes and returns the multiplicative persistence of a given number.

    Multiplicative Persistence is defined as the number of times you must multiply
    the digits in num until you reach a single digit.

    Args:
        num(int): The number for which to calculate the multiplicative persistence.
        The number must be a positive integer.

    Returns:
        int: The multiplicative persistence of the number.

    Raises:
        ValueError: If num is not an integral value.
        ValueError: If num is a negative value.

    Examples:
        >>> multiplicative_persistence(217)
        2
    """

    if not isinstance(num, int):
        raise ValueError("multiplicative_persistence() only accepts integral values")
    if num < 0:
        raise ValueError("multiplicative_persistence() does not accept negative values")

    steps = 0
    while num >= 10:
        num = product_of_digits(num)
        steps += 1
    return steps


def additive_persistence(num: int) -> int:
    """
    Return the persistence of a given number.

    https://en.wikipedia.org/wiki/Persistence_of_a_number

    >>> additive_persistence(199)
    3
    >>> additive_persistence(-1)
    Traceback (most recent call last):
        ...
    ValueError: additive_persistence() does not accept negative values
    >>> additive_persistence("long number")
    Traceback (most recent call last):
        ...
    ValueError: additive_persistence() only accepts integral values
    """

    if not isinstance(num, int):
        raise ValueError("additive_persistence() only accepts integral values")
    if num < 0:
        raise ValueError("additive_persistence() does not accept negative values")

    steps = 0
    num_string = str(num)

    while len(num_string) != 1:
        numbers = [int(i) for i in num_string]

        total = 0
        for i in range(0, len(numbers)):
            total += numbers[i]

        num_string = str(total)

        steps += 1
    return steps

def product_of_digits(num: int) -> int:
    """
    Computes the product of digits of a given number.

    Args:
        num(int): The number of which to compute the product of its digits.
        The number must be a positive integer.

    Returns:
        int: The product of digits of the number.

    """
    total = 1
    for digit in str(num):
        total *= int(digit)
    return total


if __name__ == "__main__":
    import doctest

    doctest.testmod()
