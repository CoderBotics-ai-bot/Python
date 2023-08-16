# https://en.wikipedia.org/wiki/Electrical_reactance#Inductive_reactance
from __future__ import annotations

from math import pi
from typing import Dict
PARAM_NAME_MAP = {
    "inductance": "Inductance",
    "frequency": "Frequency",
    "reactance": "Inductive reactance",
}


def ind_reactance(
    inductance: float, frequency: float, reactance: float
) -> dict[str, float]:
    params = {
        "inductance": inductance,
        "frequency": frequency,
        "reactance": reactance,
    }

    missing_param_name = get_zero_param(params)
    negative_param_name = get_negative_param(params)
    if missing_param_name is None:
        raise ValueError("One and only one argument must be 0")
    if negative_param_name is not None:
        raise ValueError(f"{PARAM_NAME_MAP[negative_param_name]} cannot be negative")

    result = calculate_missing_param(params, missing_param_name)

    return {missing_param_name: result}


if __name__ == "__main__":
    import doctest

    doctest.testmod()



def get_zero_param(params: dict) -> str:
    zero_param_names = [param for param, value in params.items() if value == 0]
    return zero_param_names[0] if len(zero_param_names) == 1 else None


def get_negative_param(params: dict) -> str:
    negative_param_names = [param for param, value in params.items() if value < 0]
    return negative_param_names[0] if negative_param_names else None


def calculate_missing_param(params: dict, missing_param_name: str) -> float:
    if missing_param_name == "inductance":
        return params["reactance"] / (2 * pi * params["frequency"])
    elif missing_param_name == "frequency":
        return params["reactance"] / (2 * pi * params["inductance"])
    else:  # missing_param_name == "reactance"
        return 2 * pi * params["frequency"] * params["inductance"]
