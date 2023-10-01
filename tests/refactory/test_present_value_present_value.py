from financial.present_value import *
import pytest


def test_present_value_no_errors():
    assert present_value(0.07, [10, 20.70, -293, 297]) is not None
    assert present_value(0.07, [-109129.39, 30923.23, 15098.93, 29734]) is not None
    assert present_value(0.07, [109129.39, 30923.23, 15098.93, 29734]) is not None


@pytest.mark.parametrize(
    "discount_rate, cash_flows",
    [(-1, [109129.39, 30923.23, 15098.93, 29734]), (0.03, [])],
)
def test_present_value_exceptions(discount_rate, cash_flows):
    with pytest.raises(ValueError):
        present_value(discount_rate, cash_flows)


def test_present_value_valid_responses():
    assert present_value(0.13, [10, 20.70, -293, 297]) == 4.69
