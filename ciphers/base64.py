B64_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64_encode(data: bytes) -> bytes:
    """Encodes data according to RFC4648.

    The data is first transformed to binary and appended with binary digits so that its
    length becomes a multiple of 6, then each 6 binary digits will match a character in
    the B64_CHARSET string. The number of appended binary digits would later determine
    how many "=" signs should be added, the padding.
    For every 2 binary digits added, a "=" sign is added in the output.
    We can add any binary digits to make it a multiple of 6, for instance, consider the
    following example:
    "AA" -> 0010100100101001 -> 001010 010010 1001
    As can be seen above, 2 more binary digits should be added, so there's 4
    possibilities here: 00, 01, 10 or 11.
    That being said, Base64 encoding can be used in Steganography to hide data in these
    appended digits.

    >>> from base64 import b64encode
    >>> a = b"This pull request is part of Hacktoberfest20!"
    >>> b = b"https://tools.ietf.org/html/rfc4648"
    >>> c = b"A"
    >>> base64_encode(a) == b64encode(a)
    True
    >>> base64_encode(b) == b64encode(b)
    True
    >>> base64_encode(c) == b64encode(c)
    True
    >>> base64_encode("abc")
    Traceback (most recent call last):
      ...
    TypeError: a bytes-like object is required, not 'str'
    """
    # Make sure the supplied data is a bytes-like object
    if not isinstance(data, bytes):
        msg = f"a bytes-like object is required, not '{data.__class__.__name__}'"
        raise TypeError(msg)

    binary_stream = "".join(bin(byte)[2:].zfill(8) for byte in data)

    padding_needed = len(binary_stream) % 6 != 0

    if padding_needed:
        # The padding that will be added later
        padding = b"=" * ((6 - len(binary_stream) % 6) // 2)

        # Append binary_stream with arbitrary binary digits (0's by default) to make its
        # length a multiple of 6.
        binary_stream += "0" * (6 - len(binary_stream) % 6)
    else:
        padding = b""

    # Encode every 6 binary digits to their corresponding Base64 character
    return (
        "".join(
            B64_CHARSET[int(binary_stream[index : index + 6], 2)]
            for index in range(0, len(binary_stream), 6)
        ).encode()
        + padding
    )


def base64_decode(encoded_data: str) -> bytes:
    """
    Decodes a Base64 encoded string into bytes.

    Base64 encoding schemes are commonly used when there is a need to encode
    binary data, especially when that data needs to be stored and transferred
    over media that are designed to deal with text. This function implements
    the standard Base64 decoding scheme as defined in RFC 4648.

    This decoding scheme disregards all line feeds, carriage returns, spaces,
    and other whitespace characters found in the encoded data. Padding ("=")
    at end of the encoded data is also handled.

    Args:
        encoded_data: A string containing the Base64-encoded data.

    Returns:
        The original bytes representation of the Base64-encoded data.

    Raises:
        TypeError: If the input is not of type string or bytes.
        UnicodeDecodeError: If the input data is not ASCII.
        AssertionError: If the input contains non Base64 characters or incorrect padding.
    """
    if not isinstance(encoded_data, str):
        raise TypeError("Input must be a string")

    try:
        encoded_data = encoded_data.encode("ASCII")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("Input data is not ASCII")

    encoded_data = encoded_data.rstrip(b"=")
    encoded_data = validate_base64_padding(encoded_data)

    return extracted_data(encoded_data)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def validate_base64_padding(encoded_data: str) -> str:
    """
    Check if the padding of the encoded data is correct. If incorrect padding
    is detected, an exception is raised.

    Args:
        encoded_data: A string containing the Base64-encoded data.

    Returns:
        The original encoded data when the padding is correct.

    Raises:
        AssertionError: If the input contains incorrect padding.
    """
    padding = encoded_data.count("=")
    assert padding in [0, 2, 3], "Invalid padding in the Base64 data"

    return encoded_data


def extracted_data(encoded_data: str) -> bytes:
    """
    Extract data from base64 encoded string

    Args:
        encoded_data: A string containing the Base64-encoded data.

    Returns:
        The extracted byte sequence

    Raises:
        AssertionError: If the input contains non Base64 characters.
    """
    decoded_bytes = bytearray()
    for i in range(0, len(encoded_data), 4):
        num = (
            (B64_CHARSET.index(encoded_data[i]) << 18)
            + (B64_CHARSET.index(encoded_data[i + 1]) << 12)
            + (B64_CHARSET.index(encoded_data[i + 2]) << 6)
            + B64_CHARSET.index(encoded_data[i + 3])
        )
        decoded_bytes.extend((num >> 16 & 0xFF, num >> 8 & 0xFF, num & 0xFF))

    return decoded_bytes
