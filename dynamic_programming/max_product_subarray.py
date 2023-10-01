

from typing import List

def max_product_subarray(numbers: list[int]) -> int:
    """
    Returns the maximal product that can be obtained by multiplying a
    contiguous subarray within the given integer list 'numbers'.

    Args:
        numbers (list[int]): List of integers.

    Returns:
        int: The maximal product that can be obtained by multiplying a
        contiguous subarray within the given integer list.

    Examples:
        >>> max_product_subarray([2, 3, -2, 4])
        6
        >>> max_product_subarray((-2, 0, -1))
        0
        >>> max_product_subarray([2, 3, -2, 4, -1])
        48
        >>> max_product_subarray([-1])
        -1
        >>> max_product_subarray([0])
        0
        >>> max_product_subarray([])
        0
    """
    verify_input(numbers)
    return find_max_product(numbers)


def verify_input(numbers: list[int]) -> None:
    if not isinstance(numbers, (list, tuple)) or not all(
        isinstance(number, int) for number in numbers
    ):
        raise ValueError("numbers must be an iterable of integers")


def find_max_product(numbers: list[int]) -> int:
    if not numbers:
        return 0

    max_till_now = min_till_now = max_prod = numbers[0]

    for number in numbers[1:]:
        max_till_now, min_till_now = (
            (max(number, max_till_now * number), min(number, min_till_now * number))
            if number >= 0
            else (
                max(number, min_till_now * number),
                min(number, max_till_now * number),
            )
        )
        max_prod = max(max_prod, max_till_now)

    return max_prod
