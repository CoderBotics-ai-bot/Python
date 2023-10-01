from collections.abc import Sequence


from typing import Sequence

def max_subsequence_sum(nums: Sequence[int] | None = None) -> int:
    """
    Computes the maximum subsequence sum of a given sequence of integers.

    The function throws a ValueError exception if the input sequence is None or empty.
    It utilizes a dynamic programming approach to calculate the sum of non-empty subsequences
    of the input array. It iteratively keeps track of the maximum sum so far and updates it
    accordingly.

    Params:
    nums (Sequence[int] | None): The input sequence of integers. If it's None or empty,
    a ValueError exception is thrown.

    Returns:
    int: The maximum possible subsequence sum among all non-empty subsequences of the input sequence.

    Raises:
    ValueError: when nums is None or empty.

    Examples:

    >>> max_subsequence_sum([1,2,3,4,-2])
    10
    >>> max_subsequence_sum([-2, -3, -1, -4, -6])
    -1
    >>> max_subsequence_sum([])
    Traceback (most recent call last):
        . . .
    ValueError: Input sequence should not be empty
    >>> max_subsequence_sum()
    Traceback (most recent call last):
        . . .
    ValueError: Input sequence should not be empty

    """
    if not nums:
        raise ValueError("Input sequence should not be empty")

    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Try on a sample input from the user
    n = int(input("Enter number of elements : ").strip())
    array = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    print(max_subsequence_sum(array))
