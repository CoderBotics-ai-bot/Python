# https://www.investopedia.com

from __future__ import annotations

def simple_interest(
    principal: float, daily_interest_rate: float, days_between_payments: float
) -> float:
    """Calculate the simple interest.

    The function calculates the simple interest based on the principal amount, the daily interest rate
    and the number of days between payments.

    Args:
        principal (float): The principal amount.
        daily_interest_rate (float): The daily interest rate.
        days_between_payments (float): The number of days between payments.

    Returns:
        float: The calculated interest.

    Raises:
        ValueError:
            - If 'principal' is less than or equal to 0.
            - If 'daily_interest_rate' is less than 0.
            - If 'days_between_payments' is less than or equal to 0.
    """
    _validate_principal(principal)
    _validate_daily_interest_rate(daily_interest_rate)
    _validate_days_between_payments(days_between_payments)

    return principal * daily_interest_rate * days_between_payments


def compound_interest(
    principal: float,
    nominal_annual_interest_rate_percentage: float,
    number_of_compounding_periods: float,
) -> float:
    """
    >>> compound_interest(10000.0, 0.05, 3)
    1576.2500000000014
    >>> compound_interest(10000.0, 0.05, 1)
    500.00000000000045
    >>> compound_interest(0.5, 0.05, 3)
    0.07881250000000006
    >>> compound_interest(10000.0, 0.06, -4)
    Traceback (most recent call last):
        ...
    ValueError: number_of_compounding_periods must be > 0
    >>> compound_interest(10000.0, -3.5, 3.0)
    Traceback (most recent call last):
        ...
    ValueError: nominal_annual_interest_rate_percentage must be >= 0
    >>> compound_interest(-5500.0, 0.01, 5)
    Traceback (most recent call last):
        ...
    ValueError: principal must be > 0
    """
    if number_of_compounding_periods <= 0:
        raise ValueError("number_of_compounding_periods must be > 0")
    if nominal_annual_interest_rate_percentage < 0:
        raise ValueError("nominal_annual_interest_rate_percentage must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")

    return principal * (
        (1 + nominal_annual_interest_rate_percentage) ** number_of_compounding_periods
        - 1
    )


def _validate_principal(principal: float) -> None:
    if principal <= 0:
        raise ValueError("'principal' must be greater than 0.")


def _validate_daily_interest_rate(daily_interest_rate: float) -> None:
    if daily_interest_rate < 0:
        raise ValueError("'daily_interest_rate' must be equal or greater than 0.")


def _validate_days_between_payments(days_between_payments: float) -> None:
    if days_between_payments <= 0:
        raise ValueError("'days_between_payments' must be greater than 0.")


def apr_interest(
    principal: float,
    nominal_annual_percentage_rate: float,
    number_of_years: float,
) -> float:
    """
    >>> apr_interest(10000.0, 0.05, 3)
    1618.223072263547
    >>> apr_interest(10000.0, 0.05, 1)
    512.6749646744732
    >>> apr_interest(0.5, 0.05, 3)
    0.08091115361317736
    >>> apr_interest(10000.0, 0.06, -4)
    Traceback (most recent call last):
        ...
    ValueError: number_of_years must be > 0
    >>> apr_interest(10000.0, -3.5, 3.0)
    Traceback (most recent call last):
        ...
    ValueError: nominal_annual_percentage_rate must be >= 0
    >>> apr_interest(-5500.0, 0.01, 5)
    Traceback (most recent call last):
        ...
    ValueError: principal must be > 0
    """
    if number_of_years <= 0:
        raise ValueError("number_of_years must be > 0")
    if nominal_annual_percentage_rate < 0:
        raise ValueError("nominal_annual_percentage_rate must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")

    return compound_interest(
        principal, nominal_annual_percentage_rate / 365, number_of_years * 365
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
