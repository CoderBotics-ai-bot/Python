"""A merge sort which accepts an array as input and recursively
splits an array in half and sorts and combines them.
"""

"""https://en.wikipedia.org/wiki/Merge_sort """

def merge(arr: list[int]) -> list[int]:
    """
    Functionality as the original `merge` function,
    Using helper functions `_merge` and `_merge_sort` to reduce complexity and improve readability.

    Args:
        arr (list[int]): Input list of integers.

    Returns:
        list[int]: Sorted version of input list using merge sort algorithm.
    """

    def _merge(left: list[int], right: list[int]) -> list[int]:
        """
        Merge two sorted lists into one sorted list.

        Args:
            left (list[int]): First sorted list.
            right (list[int]): Second sorted list.

        Returns:
            list[int]: Merged sorted list.
        """
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        return result + left + right

    def _merge_sort(lst: list[int]) -> list[int]:
        """
        Sort a list using merge sort algorithm.

        Args:
            lst (list[int]): Input list.

        Returns:
            list[int]: Sorted list.
        """
        if len(lst) <= 1:  # Guard condition to avoid unnecessary computation
            return lst

        mid = len(lst) // 2
        left = _merge_sort(lst[:mid])
        right = _merge_sort(lst[mid:])

        return _merge(left, right)

    return _merge_sort(arr)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
