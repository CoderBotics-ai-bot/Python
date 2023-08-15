"""
Totient maximum
Problem 69: https://projecteuler.net/problem=69

Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8,
are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	                1	    2
3	1,2	                2	    1.5
4	1,3	                2	    2
5	1,2,3,4	            4	    1.25
6	1,5		            2	    3
7	1,2,3,4,5,6	        6	    1.1666...
8	1,3,5,7		        4	    2
9	1,2,4,5,7,8	        6	    1.5
10	1,3,7,9	            4	    2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""


from typing import List


def solution(n: int = 10**6) -> int:
    """
    Given an integer n, this function precomputes φ(k) for all natural k, k <= n using Euler's product formula
    and returns the value of k that attains the maximum value of k/φ(k).

    Args:
        n (int, optional): The upper limit to which the computation is performed.
        Default is 10**6.

    Returns:
        int: The value of k that maximises the value of k / φ(k).

    Raises:
        ValueError: Error raised if the input n is less than or equal to 0.
    """
    if n <= 0:
        raise ValueError("Please enter an integer greater than 0")

    phi = phi_values(n)
    return max_k_value(n, phi)


if __name__ == "__main__":
    print(solution())

def phi_values(n: int) -> List[int]:
    """
    The function precomputes φ(k) for all natural k, k <= n using Euler's product formula.

    Args:
        n (int): The upper limit to which the computation is performed.

    Returns:
        List[int]: The list of precomputed φ(k) values.
    """
    phi = list(range(n + 1))
    for number in range(2, n + 1):
        if phi[number] == number:
            phi[number] -= 1
            for multiple in range(number * 2, n + 1, number):
                phi[multiple] = (phi[multiple] // number) * (number - 1)
    return phi


def max_k_value(n: int, phi: List[int]) -> int:
    """
    The function calculates the value of k that attains the maximum value of k / φ(k).

    Args:
        n (int): The upper limit to which the computation is performed.
        phi (List[int]): The list of precomputed φ(k) values.

    Returns:
        int: The value of k that maximises the value of k / φ(k).
    """
    answer = 1
    for number in range(1, n + 1):
        if (answer / phi[answer]) < (number / phi[number]):
            answer = number
    return answer
