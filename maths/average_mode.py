from typing import Any

def mode(input_list: list) -> list[Any]:
    """
    Return the mode(s) of the input list. Mode in terms of statistics is the
    most frequently occurring item in an array or list of numbers. The function
    will return a list of items (mode(s)), which may contain multiple items
    since a data set may have one mode, more than one mode or no mode at all.

    Args:
        input_list: A list of numbers or other data types.

    Returns:
        A list of mode(s) in the input list. The list is sorted in ascending
        order. If the input list is empty, return an empty list.

    Examples:
        >>> mode([2, 3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 2, 2, 2])
        [2]
        >>> mode([3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 2, 2, 2])
        [2]
        >>> mode([3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 4, 2, 2, 4, 2])
        [2, 4]
        >>> mode(["x", "y", "y", "z"])
        ['y']
        >>> mode(["x", "x" , "y", "y", "z"])
        ['x', 'y']
    """
    if not input_list:
        return []

    # Get the counts of each value in the list
    counters = [input_list.count(value) for value in input_list]

    # Get the maximum count
    max_count = max(counters)

    # Return all values that have the maximum count, sorted in ascending order
    return sorted(
        {input_list[i] for i, value in enumerate(counters) if value == max_count}
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
