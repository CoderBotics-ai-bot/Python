"""
Given a string s, partition s such that every substring of the
partition is a palindrome.
Find the minimum cuts needed for a palindrome partitioning of s.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
For other explanations refer to: https://www.youtube.com/watch?v=_H8V5hJUGd0
"""


def find_minimum_partitions(string: str) -> int:
    length = len(string)
    cut, is_palindromic = initialize_arrays(length)
    return calculate_partitions(string, length, cut, is_palindromic)


if __name__ == "__main__":
    s = input("Enter the string: ").strip()
    ans = find_minimum_partitions(s)
    print(f"Minimum number of partitions required for the '{s}' is {ans}")

def initialize_arrays(length: int):
    """
    This function initializes the necessary arrays for the dynamic programming algorithm.
    """
    cut = [0] * length
    is_palindromic = [[False for _ in range(length)] for _ in range(length)]
    return cut, is_palindromic


def calculate_partitions(string: str, length: int, cut, is_palindromic):
    """
    This function populates the necessary arrays and calculates the minimum partitions for the given string.
    """
    for i, c in enumerate(string):
        mincut = i
        for j in range(i + 1):
            if c == string[j] and (i - j < 2 or is_palindromic[j + 1][i - 1]):
                is_palindromic[j][i] = True
                mincut = min(mincut, 0 if j == 0 else (cut[j - 1] + 1))
        cut[i] = mincut
    return cut[length - 1]
