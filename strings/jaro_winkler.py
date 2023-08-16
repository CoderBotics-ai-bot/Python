"""https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance"""

def jaro_winkler(str1: str, str2: str) -> float:
    """
    Compute the Jaro-Winkler similarity between two strings.

    The Jaro-Winkler similarity is a measure of similarity between two strings. It is a variant of the
    Jaro distance metric where it favors strings that match from the beginning. A prefix scale is decided
    and penalizes the strings accordingly.

    The Jaro–Winkler distance metric is designed and best suited for short strings such as person names,
    and to detect typos.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        float: The Jaro-Winkler similarity between `str1` and `str2`.

    Examples:
        >>> jaro_winkler("martha", "marhta")
        0.9611111111111111

        >>> jaro_winkler("CRATE", "TRACE")
        0.7333333333333334

        >>> jaro_winkler("test", "dbdbdbdb")
        0.0

        >>> jaro_winkler("test", "test")
        1.0

        >>> jaro_winkler("hello world", "HeLLo W0rlD")
        0.6363636363636364

        >>> jaro_winkler("test", "")
        0.0

        >>> jaro_winkler("hello", "world")
        0.4666666666666666

        >>> jaro_winkler("hell**o", "*world")
        0.4365079365079365
    """
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(jaro_winkler("hello", "world"))
