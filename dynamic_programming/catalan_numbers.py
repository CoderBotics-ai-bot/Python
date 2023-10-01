"""
Print all the Catalan numbers from 0 to n, n being the user input.

 * The Catalan numbers are a sequence of positive integers that
 * appear in many counting problems in combinatorics [1]. Such
 * problems include counting [2]:
 * - The number of Dyck words of length 2n
 * - The number well-formed expressions with n pairs of parentheses
 *   (e.g., `()()` is valid but `())(` is not)
 * - The number of different ways n + 1 factors can be completely
 *   parenthesized (e.g., for n = 2, C(n) = 2 and (ab)c and a(bc)
 *   are the two valid ways to parenthesize.
 * - The number of full binary trees with n + 1 leaves

 * A Catalan number satisfies the following recurrence relation
 * which we will use in this algorithm [1].
 * C(0) = C(1) = 1
 * C(n) = sum(C(i).C(n-i-1)), from i = 0 to n-1

 * In addition, the n-th Catalan number can be calculated using
 * the closed form formula below [1]:
 * C(n) = (1 / (n + 1)) * (2n choose n)

 * Sources:
 *  [1] https://brilliant.org/wiki/catalan-numbers/
 *  [2] https://en.wikipedia.org/wiki/Catalan_number
"""


from typing import List

def catalan_numbers(upper_limit: int) -> list[int]:
    """Compute the Catalan numbers up to a given limit."""
    _check_upper_limit(upper_limit)
    catalan_list = _initialize_catalan_sequence(upper_limit)
    catalan_list = _compute_catalan_sequence(catalan_list, upper_limit)
    return catalan_list


if __name__ == "__main__":
    print("\n********* Catalan Numbers Using Dynamic Programming ************\n")
    print("\n*** Enter -1 at any time to quit ***")
    print("\nEnter the upper limit (≥ 0) for the Catalan number sequence: ", end="")
    try:
        while True:
            N = int(input().strip())
            if N < 0:
                print("\n********* Goodbye!! ************")
                break
            else:
                print(f"The Catalan numbers from 0 through {N} are:")
                print(catalan_numbers(N))
                print("Try another upper limit for the sequence: ", end="")
    except (NameError, ValueError):
        print("\n********* Invalid input, goodbye! ************\n")

    import doctest

    doctest.testmod()


def _check_upper_limit(upper_limit: int) -> None:
    """Throw an error if the upper limit is less than 0."""
    if upper_limit < 0:
        raise ValueError("Limit for the Catalan sequence must be ≥ 0")


def _initialize_catalan_sequence(upper_limit: int) -> list[int]:
    """Initialize the Catalan sequence with base values."""
    catalan_list = [0] * (upper_limit + 1)
    catalan_list[0] = 1
    if upper_limit > 0:
        catalan_list[1] = 1
    return catalan_list


def _compute_catalan_sequence(catalan_list: list[int], upper_limit: int) -> list[int]:
    """Compute the Catalan sequence using the given recurrence relation."""
    for i in range(2, upper_limit + 1):
        for j in range(i):
            catalan_list[i] += catalan_list[j] * catalan_list[i - j - 1]
    return catalan_list
