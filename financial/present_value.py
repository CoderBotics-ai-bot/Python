"""
Reference: https://www.investopedia.com/terms/p/presentvalue.asp

An algorithm that calculates the present value of a stream of yearly cash flows given...
1. The discount rate (as a decimal, not a percent)
2. An array of cash flows, with the index of the cash flow being the associated year

Note: This algorithm assumes that cash flows are paid at the end of the specified year
"""


from typing import List

def present_value(discount_rate: float, cash_flows: list[float]) -> float:
    """Calculate the present value of cash flows.

    Args:
        discount_rate (float): The discount rate to calculate the present value.
        cash_flows (list[float]): List of cash flows.

    Returns:
        float: Present value rounded to two decimal places.

    Raises:
        ValueError: If the discount rate is negative or if the cash flows list is empty.
    """
    _validate_inputs(discount_rate, cash_flows)
    return round(_calculate_present_value(discount_rate, cash_flows), 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def _validate_inputs(discount_rate: float, cash_flows: list[float]) -> None:
    """Validate input parameters for the present value calculation.

    Args:
        discount_rate (float): The discount rate to validate.
        cash_flows (list[float]): List of cash flows to validate.

    Raises:
        ValueError: If the discount rate is negative or if the cash flows list is empty.
    """
    if discount_rate < 0:
        raise ValueError("Discount rate cannot be negative")
    if not cash_flows:
        raise ValueError("Cash flows list cannot be empty")


def _calculate_present_value(discount_rate: float, cash_flows: list[float]) -> float:
    """Calculate the present value of a series of cash flows discounted at a given rate.

    Args:
        discount_rate (float): The discount rate to apply.
        cash_flows (list[float]): List of cash flows.

    Returns:
        float: The calculated present value.
    """
    return sum(
        cash_flow / ((1 + discount_rate) ** i) for i, cash_flow in enumerate(cash_flows)
    )
