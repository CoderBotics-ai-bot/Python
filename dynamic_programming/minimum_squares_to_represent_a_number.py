import math
import sys

def minimum_squares_to_represent_a_number(number: int) -> int:
    """
    Calculate the minimum count of perfect square numbers that sums up to the input number.
    """
    validate_input_number(number)

    # Initialize a list of size (number + 1) with maximum possible value (infinity)
    answers = initialize_answers(number)

    # Fill the answers list with min amount of squares for each number up to the input number
    answers = fill_answers(answers, number)

    return answers[number]


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def validate_input_number(number: int) -> None:
    """
    Validate the input number. Raise a ValueError if the input is invalid.
    """
    if number != int(number):
        raise ValueError("The value of the input must be a natural number")
    if number < 0:
        raise ValueError("The value of the input must not be a negative number")


def initialize_answers(number: int) -> list:
    """
    Initialize a list of answers with maximum possible value (infinity).
    """
    answers = [sys.maxsize] * (number + 1)
    answers[0] = 0  # 0 can be represented with 0 squares

    return answers


def fill_answers(answers: list, number: int) -> list:
    """
    Fill the answers list with the minimum amount of squares for each number up to the input number.
    """
    for i in range(1, number + 1):
        root = int(math.sqrt(i))
        for j in range(1, root + 1):
            current_answer = (
                1 + answers[i - (j**2)]
            )  # increment count of squares considering j^2 is used
            answers[i] = min(
                answers[i], current_answer
            )  # set minimum count in the answer list

    return answers
