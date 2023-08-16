import operator


from typing import List

def strand_sort(input_list: List[int], reverse: bool = False) -> List[int]:
    """
    Implements the strand sort algorithm, which progressively extracts
    decreasing subsequences from the input, then merges them into the required order.
    The function uses Python's comparison operators for ordering.

    Args:
        input_list: Unordered list of integers.
        reverse (Optional): A flag that indicates whether to sort in descending order.
            Default is False, resulting in an ascending order sort.

    Examples:
        >>> strand_sort([4, 2, 5, 3, 0, 1])
        [0, 1, 2, 3, 4, 5]

        >>> strand_sort([4, 2, 5, 3, 0, 1], reverse=True)
        [5, 4, 3, 2, 1, 0]

    Returns:
        A sorted version of the input array according to the required order.
    """

    def merge(left: List[int], right: List[int]) -> List[int]:
        """
        Merges two lists in the required order.

        Args:
            left: Left sublist.
            right: Right sublist.

        Returns:
            A merged version of the two input sublists.
        """
        result = []
        while left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    if len(input_list) < 2:
        return input_list
    else:
        pivot, rest = input_list[0], input_list[1:]
        less = [x for x in rest if x <= pivot]
        greater = [x for x in rest if x > pivot]
        return merge(strand_sort(less, reverse), [pivot]) + strand_sort(
            greater, reverse
        )


if __name__ == "__main__":
    assert strand_sort([4, 3, 5, 1, 2]) == [1, 2, 3, 4, 5]
    assert strand_sort([4, 3, 5, 1, 2], reverse=True) == [5, 4, 3, 2, 1]
