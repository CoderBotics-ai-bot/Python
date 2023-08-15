hex_table = {hex(i)[2:]: i for i in range(16)}  # Use [:2] to strip off the leading '0x'


def hex_to_decimal(hex_string: str) -> int:
    """
    Convert a hexadecimal string to its decimal equivalent.

    This function takes a string that represents a hexadecimal number
    and converts it into a decimal number. Leading and trailing whitespaces in the input
    are discarded. Negative hexadecimal numbers are supported, represented by a leading dash ("-").
    The function raises a ValueError if an empty string or a non-hexadecimal value is passed to it.

    Args:
        hex_string (str): A string representing the hexadecimal number.

    Returns:
        int: The decimal equivalent of the hexadecimal number.

    Raises:
        ValueError: If an empty string or a non-hexadecimal value is passed to the function.

    Examples:

        >>> hex_to_decimal("a")
        10

        >>> hex_to_decimal("12f")
        303

        >>> hex_to_decimal("   12f   ")
        303

        >>> hex_to_decimal("-Ff")
        -255

        >>> hex_to_decimal("F-f")
        ValueError: Non-hexadecimal value was passed to the function

        >>> hex_to_decimal("")
        ValueError: An empty string was passed to the function

        >>> hex_to_decimal("12m")
        ValueError: Non-hexadecimal value was passed to the function

    """
    hex_string = check_hex_string(hex_string)

    is_negative = hex_string[0] == "-"
    if is_negative:
        hex_string = hex_string[1:]

    return (
        -sum(16**i * hex_table[c] for i, c in enumerate(reversed(hex_string)))
        if is_negative
        else sum(16**i * hex_table[c] for i, c in enumerate(reversed(hex_string)))
    )


if __name__ == "__main__":
    from doctest import testmod

    testmod()

def check_hex_string(hex_string: str) -> str:
    """
    Validate and prepare a hexadecimal string for conversion.

    Args:
        hex_string (str): A string representing a hexadecimal number.

    Returns:
        str: Validated and normalized hexadecimal string.

    Raises:
        ValueError: If an empty string or a non-hexadecimal value is passed to the function.
    """

    hex_string = hex_string.strip().lower()
    if not hex_string:
        raise ValueError("Empty string was passed to the function")

    if not all(char in hex_table for char in hex_string.lstrip("-")):
        raise ValueError("Non-hexadecimal value was passed to the function")

    return hex_string
