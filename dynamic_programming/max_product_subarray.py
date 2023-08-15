

def max_product_subarray(numbers: list[int]) -> int:
    """Refactored function to find max product in subarray"""
    if not numbers:
        return 0

    validate_input(numbers)

    max_till_now = min_till_now = max_prod = numbers[0]

    for number in numbers[1:]:
        max_till_now, min_till_now = update_current_products(
            number, max_till_now, min_till_now
        )
        max_prod = max(max_prod, max_till_now)

    return max_prod

def validate_input(numbers: list[int]) -> None:
    """
    Validates the input for the max_product_subarray function.
    Raises ValueError if the input is not a list of integers.
    """
    if not isinstance(numbers, (list, tuple)) or not all(
        isinstance(number, int) for number in numbers
    ):
        raise ValueError("numbers must be an iterable of integers")


def update_current_products(
    number: int, max_till_now: int, min_till_now: int
) -> tuple[int, int]:
    """
    Updates the current maximum and minimum products given a new number from the list.
    """
    if number < 0:
        max_till_now, min_till_now = min_till_now, max_till_now

    max_till_now = max(number, max_till_now * number)
    min_till_now = min(number, min_till_now * number)

    return max_till_now, min_till_now
