"""
Pure Python implementation of a binary search algorithm.

For doctests run following command:
python3 -m doctest -v simple_binary_search.py

For manual testing run:
python3 simple_binary_search.py
"""
from __future__ import annotations

def binary_search(a_list: list[int], item: int) -> bool:
    """Search for item in sorted list a_list using binary search.

    Args:
        a_list: Sorted list to search.
        item: Item to search for.

    Returns:
        True if item is found, False otherwise.
    """
    return _binary_search(a_list, item, 0, len(a_list) - 1)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item.strip()) for item in user_input.split(",")]
    target = int(input("Enter the number to be found in the list:\n").strip())
    not_str = "" if binary_search(sequence, target) else "not "
    print(f"{target} was {not_str}found in {sequence}")


def _binary_search(a_list: list[int], item: int, left: int, right: int) -> bool:
    """Recursive helper function for binary_search."""
    if right >= left:
        midpoint = (right + left) // 2
        if a_list[midpoint] == item:
            return True
        if a_list[midpoint] > item:
            return _binary_search(a_list, item, left, midpoint - 1)
        return _binary_search(a_list, item, midpoint + 1, right)
    return False
