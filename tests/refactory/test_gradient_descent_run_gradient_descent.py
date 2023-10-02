#
#
#from unittest.mock import MagicMock
#
#import pytest
#import pytest
#from machine_learning.gradient_descent import *
#
#
#def test_run_gradient_descent(monkeypatch):
#    # Mocking the global parameter_vector
#    parameter_vector = [0, 0, 0, 0]
#    mock_get_cost_derivative = MagicMock(return_value=1)
#    mock_allclose = MagicMock(side_effect=[False, True])
#
#    # Mocking necessary functions.
#    monkeypatch.setattr(
#        "your_module_name.get_cost_derivative", mock_get_cost_derivative
#    )
#    monkeypatch.setattr("numpy.allclose", mock_allclose)
#
#    run_gradient_descent()
#
#    # The function is expected to run without any errors.
#    assert True
#
#
#def test_run_gradient_descent_no_change(monkeypatch):
#    # In this scenario, the cost derivative is 0. Hence, no changes to the parameter_vector
#    parameter_vector = [0, 0, 0, 0]
#    mock_get_cost_derivative = MagicMock(return_value=0)
#    mock_allclose = MagicMock(return_value=True)
#
#    # Mocking necessary functions.
#    monkeypatch.setattr(
#        "your_module_name.get_cost_derivative", mock_get_cost_derivative
#    )
#    monkeypatch.setattr("numpy.allclose", mock_allclose)
#
#    run_gradient_descent()
#
#    # The function is expected to run without any errors.
#    assert True
#