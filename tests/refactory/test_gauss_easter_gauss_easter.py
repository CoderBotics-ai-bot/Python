from other.gauss_easter import *
import pytest


def test_gauss_easter_no_errors():
    # Testing that the function doesn't throw errors when it gets executed.
    assert gauss_easter(2022) is not None
    assert gauss_easter(2023) is not None
    assert gauss_easter(2020) is not None
    assert gauss_easter(2021) is not None


def test_gauss_easter_leap_year():
    # Testing that the function returns a date in either March or April for a leap year
    leap_year = 2024
    easter = gauss_easter(leap_year)
    assert easter.year == leap_year
    assert easter.month in [3, 4]


def test_gauss_easter_non_leap_year():
    # Testing that the function returns a date in either March or April for a non-leap year
    non_leap_year = 2023
    easter = gauss_easter(non_leap_year)
    assert easter.year == non_leap_year
    assert easter.month in [3, 4]


def test_gauss_easter_invalid_input():
    # Testing that the function throws a TypeError when a non-integer year is provided
    with pytest.raises(TypeError):
        gauss_easter("2024")
    with pytest.raises(TypeError):
        gauss_easter(2024.0)
