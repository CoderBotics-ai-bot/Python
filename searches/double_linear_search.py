from __future__ import annotations

def double_linear_search(array: list[int], search_item: int) -> int:
    """
    Conduct a double-ended linear search in an array for a specific item.

    Parameters:
    array (list[int]): The array to be searched.
    search_item (int): The item to be searched for.

    Returns:
    int: The index of the first found instance of the search item in the array;
         if not found or list is empty, returns -1.
    """
    if not array:  # return early when array is empty
        return -1

    start_ind, end_ind = 0, len(array) - 1

    while start_ind <= end_ind:
        if array[start_ind] == search_item:
            return start_ind
        if array[end_ind] == search_item:
            return end_ind
        start_ind += 1
        end_ind -= 1

    return -1


if __name__ == "__main__":
    print(double_linear_search(list(range(100)), 40))
