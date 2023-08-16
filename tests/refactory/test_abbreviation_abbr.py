from dynamic_programming.abbreviation import *
import pytest


def test_abbr():
    # testing normal scenario
    assert abbr("daBcd", "ABC") is True
    assert abbr("dBcd", "ABC") is False

    # testing edge case for single letters
    assert abbr("A", "A") is True
    assert abbr("a", "A") is True

    # testing edge case for special characters
    assert abbr("@#", "!%") is False
    assert abbr("A@", "A!") is False

    # testing for all lowercase and uppercase
    assert abbr("abc", "ABC") is True

    # test with all uppercase in a and lowercase in b
    assert abbr("ABC", "abc") is False

    # test where ‘a’ can be abbreviated to ‘b’ or not
    assert abbr("ABBC", "ABC") is False
    assert abbr("ABBC", "ABBC") is True
