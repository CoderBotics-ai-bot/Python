import pytest
from other.doomsday import *


import pytest


def test_get_week_day_no_errors():
    result = get_week_day(2020, 12, 31)
    assert result is not None


def test_get_week_day_correct_years():
    assert len(str(2020)) > 2
    assert len(str(1900)) > 2
    assert len(str(1800)) > 2


def test_get_week_day_incorrect_years():
    with pytest.raises(AssertionError):
        get_week_day(20, 1, 1)
    with pytest.raises(AssertionError):
        get_week_day(99, 1, 1)


def test_get_week_day_correct_months():
    for month in range(1, 13):
        assert get_week_day(2022, month, 1) is not None


def test_get_week_day_incorrect_months():
    with pytest.raises(AssertionError):
        get_week_day(2022, 0, 1)
    with pytest.raises(AssertionError):
        get_week_day(2022, 13, 1)


def test_get_week_day_correct_days():
    for day in range(1, 32):
        assert get_week_day(2020, 1, day) is not None


def test_get_week_day_incorrect_days():
    with pytest.raises(AssertionError):
        get_week_day(2020, 1, 0)
    with pytest.raises(AssertionError):
        get_week_day(2020, 1, 32)
