"""
Longest Common Substring Problem Statement: Given two sequences, find the
longest common substring present in both of them. A substring is
necessarily continuous.
Example: "abcdef" and "xabded" have two longest common substrings, "ab" or "de".
Therefore, algorithm should return any one of them.
"""


from typing import List, Tuple

def longest_common_substring(text1: str, text2: str) -> str:
    """
    This function is used to find the longest common substring between two strings.

    Args:
        text1: The first input string.
        text2: The second input string.

    Returns:
        The longest common substring if exists otherwise ''.

    Raises:
        ValueError: If the function does not receive two strings for inputs.

    """
    validate_strings(text1, text2)
    dp, text1_length, text2_length = initiate_dp_table(text1, text2)
    max_length, last_sub_end = find_max_length_substring(text1, text2, dp)
    return extract_substring(text1, max_length, last_sub_end)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def validate_strings(text1: str, text2: str) -> None:
    """
    Validate that the provided texts are strings.
    """
    if not (isinstance(text1, str) and isinstance(text2, str)):
        raise ValueError("longest_common_substring() takes two strings for inputs")


def initiate_dp_table(text1: str, text2: str) -> Tuple[List[List[int]], int, int]:
    """
    Initiate the dynamic programming table.
    """
    text1_length = len(text1)
    text2_length = len(text2)
    dp = [[0] * (text2_length + 1) for _ in range(text1_length + 1)]
    return dp, text1_length, text2_length


def find_max_length_substring(
    text1: str, text2: str, dp: List[List[int]]
) -> Tuple[int, int]:
    """
    Find the maximum length substring and its end index.
    """
    max_length = 0
    last_sub_end = 0
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] != text2[j - 1]:
                continue
            dp[i][j] = 1 + dp[i - 1][j - 1]
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                last_sub_end = i
    return max_length, last_sub_end


def extract_substring(text: str, length: int, end_index: int) -> str:
    """
    Extract the common substring from the text.
    """
    return text[end_index - length : end_index]
