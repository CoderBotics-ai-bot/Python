def generate_pascal_triangle(num_rows: int) -> list[list[int]]:
    """Refactored version of generate_pascal_triangle."""
    check_num_rows(num_rows)

    triangle: list[list[int]] = []
    for current_row_idx in range(num_rows):
        triangle.append(populate_current_row(triangle, current_row_idx))

    return triangle


def check_num_rows(num_rows: int) -> None:
    if not isinstance(num_rows, int):
        raise TypeError("The input value of 'num_rows' should be 'int'")
    elif num_rows < 0:
        raise ValueError(
            "The input value of 'num_rows' should be greater than or equal to 0"
        )


def populate_current_row(triangle: list[list[int]], current_row_idx: int) -> list[int]:
    if current_row_idx == 0:
        return [1]
    previous_row = triangle[current_row_idx - 1]
    current_row = (
        [1]
        + [previous_row[i - 1] + previous_row[i] for i in range(1, current_row_idx)]
        + [1]
    )
    return current_row


from typing import List
