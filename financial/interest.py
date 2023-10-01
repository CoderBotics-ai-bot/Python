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
    Calculate the compound interest.

    This function calculates the compound interest based on the principal amount,
    the nominal annual interest rate in percentage, and the number of compounding periods.

    Arguments:
    principal -- The initial amount of money that's been borrowed or invested.
    nominal_annual_interest_rate_percentage -- The nominal annual interest rate in percentage.
    number_of_compounding_periods -- The number of times that interest is compounded per time period.

    Returns:
    The compound interest, calculated based on the provided parameters.
    """
    _validate_principal(principal)
    _validate_interest_rate(nominal_annual_interest_rate_percentage)
    _validate_compounding_periods(number_of_compounding_periods)

    compound_interest = calculate_compound_interest(
        principal,
        nominal_annual_interest_rate_percentage,
        number_of_compounding_periods,
    )

    return compound_interest


def _validate_principal(principal: float) -> None:
    if principal <= 0:
        raise ValueError("'principal' must be greater than 0.")

def apr_interest(
    principal: float,
    nominal_annual_percentage_rate: float,
    number_of_years: float,
) -> float:
    """
    Calculate the Annual Percentage Rate (APR) interest.

    It calculates the APR interest based on the principal value, the nominal
    annual percentage rate, and the number of years. The nominal annual percentage
    rate is divided by 365 days to have it on a daily basis, and the number of years
    is also converted to days (multiplied by 365) to match the time span of the rate.

    Arguments:
    principal -- The initial amount of money that has been borrowed or invested.
    nominal_annual_percentage_rate -- The nominal annual percentage rate.
    number_of_years -- The number of years over which the investment or loan occurs.

    Returns:
    The APR interest, calculated based on the provided parameters.

    Raises:
    ValueError -- If number_of_years is less than or equal to 0,
                  If nominal_annual_percentage_rate is less than 0,
                  If principal is less than or equal to 0

    Examples:
    >>> apr_interest(10000.0, 0.05, 3)
    1618.223072263547
    >>> apr_interest(10000.0, 0.05, 1)
    512.6749646744732
    >>> apr_interest(0.5, 0.05, 3)
    0.08091115361317736
    """
    _validate_inputs(principal, nominal_annual_percentage_rate, number_of_years)

    return compound_interest(
        principal, nominal_annual_percentage_rate / 365, number_of_years * 365
    )


def _validate_interest_rate(nominal_annual_interest_rate_percentage: float) -> None:
    if nominal_annual_interest_rate_percentage < 0:
        raise ValueError("Interest rate must be >= 0")


def _validate_inputs(
    principal: float,
    nominal_annual_percentage_rate: float,
    number_of_years: float,
) -> None:
    if number_of_years <= 0:
        raise ValueError("number_of_years must be > 0")
    if nominal_annual_percentage_rate < 0:
        raise ValueError("nominal_annual_percentage_rate must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")


def _validate_compounding_periods(number_of_compounding_periods: float) -> None:
    if number_of_compounding_periods <= 0:
        raise ValueError("Number of compounding periods must be > 0")


def calculate_compound_interest(
    principal: float,
    nominal_annual_interest_rate_percentage: float,
    number_of_compounding_periods: float,
) -> float:
    return principal * (
        (1 + nominal_annual_interest_rate_percentage) ** number_of_compounding_periods
        - 1
    )


def _validate_daily_interest_rate(daily_interest_rate: float) -> None:
    if daily_interest_rate < 0:
        raise ValueError("'daily_interest_rate' must be equal or greater than 0.")


def _validate_days_between_payments(days_between_payments: float) -> None:
    if days_between_payments <= 0:
        raise ValueError("'days_between_payments' must be greater than 0.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
