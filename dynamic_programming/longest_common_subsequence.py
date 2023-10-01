"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence
present in both of them.  A subsequence is a sequence that appears in the same relative
order, but not necessarily continuous.
Example:"abc", "abg" are subsequences of "abcdefgh".
"""


from typing import Tuple


from typing import List, Tuple

def longest_common_subsequence(x: str, y: str) -> Tuple[int, str]:
    """
    Calculates the length of the longest common subsequence between two given strings and
    returns the longest common subsequence.

    This function uses a dynamic programming approach. It creates a
    matrix to store the lengths of common subsequences for each pair
    of indices of the given strings. The function iterates over the strings,
    updating the matrix, and finally derives the longest common subsequence
    from the matrix.

    Parameters
    ----------
    x: str
        The first string to compare.
    y: str
        The second string to compare.

    Returns
    -------
    Tuple[int, str]
        A tuple containing two elements, the length of the longest
        common subsequence and the longest common subsequence itself.
    """
    assert x is not None and y is not None

    memo = __initialize_memo(x, y)
    memo = __calculate_subsequence_lengths(x, y, memo)
    length, sequence = __extract_subsequence(x, y, memo)

    return length, sequence


if __name__ == "__main__":
    a = "AGGTAB"
    b = "GXTXAYB"
    expected_ln = 4
    expected_subseq = "GTAB"

    ln, subseq = longest_common_subsequence(a, b)
    print("len =", ln, ", sub-sequence =", subseq)
    import doctest

    doctest.testmod()


def __initialize_memo(x: str, y: str) -> List[List[int]]:
    return [[0] * (len(y) + 1) for _ in range(len(x) + 1)]


def __calculate_subsequence_lengths(
    x: str, y: str, memo: List[List[int]]
) -> List[List[int]]:
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            match = int(x[i - 1] == y[j - 1])
            memo[i][j] = max(memo[i - 1][j], memo[i][j - 1], memo[i - 1][j - 1] + match)

    return memo


def __extract_subsequence(x: str, y: str, memo: List[List[int]]) -> Tuple[int, str]:
    sequence = ""
    i, j = len(x), len(y)

    while i > 0 and j > 0:
        match = int(x[i - 1] == y[j - 1])
        if memo[i][j] == memo[i - 1][j - 1] + match:
            if match:
                sequence = x[i - 1] + sequence

            i -= 1
            j -= 1
        elif memo[i][j] == memo[i - 1][j]:
            i -= 1
        else:
            j -= 1

    return memo[len(x)][len(y)], sequence
