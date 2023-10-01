import pytest
from dynamic_programming.fizz_buzz import *


def test_fizz_buzz():
    result = fizz_buzz(1, 15)
    assert result is not None


@pytest.mark.parametrize("number, iterations", [(1.5, 5), ("1", 5), (1, "5"), (1, 5.5)])
def test_fizz_buzz_with_invalid_inputs(number, iterations):
    with pytest.raises(ValueError):
        fizz_buzz(number, iterations)


def test_fizz_buzz_with_zero_iterations():
    with pytest.raises(ValueError) as e_info:
        fizz_buzz(1, 0)
    assert (
        str(e_info.value)
        == "Iterations must be done more than 0 times to play FizzBuzz"
    )


def test_fizz_buzz_with_negative_starting_number():
    with pytest.raises(ValueError) as e_info:
        fizz_buzz(-5, 5)
    assert (
        str(e_info.value)
        == "starting number must be\n                         and integer and be more than 0"
    )
