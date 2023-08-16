from __future__ import annotations

from math import gcd

def pollard_rho(
    num: int,
    seed: int = 2,
    step: int = 1,
    attempts: int = 3,
) -> int | None:
    """
    Use Pollard's Rho algorithm to return a nontrivial factor of `num`.
    The returned factor may be composite and require further factorization.
    If the algorithm will return None if it fails to find a factor within
    the specified number of attempts or within the specified number of steps.
    If `num` is prime, this algorithm is guaranteed to return None.
    https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm

    Args:
        num (int): The number to be factorized.
        seed (int, optional): The initial value of x, defaults to 2.
        step (int, optional): The increment used in the function f(x) for generating pseudorandom values, defaults to 1.
        attempts (int, optional): The number of attempts before giving up, defaults to 3.

    Returns:
        int | None: Returns a factor of `num` if found, else None.

    Raises:
        ValueError: When `num` is less than 2.

    Examples:
        >>> pollard_rho(18446744073709551617)
        274177
        >>> pollard_rho(97546105601219326301)
        9876543191
        >>> pollard_rho(100)
        2
        >>> pollard_rho(17)
        >>> pollard_rho(17**3)
        17
        >>> pollard_rho(17**3, attempts=1)
        >>> pollard_rho(3*5*7)
        21
        >>> pollard_rho(1)
        Traceback (most recent call last):
            ...
        ValueError: The input value cannot be less than 2
    """
    ...


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "num",
        type=int,
        help="The value to find a divisor of",
    )
    parser.add_argument(
        "--attempts",
        type=int,
        default=3,
        help="The number of attempts before giving up",
    )
    args = parser.parse_args()

    divisor = pollard_rho(args.num, attempts=args.attempts)
    if divisor is None:
        print(f"{args.num} is probably prime")
    else:
        quotient = args.num // divisor
        print(f"{args.num} = {divisor} * {quotient}")
