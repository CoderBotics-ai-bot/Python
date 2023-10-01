from __future__ import annotations


from typing import List

ELECTRON_CHARGE = 1.6021e-19  # units = C


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def electric_conductivity(
    conductivity: float,
    electron_conc: float,
    mobility: float,
) -> tuple[str, float]:
    """Same description as given above."""
    parameters = [conductivity, electron_conc, mobility]
    labels = ["conductivity", "electron_conc", "mobility"]

    validate_inputs(parameters)

    if conductivity == 0:
        return (labels[0], mobility * electron_conc * ELECTRON_CHARGE)
    elif electron_conc == 0:
        return (labels[1], conductivity / (mobility * ELECTRON_CHARGE))
    else:
        return (labels[2], conductivity / (electron_conc * ELECTRON_CHARGE))

def validate_inputs(values: list[float]) -> None:
    """Check if inputs are valid."""
    if values.count(0) != 1:
        raise ValueError("You cannot supply more or less than 2 values")
    neg_val = [v < 0 for v in values]
    if any(neg_val):
        raise ValueError(f"{values[neg_val.index(True)]} cannot be negative")
