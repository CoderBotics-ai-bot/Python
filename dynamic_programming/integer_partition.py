"""
The number of partitions of a number n into at least k parts equals the number of
partitions into exactly k parts plus the number of partitions into at least k-1 parts.
Subtracting 1 from each part of a partition of n into k parts gives a partition of n-k
into k parts. These two facts together are used for this algorithm.
"""


from typing import List

def partition(m: int) -> int:
    """
    Calculates the number of ways a number can be partitioned.

    The main goal of this function is to determine the number of ways an integer 'm'
    can be expressed as the sum of positive integers.
    This function uses dynamic programming approach filling up an 'm x m' 2D list,
    called memo.

    Args:
        m: The integer to be partitioned.

    Returns:
        The number of ways 'm' can be partitioned.

    Examples:
        >>> partition(3)
        3
        >>> partition(4)
        5
    """

    def initialize_memo() -> List[List[int]]:
        """
        Initializes memoization list.

        Returns:
            memo: The initialized memoization list.
        """
        memo: List[List[int]] = [[0 for _ in range(m)] for _ in range(m + 1)]
        for i in range(m + 1):
            memo[i][0] = 1
        return memo

    def fill_memo(memo: List[List[int]]):
        """
        Fills the memoization list.

        Args:
            memo: The memoization list.

        Returns:
            None
        """
        for n in range(m + 1):
            for k in range(1, m):
                memo[n][k] += memo[n][k - 1]
                if n - k > 0:
                    memo[n][k] += memo[n - k - 1][k]

    memo = initialize_memo()
    fill_memo(memo)

    return memo[m][m - 1]


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        try:
            n = int(input("Enter a number: ").strip())
            print(partition(n))
        except ValueError:
            print("Please enter a number.")
    else:
        try:
            n = int(sys.argv[1])
            print(partition(n))
        except ValueError:
            print("Please pass a number.")
