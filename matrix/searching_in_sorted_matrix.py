from __future__ import annotations


from typing import List
from typing import List, Tuple


from typing import Tuple



def search_in_a_sorted_matrix(mat: List[List[int]], m: int, n: int, key: float) -> None:
    """
    The main function to search the target key in the sorted matrix
    """
    coordinates = _find_key_coordinates(mat, m, n, key)

    if coordinates:
        i, j = coordinates
        print(f"Key {key} found at row- {i + 1} column- {j + 1}")
    else:
        print(f"Key {key} not found")


def main() -> None:
    mat = [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]]
    x = int(input("Enter the element to be searched:"))
    print(mat)
    search_in_a_sorted_matrix(mat, len(mat), len(mat[0]), x)


def _find_key_coordinates(
    mat: List[List[int]], m: int, n: int, key: float
) -> Tuple[int, int]:
    """
    A helper function to find the coordinates of the target key in the sorted matrix.
    It returns a tuple (i, j) if the key is found; otherwise, it returns None
    """
    i, j = m - 1, 0
    while _is_valid_coordinate(i, j, m, n):
        if _is_equal_key(mat, i, j, key):
            return i, j
        i, j = _get_next_coordinate(mat, i, j, key)
    return None


def _is_valid_coordinate(i: int, j: int, m: int, n: int) -> bool:
    """
    A helper function to check if the current coordinates (i, j) are valid in the given matrix
    """
    return 0 <= i < m and 0 <= j < n


def _is_equal_key(mat: List[List[int]], i: int, j: int, key: float) -> bool:
    """
    A helper function to check if the current cell is equal to the target key
    """
    return mat[i][j] == key


def _get_next_coordinate(
    mat: List[List[int]], i: int, j: int, key: float
) -> Tuple[int, int]:
    """
    A helper function to get the next searching coordinates based on the current value and the target key
    """
    return (i - 1, j) if key < mat[i][j] else (i, j + 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
