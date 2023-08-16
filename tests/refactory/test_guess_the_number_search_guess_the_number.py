from other.guess_the_number_search import *
from unittest import mock

import pytest


from unittest import mock


def test_guess_the_number():
    with mock.patch("builtins.print") as mocked_print:
        guess_the_number(10, 1000, 17)
        calls = [
            mock.call("started..."),
            mock.call("guess the number : 17"),
            mock.call("details : [505, 257, 133, 71, 40, 25, 17]"),
        ]
        mocked_print.assert_has_calls(calls, any_order=True)


def test_guess_the_number_large_range():
    with mock.patch("builtins.print") as mocked_print:
        guess_the_number(-10000, 10000, 7)
        calls = [
            mock.call("started..."),
            mock.call("guess the number : 7"),
            mock.call(
                "details : [0, 5000, 2500, 1250, 625, 312, 156, 78, 39, 19, 9, 4, 6, 7]"
            ),
        ]
        mocked_print.assert_has_calls(calls, any_order=True)


def test_guess_the_number_non_int_to_guess():
    with pytest.raises(AssertionError, match='argument values must be type of "int"'):
        guess_the_number(10, 1000, "a")


def test_guess_the_number_out_of_range_to_guess():
    with pytest.raises(
        ValueError,
        match="guess value must be within the range of lower and higher value",
    ):
        guess_the_number(10, 1000, 5)


def test_guess_the_number_incorrect_lower_higher():
    with pytest.raises(
        ValueError,
        match="argument value for lower and higher must be\(lower > higher\)",
    ):
        guess_the_number(10000, 100, 5)
