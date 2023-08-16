import math
import sys

def minimum_squares_to_represent_a_number(number: int) -> int:
    """
    Calculate the minimum number of squares required to sum up to a given integer.

    This function uses the dynamic programming approach to calculate the minimum
    number of square numbers needed to sum up to the provided integer. The function
    starts from the smallest square number and keeps adding squares while
    maintaining the minimum squares required until it reaches the provided integer.
    If the provided number is not an integer or if it is a negative number, the
    function raises a ValueError.

    Args:
        number: An integer that is the sum of squares of other integers.

    Returns:
        The minimum number of square integers needed to sum up to the provided integer.

    Raises:
        ValueError: If the provided number is not an integer or if it is a
                    negative number.

    Examples:
        >>> minimum_squares_to_represent_a_number(25)
        1

        >>> minimum_squares_to_represent_a_number(37)
        2

        >>> minimum_squares_to_represent_a_number(21)
        3

        >>> minimum_squares_to_represent_a_number(58)
        2

        >>> minimum_squares_to_represent_a_number(0)
        1

        >>> minimum_squares_to_represent_a_number(12.34)
        Traceback (most recent call last):
            ...
        ValueError: the value of input must be a natural number

        >>> minimum_squares_to_represent_a_number(-1)
        Traceback (most recent call last):
            ...
        ValueError: the value of input must not be a negative number
    """

    if number != int(number):
        raise ValueError("the value of input must be a natural number")
    if number < 0:
        raise ValueError("the value of input must not be a negative number")
    if number == 0:
        return 1

    answers = [-1] * (number + 1)
    answers[0] = 0

    for i in range(1, number + 1):
        answer = sys.maxsize
        root = int(math.sqrt(i))

        for j in range(1, root + 1):
            current_answer = 1 + answers[i - (j**2)]
            answer = min(answer, current_answer)

        answers[i] = answer

    return answers[number]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
