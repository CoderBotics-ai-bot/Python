"""
https://en.wikipedia.org/wiki/Weird_number

Fun fact: The set of weird numbers has positive asymptotic density.
"""
from math import sqrt


def factors(number: int) -> list[int]:
    """
    >>> factors(12)
    [1, 2, 3, 4, 6]
    >>> factors(1)
    [1]
    >>> factors(100)
    [1, 2, 4, 5, 10, 20, 25, 50]

    # >>> factors(-12)
    # [1, 2, 3, 4, 6]
    """

    values = [1]
    for i in range(2, int(sqrt(number)) + 1, 1):
        if number % i == 0:
            values.append(i)
            if int(number // i) != i:
                values.append(int(number // i))
    return sorted(values)


def abundant(n: int) -> bool:
    """
    >>> abundant(0)
    True
    >>> abundant(1)
    False
    >>> abundant(12)
    True
    >>> abundant(13)
    False
    >>> abundant(20)
    True

    # >>> abundant(-12)
    # True
    """
    return sum(factors(n)) > n

def semi_perfect(number: int) -> bool:
    """
    This function checks whether a number is semi-perfect.
    A number is semi-perfect if it can be written as a sum of some
    (not necessarily distinct) factors of it
    (not including the number itself).

    Args:
        number (int): The number to check for semi-perfectness.

    Returns:
        bool: True if the number is semi-perfect, False otherwise.

    Note:
        This function uses a dynamic programming approach,
        where the state is defined as
        ('how many factors considered up to now', 'target sum remaining').
        The task is then to fill up the dp table with boolean values
        denoting whether the current state is achievable or not.
    """
    factors_of_number = factors(number)
    dp = _initalize_dp_table(len(factors_of_number), number)
    _fill_dp_table(dp, factors_of_number, number)

    return dp[len(factors_of_number)][number] != 0


def weird(number: int) -> bool:
    """
    >>> weird(0)
    False
    >>> weird(70)
    True
    >>> weird(77)
    False
    """
    return abundant(number) and not semi_perfect(number)


def _initalize_dp_table(n_rows: int, n_cols: int) -> list:
    """
    Initialize the DP table with basic conditions.
    """
    dp = [[0 for _ in range(n_cols + 1)] for _ in range(n_rows + 1)]
    for i in range(n_rows + 1):
        dp[i][0] = True
    for i in range(1, n_cols + 1):
        dp[0][i] = False

    return dp


def _fill_dp_table(dp: list, factors_of_number: list, number: int) -> None:
    """
    Fill up the DP table with values.
    """
    for i in range(1, len(factors_of_number) + 1):
        for j in range(1, number + 1):
            if j < factors_of_number[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - factors_of_number[i - 1]]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    for number in (69, 70, 71):
        print(f"{number} is {'' if weird(number) else 'not '}weird.")
