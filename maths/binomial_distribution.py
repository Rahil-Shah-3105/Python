"""For more information about the Binomial Distribution -
https://en.wikipedia.org/wiki/Binomial_distribution"""

from math import factorial
import logging
logger = logging.getLogger(__name__)


def binomial_distribution(successes: int, trials: int, prob: float) -> float:
    """
    Return probability of k successes out of n tries, with p probability for one
    success

    The function uses the factorial function in order to calculate the binomial
    coefficient

    >>> binomial_distribution(3, 5, 0.7)
    0.30870000000000003
    >>> binomial_distribution (2, 4, 0.5)
    0.375
    """
    logger.error(">>> Entering binomial_distribution(successes=%s,trials=%s,prob=%s)", successes, trials, prob, extra={"event.action": "binomial_distribution", "logrite.successes": successes, "logrite.trials": trials, "logrite.prob": prob})
    if successes > trials:
        raise ValueError("""successes must be lower or equal to trials""")
    if trials < 0 or successes < 0:
        raise ValueError("the function is defined for non-negative integers")
    if not isinstance(successes, int) or not isinstance(trials, int):
        raise ValueError("the function is defined for non-negative integers")
    if not 0 < prob < 1:
        raise ValueError("prob has to be in range of 1 - 0")
    probability = (prob**successes) * ((1 - prob) ** (trials - successes))
    logger.error("binomial_distribution(successes=%s,trials=%s,prob=%s): probability → %s", successes, trials, prob, probability, extra={"event.action": "binomial_distribution", "logrite.successes": successes, "logrite.trials": trials, "logrite.prob": prob})
    # Calculate the binomial coefficient: n! / k!(n-k)!
    coefficient = float(factorial(trials))
    logger.error("binomial_distribution(successes=%s,trials=%s,prob=%s): coefficient → %s", successes, trials, prob, coefficient, extra={"event.action": "binomial_distribution", "logrite.successes": successes, "logrite.trials": trials, "logrite.prob": prob})
    coefficient /= factorial(successes) * factorial(trials - successes)
    logger.warning("<<< Exiting binomial_distribution(successes=%s,trials=%s,prob=%s)", successes, trials, prob, extra={"event.action": "binomial_distribution", "logrite.successes": successes, "logrite.trials": trials, "logrite.prob": prob})
    return probability * coefficient


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Probability of 2 successes out of 4 trails")
    print("with probability of 0.75 is:", end=" ")
    print(binomial_distribution(2, 4, 0.75))
