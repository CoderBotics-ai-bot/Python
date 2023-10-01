

from itertools import groupby

def run_length_encode(text: str) -> list:
    """
    Performs Run Length Encoding on a string of characters.

    Args:
        text (str): A string of characters to encode.

    Returns:
        list: A list of tuples where each tuple represents an encoded sequence.
            The first element of the tuple is the character, and the second element is the number of times it repeats.

    Examples:
        >>> run_length_encode("AAAABBBCCDAA")
        [('A', 4), ('B', 3), ('C', 2), ('D', 1), ('A', 2)]
        >>> run_length_encode("A")
        [('A', 1)]
        >>> run_length_encode("AA")
        [('A', 2)]
        >>> run_length_encode("AAADDDDDDFFFCCCAAVVVV")
        [('A', 3), ('D', 6), ('F', 3), ('C', 3), ('A', 2), ('V', 4)]
    """
    # return empty list if text is None or empty
    if not text:
        return []

    # Using list comprehension and itertools to simplify the code
    return [(k, len(list(g))) for k, g in groupby(text)]


def run_length_decode(encoded: list) -> str:
    """
    Performs Run Length Decoding
    >>> run_length_decode([('A', 4), ('B', 3), ('C', 2), ('D', 1), ('A', 2)])
    'AAAABBBCCDAA'
    >>> run_length_decode([('A', 1)])
    'A'
    >>> run_length_decode([('A', 2)])
    'AA'
    >>> run_length_decode([('A', 3), ('D', 6), ('F', 3), ('C', 3), ('A', 2), ('V', 4)])
    'AAADDDDDDFFFCCCAAVVVV'
    """
    return "".join(char * length for char, length in encoded)


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="run_length_encode", verbose=True)
    testmod(name="run_length_decode", verbose=True)
