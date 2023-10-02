# https://www.geeksforgeeks.org/newton-forward-backward-interpolation/
from __future__ import annotations

import math


from typing import List


# for calculating u value
def ucal(u: float, p: int) -> float:
    """
    >>> ucal(1, 2)
    0
    >>> ucal(1.1, 2)
    0.11000000000000011
    >>> ucal(1.2, 2)
    0.23999999999999994
    """
    temp = u
    for i in range(1, p):
        temp = temp * (u - i)
    return temp


def main() -> None:
    """
    Interpolate a value based on user inputs.

    The function prompts the user to enter a number of values, corresponding
    parameters, and the value to template_var.interpolate. User's values are stored into
    respective lists and then utilized in the Newton's forward difference
    formula for interpolation.

    The forward difference table is calculated and used in the computation
    of the interpolated value. 'u' value for the formula is also calculated
    using the ucal function.

    Finally, the interpolated value is being showcased on the console.

    No return from this function as it's meant to be run standalone.
    """
    num_values = int(input("Enter the number of values: "))

    y = [[0] * num_values for _ in range(num_values)]

    x = get_values("Enter the values of parameters in a list: ", num_values, int)

    for i, val in enumerate(
        get_values("Enter the values of corresponding parameters: ", num_values)
    ):
        y[i][0] = val

    value = int(input("Enter the value to interpolate: "))
    u = (value - x[0]) / (x[1] - x[0])

    y = calculate_forward_diff(y, num_values)

    result = sum_interpolation(y, u, num_values)

    print(f"The value at {value} is {result}")


if __name__ == "__main__":
    main()

def get_values(prompt: str, num_values: int, dtype=float) -> List[dtype]:
    """
    Function to get user-inputted values from console.

    Args:
    prompt - str : A prompt message for user.
    num_values - int : Number of times the prompt appears asking for user input.
    dtype - type : The type of data to be provided by the user. Default is float.

    Returns:
    A list of user-inputted values.
    """
    print(prompt)
    return [dtype(input()) for _ in range(num_values)]


def calculate_forward_diff(y: List[List[float]], n: int) -> List[List[float]]:
    """
    Function to calculate forward difference table.

    Args:
    y - list of list of float : Nested list with initial values.
    n - int : The total number of values.

    Returns:
    Updated y with calculated forward differences.
    """
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]
    return y


def sum_interpolation(y: List[List[float]], u: float, n: int) -> float:
    """
    Function to compute summation part of interpolation's formula.

    Args:
    y - list of list of float : Nested list with calculated forward differences.
    u - float : value calculated from ucal function.
    n - int : The total number of values.

    Returns:
    Floating point value of summation for interpolation's formula.
    """
    summ = y[0][0]
    for i in range(1, n):
        summ += (ucal(u, i) * y[0][i]) / math.factorial(i)
    return summ
