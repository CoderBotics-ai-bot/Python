"""
Project Euler Problem 10: https://projecteuler.net/problem=10

Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

References:
    - https://en.wikipedia.org/wiki/Prime_number
    - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


def solution(n: int = 2000000) -> int:
    """
    Calculate the sum of all prime numbers below a given number `n`.

    This function uses the Sieve of Eratosthenes algorithm to find all prime numbers
    smaller than `n`. The function then calculates the sum of these prime numbers.

    The Sieve of Eratosthenes algorithm is most efficient when `n` is less than 10 million.
    Note: This function only handles positive integers

    Args:
        n: An integer, the upper limit to sum primes up to. Default is 2,000,000.

    Returns:
        The sum of all prime numbers below `n`.

    Raises:
        TypeError: If `n` is not an integer.
        IndexError: If `n` is a negative integer.
    """
    return sum_primes(n)


if __name__ == "__main__":
    print(f"{solution() = }")

def generate_primes(n: int) -> List[int]:
    """
    Generate a list of prime numbers up to n using the Sieve of Eratosthenes method.

    Args:
        n: The upper limit to generate primes up to.

    Returns:
        A list of primes numbers up to n.
    """
    primes = [i for i in range(2, n + 1)]
    for i in primes:
        if i is None:
            continue
        for j in range(i * 2, n + 1, i):
            primes[j - 2] = None
    return [prime for prime in primes if prime is not None]


def sum_primes(n: int) -> int:
    """
    Sums the prime numbers up to n.

    Args:
        n: The upper limit to sum primes up to.

    Returns:
        The sum of primes up to n.
    """
    primes = generate_primes(n)
    return sum(primes)
