
## REFACTORED CODE:


def fizz_buzz(number: int, iterations: int) -> str:
    """
    Play the game of FizzBuzz. Begins with the given number and plays up to the number of iterations.
    """
    _validate_inputs(number, iterations)

    return (
        " ".join(_get_fizz_buzz_output(i) for i in range(number, number + iterations))
        + " "
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def _validate_inputs(number: int, iterations: int) -> None:
    """
    Validates input parameters for the FizzBuzz game.
    """
    if not isinstance(iterations, int):
        raise ValueError("Iterations must be defined as integers")
    if not isinstance(number, int) or number < 1:
        raise ValueError(
            "starting number must be\n                         and integer and be more than 0"
        )
    if iterations < 1:
        raise ValueError("Iterations must be done more than 0 times to play FizzBuzz")


def _get_fizz_buzz_output(number: int) -> str:
    """
    Determines the FizzBuzz output for a given number.
    """
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
