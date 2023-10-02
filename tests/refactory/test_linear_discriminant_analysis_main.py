import builtins
from machine_learning.linear_discriminant_analysis import *

import pytest
from unittest.mock import MagicMock
from typing import Any, Type, Union


def test_main_no_errors(monkeypatch: Any) -> None:
    """Test if main function can run without throwing any error"""
    inputs = ["2", "1.0", "2", "3", "1.0", "2.0", "q"]
    mock_input = MagicMock(side_effect=inputs)
    monkeypatch.setattr(builtins, "input", mock_input)
    main()


def test_main_function_execution_with_custom_inputs(monkeypatch: Any) -> None:
    """Test if main function runs with custom inputs"""
    inputs = ["2", "2.0", "3", "4", "1.5", "2.5", "q"]
    mock_input = MagicMock(side_effect=inputs)
    monkeypatch.setattr(builtins, "input", mock_input)
    main()
