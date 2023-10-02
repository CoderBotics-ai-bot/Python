from typing import List

def double_sort(lst: List[int]) -> List[int]:
    """
    The function sorts the input list using Python's built-in sort function.

    Args:
        lst (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list.

    Examples:
        >>> double_sort([-1, -2, -3, -4, -5, -6, -7])
        [-7, -6, -5, -4, -3, -2, -1]

        >>> double_sort([])
        []

        >>> double_sort([-1, -2, -3, -4, -5, -6])
        [-6, -5, -4, -3, -2, -1]

        >>> double_sort([-3, 10, 16, -42, 29]) == sorted([-3, 10, 16, -42, 29])
        True
    """
    lst.sort()
    return lst


if __name__ == "__main__":
    print("enter the list to be sorted")
    lst = [int(x) for x in input().split()]  # inputing elements of the list in one line
    sorted_lst = double_sort(lst)
    print("the sorted list is")
    print(sorted_lst)
