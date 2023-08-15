""" Convert Base 10 (Decimal) Values to Hexadecimal Representations """

# set decimal value for each hexadecimal digit
values = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}

def decimal_to_hexadecimal(decimal: float) -> str:
    """
    Converts a decimal to hexadecimal representation.

    This function takes a float or integer value and returns a string representing the hexadecimal value.
    The returned string always begins with '0x'.
    The input should be equivalent to an integer. Floats that represent non-integer numbers or non-numeric types will raise an AssertionError.
    Negative values are also processed if they are equivalent to integers.

    Args:
        decimal: A float or integer to be converted.

    Returns:
        The hexadecimal representation of the decimal as a string.

    Raises:
        AssertionError: If an argument of an unsupported type is passed or the decimal argument contains a fractional component.

    Notes:
        This function behaves similarly to Python's built-in hex() function.

    Examples:

        >>> decimal_to_hexadecimal(5)
        '0x5'
        >>> decimal_to_hexadecimal(15)
        '0xf'
        >>> decimal_to_hexadecimal(37)
        '0x25'
        >>> decimal_to_hexadecimal(255)
        '0xff'
        >>> decimal_to_hexadecimal(4096)
        '0x1000'
        >>> decimal_to_hexadecimal(999098)
        '0xf3eba'
        >>> decimal_to_hexadecimal(-256)
        '-0x100'
        >>> decimal_to_hexadecimal(17.0)
        '0x11'
        >>> decimal_to_hexadecimal(-256) == hex(-256)
        True

    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
