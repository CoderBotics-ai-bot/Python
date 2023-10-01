"""
This implementation demonstrates how to generate the elements of a Pascal's triangle.
The element havingva row index of r and column index of c can be derivedvas follows:
triangle[r][c] = triangle[r-1][c-1]+triangle[r-1][c]

A Pascal's triangle is a triangular array containing binomial coefficients.
https://en.wikipedia.org/wiki/Pascal%27s_triangle
"""

def print_pascal_triangle(num_rows: int) -> None:
    """
    Prints a formatted Pascal's triangle for a given number of rows.

    The function takes an integer as input which represents the number of rows in the Pascal's triangle.
    It generates the Pascal's triangle using the `generate_pascal_triangle` function, then prints it
    in a triangle format where each value is separated by a space and each row is centered.

    Args:
        num_rows (int): The number of rows in the Pascal's triangle.

    Returns:
        None

    Raises:
        TypeError: An error occurs if the input argument is not of 'int' type.
        ValueError: An error occurs if the input value is less than zero.

    Doctest:
        >>> print_pascal_triangle(5)
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
    """
    triangle = generate_pascal_triangle(num_rows)
    max_len = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_len))

def generate_pascal_triangle(num_rows: int) -> list[list[int]]:
    """
    Generate the Pascal's Triangle for a given number of rows.

    Pascal's Triangle has a property where each number is a sum of the two numbers directly above it.
    This function generates the Pascal's Triangle for different number of rows depending on the input.

    Args:
        num_rows (int): The number of rows in Pascal's Triangle one wants to generate.
        It should be a non-negative integer. If it's 0, an empty list is returned.

    Returns:
        list[list[int]]: A list of lists of integers representing Pascal's Triangle.
        Each top-level list represents a row in the triangle, and the number of integers
        in a single row equals to the index of this row plus one (indexing from 0).

    Raises:
        TypeError: If the input 'num_rows' is not an integer.
        ValueError: If number of rows is negative.

    Examples:
    >>> generate_pascal_triangle(0)
    []
    >>> generate_pascal_triangle(1)
    [[1]]
    >>> generate_pascal_triangle(2)
    [[1], [1, 1]]
    >>> generate_pascal_triangle(3)
    [[1], [1, 1], [1, 2, 1]]
    >>> generate_pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if not isinstance(num_rows, int):
        raise TypeError("The input value of 'num_rows' should be 'int'")
    if num_rows < 0:
        raise ValueError(
            "The input value of 'num_rows' should be greater than or equal to 0"
        )

    if num_rows == 0:
        return []

    triangle: list[list[int]] = [[1]]
    for current_row_idx in range(1, num_rows):
        current_row = populate_current_row(triangle, current_row_idx)
        triangle.append(current_row)

    return triangle


def populate_current_row(triangle: list[list[int]], current_row_idx: int) -> list[int]:
    """
    >>> triangle = [[1]]
    >>> populate_current_row(triangle, 1)
    [1, 1]
    """
    current_row = [-1] * (current_row_idx + 1)
    # first and last elements of current row are equal to 1
    current_row[0], current_row[-1] = 1, 1
    for current_col_idx in range(1, current_row_idx):
        calculate_current_element(
            triangle, current_row, current_row_idx, current_col_idx
        )
    return current_row


def calculate_current_element(
    triangle: list[list[int]],
    current_row: list[int],
    current_row_idx: int,
    current_col_idx: int,
) -> None:
    """
    >>> triangle = [[1], [1, 1]]
    >>> current_row = [1, -1, 1]
    >>> calculate_current_element(triangle, current_row, 2, 1)
    >>> current_row
    [1, 2, 1]
    """
    above_to_left_elt = triangle[current_row_idx - 1][current_col_idx - 1]
    above_to_right_elt = triangle[current_row_idx - 1][current_col_idx]
    current_row[current_col_idx] = above_to_left_elt + above_to_right_elt


def generate_pascal_triangle_optimized(num_rows: int) -> list[list[int]]:
    """
    This function returns a matrix representing the corresponding pascal's triangle
    according to the given input of number of rows of Pascal's triangle to be generated.
    It reduces the operations done to generate a row by half
    by eliminating redundant calculations.

    :param num_rows: Integer specifying the number of rows in the Pascal's triangle
    :return: 2-D List (matrix) representing the Pascal's triangle

    Return the Pascal's triangle of given rows
    >>> generate_pascal_triangle_optimized(3)
    [[1], [1, 1], [1, 2, 1]]
    >>> generate_pascal_triangle_optimized(1)
    [[1]]
    >>> generate_pascal_triangle_optimized(0)
    []
    >>> generate_pascal_triangle_optimized(-5)
    Traceback (most recent call last):
        ...
    ValueError: The input value of 'num_rows' should be greater than or equal to 0
    >>> generate_pascal_triangle_optimized(7.89)
    Traceback (most recent call last):
        ...
    TypeError: The input value of 'num_rows' should be 'int'
    """

    if not isinstance(num_rows, int):
        raise TypeError("The input value of 'num_rows' should be 'int'")

    if num_rows == 0:
        return []
    elif num_rows < 0:
        raise ValueError(
            "The input value of 'num_rows' should be greater than or equal to 0"
        )

    result: list[list[int]] = [[1]]

    for row_index in range(1, num_rows):
        temp_row = [0] + result[-1] + [0]
        row_length = row_index + 1
        # Calculate the number of distinct elements in a row
        distinct_elements = sum(divmod(row_length, 2))
        row_first_half = [
            temp_row[i - 1] + temp_row[i] for i in range(1, distinct_elements + 1)
        ]
        row_second_half = row_first_half[: (row_index + 1) // 2]
        row_second_half.reverse()
        row = row_first_half + row_second_half
        result.append(row)

    return result


def benchmark() -> None:
    """
    Benchmark multiple functions, with three different length int values.
    """
    from collections.abc import Callable
    from timeit import timeit

    def benchmark_a_function(func: Callable, value: int) -> None:
        call = f"{func.__name__}({value})"
        timing = timeit(f"__main__.{call}", setup="import __main__")
        # print(f"{call:38} = {func(value)} -- {timing:.4f} seconds")
        print(f"{call:38} -- {timing:.4f} seconds")

    for value in range(15):  # (1, 7, 14):
        for func in (generate_pascal_triangle, generate_pascal_triangle_optimized):
            benchmark_a_function(func, value)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
