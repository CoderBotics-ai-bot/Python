"""
Longest Common Substring Problem Statement: Given two sequences, find the
longest common substring present in both of them. A substring is
necessarily continuous.
Example: "abcdef" and "xabded" have two longest common substrings, "ab" or "de".
Therefore, algorithm should return any one of them.
"""


from typing import List

def longest_common_substring(text1: str, text2: str) -> str:
    """
    Finds the longest common substring between two given strings.

    Args:
        text1 (str): The first string.
        text2 (str): The second string.

    Returns:
        str: The longest common substring. If there is none, returns an empty string.
    """
    _raise_for_incorrect_types(text1, text2)

    matrix = _init_matrix(len(text1), len(text2))
    longest_substring = _compute_longest_substring(text1, text2, matrix)

    return longest_substring


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def _raise_for_incorrect_types(text1: str, text2: str):
    if not (isinstance(text1, str) and isinstance(text2, str)):
        raise ValueError("longest_common_substring() takes two strings for inputs")


def _init_matrix(width: int, height: int) -> List[List[int]]:
    return [[0] * (height + 1) for _ in range(width + 1)]


def _compute_longest_substring(text1: str, text2: str, dp: List[List[int]]) -> str:
    ans_length = ans_index = 0

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

                if dp[i][j] > ans_length:
                    ans_length = dp[i][j]
                    ans_index = i

    return text1[ans_index - ans_length : ans_index]
