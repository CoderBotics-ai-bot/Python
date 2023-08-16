"""
Author  : Turfa Auliarachman
Date    : October 12, 2016

This is a pure Python implementation of Dynamic Programming solution to the edit
distance problem.

The problem is :
Given two strings A and B. Find the minimum number of operations to string B such that
A = B. The permitted operations are removal,  insertion, and substitution.
"""








class EditDistance:

    def __init__(self):
        self.word1 = ""
        self.word2 = ""
        self.dp = []

    def __min_dist_top_down_dp(self, m: int, n: int) -> int:
        """
        A private method to calculate the minimum distance (edit distance) between two words using top-down dynamic programming.

        Args:
            m (int): The length of the first word.
            n (int): The length of the second word.

        Returns:
            int: The minimum distance between the two words.

        This method uses a top-down approach for dynamic programming. It begins at the top and breaks the problem
        down into subproblems. It uses a 2D tabulation table, where dp[i][j] indicates the edit distance
        between the substrings of the first word of length i and the second word of length j.

        When the characters at the given indices in both words are equal, the function moves diagonally left in
        the tabulation table; otherwise, it finds the minimum among the cells to the left, top, and diagonally left
        (corresponding to insertion, deletion, and replacement) and adds 1.

        The memoized values in the table avoid repeated computation of the same subproblems, hence improving the
        time efficiency of the solution.
        """
        if m == -1:
            return n + 1
        elif n == -1:
            return m + 1
        elif self.dp[m][n] > -1:
            return self.dp[m][n]
        else:
            if self.word1[m] == self.word2[n]:
                self.dp[m][n] = self.__min_dist_top_down_dp(m - 1, n - 1)
            else:
                insert = self.__min_dist_top_down_dp(m, n - 1)
                delete = self.__min_dist_top_down_dp(m - 1, n)
                replace = self.__min_dist_top_down_dp(m - 1, n - 1)
                self.dp[m][n] = 1 + min(insert, delete, replace)

            return self.dp[m][n]

    def min_dist_top_down(self, word1: str, word2: str) -> int:
        """
        >>> EditDistance().min_dist_top_down("intention", "execution")
        5
        >>> EditDistance().min_dist_top_down("intention", "")
        9
        >>> EditDistance().min_dist_top_down("", "")
        0
        """
        self.word1 = word1
        self.word2 = word2
        self.dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]

        return self.__min_dist_top_down_dp(len(word1) - 1, len(word2) - 1)

    def min_dist_bottom_up(self, word1: str, word2: str) -> int:
        """
        Calculate the minimum edit distance between two given words using dynamic programming.
        This method uses bottom-up approach which iteratively fills up a 2D DP table.

        Args:
            word1 (str): The first word as a string.
            word2 (str): The second word as a string.

        Returns:
            int: The minimum edit distance between word1 and word2.

        Examples:
            >>> EditDistance().min_dist_bottom_up("intention", "execution")
            5
            >>> EditDistance().min_dist_bottom_up("intention", "")
            9
            >>> EditDistance().min_dist_bottom_up("", "")
            0

        Note:
            Edit distance, also known as Levenshtein distance, is a measure of similarity between two strings.
            The distance is the minimum number of operations (insertions, deletions, and substitutions)
            required to transform one string into another.
            This implementation uses dynamic programming to reduce the time complexity.
        """
        self.word1 = word1
        self.word2 = word2
        m = len(word1)
        n = len(word2)
        self.dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:  # first string is empty
                    self.dp[i][j] = j
                elif j == 0:  # second string is empty
                    self.dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:  # last characters are equal
                    self.dp[i][j] = self.dp[i - 1][j - 1]
                else:
                    insert = self.dp[i][j - 1]
                    delete = self.dp[i - 1][j]
                    replace = self.dp[i - 1][j - 1]
                    self.dp[i][j] = 1 + min(insert, delete, replace)
        return self.dp[m][n]


if __name__ == "__main__":
    solver = EditDistance()

    print("****************** Testing Edit Distance DP Algorithm ******************")
    print()

    S1 = input("Enter the first string: ").strip()
    S2 = input("Enter the second string: ").strip()

    print()
    print(f"The minimum edit distance is: {solver.min_dist_top_down(S1, S2)}")
    print(f"The minimum edit distance is: {solver.min_dist_bottom_up(S1, S2)}")
    print()
    print("*************** End of Testing Edit Distance DP Algorithm ***************")
