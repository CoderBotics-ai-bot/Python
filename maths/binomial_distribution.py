"""For more information about the Binomial Distribution -
    https://en.wikipedia.org/wiki/Binomial_distribution"""
from math import factorial

def binomial_distribution(successes: int, trials: int, prob: float) -> float:
    """
    Calculate the probability of a specific binary outcome in a given number of trials.

    This function uses the binomial theorem to calculate the likelihood of a specified number
    of successes in a series of trials, where each trial has the same probability of success.

    Args:
        successes (int): The number of successful outcomes.
        trials (int): Total number of trials.
        prob (float): Probability of success in one trial.

    Returns:
        float: The calculated binomial probability.

    Raises:
        ValueError: If the number of successes is greater than the number of trials.
        ValueError: If the number of trials or the number of successes is negative.
        ValueError: If the number of successes or trials is not integer.
        ValueError: If the probability of success is not within the range [0, 1].

    Example:
        >>> binomial_distribution(3, 5, 0.7)
        0.30870000000000003
        >>> binomial_distribution (2, 4, 0.5)
        0.375

    Note:
        The returned probability corresponds to the specific outcome, not the cumulative
        probability up to the specified number of successes. To calculate the latter, sum
        the binomial probabilities for all possible outcomes up to and including the
        specified number of successes.
    """
    if successes > trials:
        raise ValueError("Successes must be lower or equal to trials")
    if trials < 0 or successes < 0:
        raise ValueError("The function is defined for non-negative integers")
    if not isinstance(successes, int) or not isinstance(trials, int):
        raise ValueError("The function is defined for non-negative integers")
    if not 0 <= prob <= 1:
        raise ValueError("Probability has to be within the range [0, 1]")
    probability = (prob**successes) * ((1 - prob) ** (trials - successes))
    # Calculate the binomial coefficient: n! / k!(n-k)!
    coefficient = float(factorial(trials))
    coefficient /= factorial(successes) * factorial(trials - successes)
    return probability * coefficient


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Probability of 2 successes out of 4 trails")
    print("with probability of 0.75 is:", end=" ")
    print(binomial_distribution(2, 4, 0.75))
