"""
https://cp-algorithms.com/string/z-function.html

Z-function or Z algorithm

Efficient algorithm for pattern occurrence in a string

Time Complexity: O(n) - where n is the length of the string

"""


from typing import Any

def z_function(input_str: str) -> list[int]:
    """
    Compute the Z-values for each index of the provided string.

    For each index in the string, the Z-value represents the maximal length of the substring starting from the index that
    is the same as the prefix of the same length.

    The first element of the computed array is always 0, given that substring of length 0 has no meaningful comparison.

    Parameters:
    ------------
    input_str : str
        The input string for which the Z-values are to be computed.

    Returns:
    --------
    list[int]
        A list of integers where each integer at index 'i' represents the Z-value for the 'i-th' character in the input string.

    Raises:
    ------
    TypeError
        For non-string inputs.

    Examples:
    --------
    >>> z_function("abracadabra")
    [0, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1]

    >>> z_function("aaaa")
    [0, 3, 2, 1]

    >>> z_function("zxxzxxz")
    [0, 0, 0, 4, 0, 0, 1]
    """
    check_input_type(input_str)

    z_result = init_z_values(len(input_str))
    left_pointer, right_pointer = 0, 0

    for i in range(1, len(input_str)):
        if is_within_interval(i, right_pointer):
            z_result[i] = get_min_edge(i, left_pointer, right_pointer, z_result)

        while go_next(i, z_result, input_str):
            increment_z_value(i, z_result)

        if extends_interval(i, right_pointer, z_result):
            left_pointer, right_pointer = update_pointers(i, z_result)

    return z_result


def go_next(i: int, z_result: list[int], s: str) -> bool:
    """
    Check if we have to move forward to the next characters or not
    """
    return i + z_result[i] < len(s) and s[z_result[i]] == s[i + z_result[i]]


def check_input_type(input_str: Any) -> None:
    """Check if input is a string."""
    if not isinstance(input_str, str):
        raise TypeError("Input must be of string type.")


def init_z_values(length: int) -> list[int]:
    """Initialize Z-values."""
    return [0 for _ in range(length)]


def is_within_interval(current_index: int, right_pointer: int) -> bool:
    """Check if current index is within the Z-algorithm interval."""
    return current_index <= right_pointer


def get_min_edge(
    current_index: int, left_pointer: int, right_pointer: int, z_values: list[int]
) -> int:
    """Calculate minimum edge of Z-algorithm interval."""
    return min(
        right_pointer - current_index + 1, z_values[current_index - left_pointer]
    )


def increment_z_value(current_index: int, z_values: list[int]) -> None:
    """Increment Z-value at current index."""
    z_values[current_index] += 1


def extends_interval(
    current_index: int, right_pointer: int, z_values: list[int]
) -> bool:
    """Check if current Z-value extends Z-algorithm interval."""
    return current_index + z_values[current_index] - 1 > right_pointer


def update_pointers(current_index: int, z_values: list[int]) -> tuple:
    """Update Z-algorithm interval pointers."""
    return current_index, current_index + z_values[current_index] - 1


def find_pattern(pattern: str, input_str: str) -> int:
    """
    Example of using z-function for pattern occurrence
    Given function returns the number of times 'pattern'
    appears in 'input_str' as a substring

    >>> find_pattern("abr", "abracadabra")
    2
    >>> find_pattern("a", "aaaa")
    4
    >>> find_pattern("xz", "zxxzxxz")
    2
    """
    answer = 0
    # concatenate 'pattern' and 'input_str' and call z_function
    # with concatenated string
    z_result = z_function(pattern + input_str)

    for val in z_result:
        # if value is greater then length of the pattern string
        # that means this index is starting position of substring
        # which is equal to pattern string
        if val >= len(pattern):
            answer += 1

    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
