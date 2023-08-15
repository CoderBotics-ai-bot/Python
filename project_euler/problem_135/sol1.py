"""
Project Euler Problem 135: https://projecteuler.net/problem=135

Given the positive integers, x, y, and z,
are consecutive terms of an arithmetic progression,
the least value of the positive integer, n,
for which the equation,
x2 − y2 − z2 = n, has exactly two solutions is n = 27:

342 − 272 − 202 = 122 − 92 − 62 = 27

It turns out that n = 1155 is the least value
which has exactly ten solutions.

How many values of n less than one million
have exactly ten distinct solutions?


Taking x,y,z of the form a+d,a,a-d respectively,
the given equation reduces to a*(4d-a)=n.
Calculating no of solutions for every n till 1 million by fixing a
,and n must be multiple of a.
Total no of steps=n*(1/1+1/2+1/3+1/4..+1/n)
,so roughly O(nlogn) time complexity.

"""


from typing import List


def solution(limit: int = 1000000) -> int:
    """
    The function finds the number of 'n' values less than the specified 'limit' which have exactly ten distinct solutions.

    Args:
    limit: A number that defines the upper boundary for 'n'. By default it is 1000000.

    Returns:
    The number of 'n' values less than or equal to 'limit' which have exactly ten distinct solutions.

    """
    # Increase the limit by one for accurate counting
    limit = limit + 1

    # Generate frequency of 'n' values
    frequency = generate_frequency(limit)

    # Count how many 'n' values have exactly 10 distinct solutions
    count = sum(1 for x in frequency[1:limit] if x == 10)

    return count


if __name__ == "__main__":
    print(f"{solution() = }")

def validate_common_difference(first_term: int, common_difference: float) -> int:
    """
    Function to validate common difference and return its status.

    Args:
    first_term: First term of the progressions.
    common_difference: The common difference used to control the arithmetic progression.

    Returns:
    Frequency count increase based on the condition of the common difference.

    """

    if common_difference % 4:
        # Skip this iteration
        return 0
    else:
        common_difference /= 4

        if first_term > common_difference and first_term < 4 * common_difference:
            # Increment value of n in frequency
            return 1
    return 0


def generate_frequency(limit: int) -> List[int]:
    """
    Function to generate the frequency of 'n' values for the arithmetic progression.

    Args:
    limit: The upper boundary for 'n'.

    Returns:
    A list of the frequency of 'n' values.

    """
    # Create a list of zeros with length of limit
    frequency = [0] * limit

    for first_term in range(1, limit):
        for n in range(first_term, limit, first_term):
            # Calculate common difference
            common_difference = first_term + n / first_term

            # Update frequency of 'n' values
            frequency[n] += validate_common_difference(first_term, common_difference)

    return frequency
