#!/bin/python3
# Doomsday algorithm info: https://en.wikipedia.org/wiki/Doomsday_rule

DOOMSDAY_LEAP = [4, 1, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
DOOMSDAY_NOT_LEAP = [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
WEEK_DAY_NAMES = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def get_week_day(year: int, month: int, day: int) -> str:
    """Returns the week-day name out of a given date.

    >>> get_week_day(2020, 10, 24)
    'Saturday'
    >>> get_week_day(2017, 10, 24)
    'Tuesday'
    >>> get_week_day(2019, 5, 3)
    'Friday'
    >>> get_week_day(1970, 9, 16)
    'Wednesday'
    >>> get_week_day(1870, 8, 13)
    'Saturday'
    >>> get_week_day(2040, 3, 14)
    'Wednesday'
    """
    validate_year(year)
    validate_month(month)
    validate_day(day)

    dooms_day = calculate_dooms_day(year)
    day_anchor = calculate_day_anchor(year, month)

    week_day = (dooms_day + day - day_anchor) % 7
    return WEEK_DAY_NAMES[week_day]


def validate_year(year: int) -> None:
    assert len(str(year)) > 2, "Year should be in YYYY format."


def validate_month(month: int) -> None:
    assert 1 <= month <= 12, "Month should be between 1 to 12."


def validate_day(day: int) -> None:
    assert 1 <= day <= 31, "Day should be between 1 to 31."


def calculate_dooms_day(year: int) -> int:
    century = year // 100
    century_anchor = (5 * (century % 4) + 2) % 7
    centurian = year % 100
    centurian_m = centurian % 12
    return ((centurian // 12) + centurian_m + (centurian_m // 4) + century_anchor) % 7


def calculate_day_anchor(year: int, month: int) -> int:
    if (year % 4 != 0) or (year % 100 == 0 and year % 400 == 0):
        return DOOMSDAY_NOT_LEAP[month - 1]
    return DOOMSDAY_LEAP[month - 1]
