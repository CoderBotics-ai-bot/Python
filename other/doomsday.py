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


def get_week_day(year: int, month: int, day: int) -> str:
    assert len(str(year)) > 2, "year should be in YYYY format"
    assert 1 <= month <= 12, "month should be between 1 to 12"
    assert 1 <= day <= 31, "day should be between 1 to 31"

    century = get_century(year)
    century_anchor = (5 * (century % 4) + 2) % 7
    centurian = get_centurian(year)
    centurian_m = centurian % 12
    dooms_day = (
        (centurian // 12) + centurian_m + (centurian_m // 4) + century_anchor
    ) % 7

    day_anchor = (
        DOOMSDAY_NOT_LEAP[month - 1]
        if not is_leap_year(year)
        else DOOMSDAY_LEAP[month - 1]
    )

    week_day = week_day_number(dooms_day, day, day_anchor)
    return WEEK_DAY_NAMES[week_day]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def get_century(year: int) -> int:
    """Function to get the century from year."""
    return year // 100


def get_centurian(year: int) -> int:
    """Function to get the centurian from year."""
    return year % 100


def is_leap_year(year: int) -> bool:
    """Function to check if a year is a leap year or not."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def week_day_number(dooms_day: int, day: int, day_anchor: int) -> int:
    """Function to calculate the week day number."""
    return (dooms_day + day - day_anchor) % 7
