from financial.interest import *
import pytest


import pytest


def test_apr_interest_no_error():
    assert apr_interest(10000.0, 0.05, 3) is not None


def test_apr_interest_zero_years():
    with pytest.raises(ValueError) as e:
        apr_interest(10000.0, 0.05, 0.0)
    assert str(e.value) == "number_of_years must be > 0"


def test_apr_interest_negative_years():
    with pytest.raises(ValueError) as e:
        apr_interest(10000.0, 0.05, -1.0)
    assert str(e.value) == "number_of_years must be > 0"


def test_apr_interest_zero_rate():
    assert apr_interest(10000.0, 0.0, 3.0) is not None


def test_apr_interest_negative_rate():
    with pytest.raises(ValueError) as e:
        apr_interest(10000.0, -0.05, 3.0)
    assert str(e.value) == "nominal_annual_percentage_rate must be >= 0"


def test_apr_interest_zero_principal():
    with pytest.raises(ValueError) as e:
        apr_interest(0.0, 0.05, 3.0)
    assert str(e.value) == "principal must be > 0"


def test_apr_interest_negative_principal():
    with pytest.raises(ValueError) as e:
        apr_interest(-10000.0, 0.05, 3.0)
    assert str(e.value) == "principal must be > 0"
