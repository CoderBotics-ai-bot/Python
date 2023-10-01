"""
Given an matrix of numbers in which all rows and all columns are sorted in decreasing
order, return the number of negative numbers in grid.

Reference: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
"""


from typing import List


def generate_large_matrix() -> list[list[int]]:
    """
    >>> generate_large_matrix() # doctest: +ELLIPSIS
    [[1000, ..., -999], [999, ..., -1001], ..., [2, ..., -1998]]
    """
    return [list(range(1000 - i, -1000 - i, -1)) for i in range(1000)]


grid = generate_large_matrix()
test_grids = (
    [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],
    [[3, 2], [1, 0]],
    [[7, 7, 6]],
    [[7, 7, 6], [-1, -2, -3]],
    grid,
)


def validate_grid(grid: list[list[int]]) -> None:
    """
    Validate that the rows and columns of the grid is sorted in decreasing order.
    >>> for grid in test_grids:
    ...     validate_grid(grid)
    """
    assert all(row == sorted(row, reverse=True) for row in grid)
    assert all(list(col) == sorted(col, reverse=True) for col in zip(*grid))

def find_negative_index(array: List[int]) -> int:
    """
    Find the index of the first negative number in a sorted integer array.

    This function uses a binary search algorithm for finding the index at which
    the first negative number occurs in a given list. The list/array must be
    sorted in non-descending order. If there is no negative number in the array,
    it returns the length of the array.

    The time complexity is O(log n), where n is the number of elements in the array.

    Args:
        array (List[int]): A sorted list of integers.

    Returns:
        int: The index of first negative number in the array. If there is no negative
             number, the function returns the length of the array.
    """
    if not array or array[0] < 0:
        return 0

    left = 0
    right = len(array) - 1

    while left < right:
        mid = (left + right) // 2
        if array[mid] < 0:
            right = mid
        else:
            left = mid + 1
    return left if array[left] < 0 else len(array)


def count_negatives_binary_search(grid: list[list[int]]) -> int:
    """
    An O(m logn) solution that uses binary search in order to find the boundary between
    positive and negative numbers

    >>> [count_negatives_binary_search(grid) for grid in test_grids]
    [8, 0, 0, 3, 1498500]
    """
    total = 0
    bound = len(grid[0])

    for i in range(len(grid)):
        bound = find_negative_index(grid[i][:bound])
        total += bound
    return (len(grid) * len(grid[0])) - total


def count_negatives_brute_force(grid: List[List[int]]) -> int:
    """
    Count the number of negative numbers in the given 2D grid.

    The function uses a brute force approach, scanning every element in the grid. As a result, its time complexity
    is O(n^2), where n is the number of elements in the grid.
    For a grid with only negative numbers, the function performs optimally. However, for a grid with only
    positive numbers, performance suffers as the algorithm checks each number individually.

    Args:
        grid (List[List[int]]): A 2D list of integers.

    Returns:
        int: The count of negative numbers in the grid.
    """
    return sum(count_negatives_in_row(row) for row in grid)

def count_negatives_brute_force_with_break(grid: List[List[int]]) -> int:
    """
    Similar to the brute force solution above but uses break in order to reduce the
    number of iterations.

    Args:
        grid (List[List[int]]): A 2D grid

    Returns:
        int: The total count of negative numbers in the grid.
    """

    total = 0
    for row in grid:
        try:
            first_negative_ind = next(i for i, x in enumerate(row) if x < 0)
        except StopIteration:
            continue

        total += len(row) - first_negative_ind

    return total

def count_negatives_in_row(row: List[int]) -> int:
    """
    Count the number of negative numbers in the list.

    Args:
        row (List[int]): An list of integers.

    Returns:
        int: The count of negative numbers in the list.
    """
    return sum(1 for i in row if i < 0)


def benchmark() -> None:
    """Benchmark our functions next to each other"""
    from timeit import timeit

    print("Running benchmarks")
    setup = (
        "from __main__ import count_negatives_binary_search, "
        "count_negatives_brute_force, count_negatives_brute_force_with_break, grid"
    )
    for func in (
        "count_negatives_binary_search",  # took 0.7727 seconds
        "count_negatives_brute_force_with_break",  # took 4.6505 seconds
        "count_negatives_brute_force",  # took 12.8160 seconds
    ):
        time = timeit(f"{func}(grid=grid)", setup=setup, number=500)
        print(f"{func}() took {time:0.4f} seconds")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
