def print_pascal_triangle(num_rows: int) -> None:
    """
    Prints Pascal's triangle for a given number of rows.

    This method generates a triangle and then prints it out to the console.
    Each line of the triangle is printed on a new line, with padding so that
    the triangle is centered.

    Args:
        num_rows (int): The number of rows in the triangle. Must be a non-negative integer.

    Raises:
        TypeError: If num_rows is not an integer.
        ValueError: If num_rows is less than 0.

    Side Effects:
        Prints to standard output.

    Examples:
    >>> print_pascal_triangle(5)
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    """
    triangle = generate_pascal_triangle(num_rows)

    for row in triangle:
        print(" ".join(str(num) for num in row).center(num_rows * 2))
