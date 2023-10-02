from typing import List

def search(list_data: List[int], key: int, left: int = 0, right: int = 0) -> int:
    """
    Search for a key in the provided list using recursion.

    This function iterates through the provided list from both ends to find the index of the key.
    If the key is not present in the list, it returns -1. This function uses a recursive approach,
    where it checks for the key at the current indices from both ends, and if not found, it moves
    the indices inward and calls itself again.

    Args:
        list_data (List[int]): The list to search.
        key (int): The key to search for.
        left (int, optional): The starting index for the search. Defaults to 0.
        right (int, optional): The end index for the search. Defaults to 0, which means it will be set to len(list_data) - 1.

    Returns:
        int: The index of the key if found, else -1.

    Examples:
        >>> search(list(range(0, 11)), 5)
        5
        >>> search([1, 2, 4, 5, 3], 4)
        2
        >>> search([1, 2, 4, 5, 3], 6)
        -1
        >>> search([5], 5)
        0
        >>> search([], 1)
        -1
    """
    right = right or len(list_data) - 1
    if left > right:
        return -1
    if list_data[left] == key:
        return left
    if list_data[right] == key:
        return right
    return search(list_data, key, left + 1, right - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
