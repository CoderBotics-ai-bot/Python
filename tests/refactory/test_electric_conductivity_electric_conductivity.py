import pytest
from electronics.electric_conductivity import *


# Test case to validate correct exception is raised when no parameters is zero
def test_electric_conductivity_value_error_no_zero_parameters():
    conductivity = 5
    electron_conc = 5
    mobility = 5
    with pytest.raises(ValueError, match=r".*cannot supply more or less than 2 values"):
        electric_conductivity(conductivity, electron_conc, mobility)


# Test case to validate correct exception is raised when more than one parameter is zero
def test_electric_conductivity_value_error_more_than_one_zero_parameters():
    conductivity = 0
    electron_conc = 0
    mobility = 5
    with pytest.raises(ValueError, match=r".*cannot supply more or less than 2 values"):
        electric_conductivity(conductivity, electron_conc, mobility)


# Test case to validate the function doesn't throw any errors when expecting to return conductivity
def test_electric_conductivity_is_calculating_conductivity():
    conductivity = 0
    electron_conc = 26
    mobility = 1.2
    result = electric_conductivity(conductivity, electron_conc, mobility)
    assert result is not None
    assert isinstance(result, tuple)
    assert result[0] == "conductivity"


# Test case to validate the function doesn't throw any errors when expecting to return electron concentration
def test_electric_conductivity_is_calculating_electron_concentration():
    conductivity = 2.5
    electron_conc = 0
    mobility = 1.3
    result = electric_conductivity(conductivity, electron_conc, mobility)
    assert result is not None
    assert isinstance(result, tuple)
    assert result[0] == "electron_conc"


# Test case to validate the function doesn't throw any errors when expecting to return electron mobility
def test_electric_conductivity_is_calculating_mobility():
    conductivity = 3.5
    electron_conc = 2.6
    mobility = 0
    result = electric_conductivity(conductivity, electron_conc, mobility)
    assert result is not None
    assert isinstance(result, tuple)
    assert result[0] == "mobility"
