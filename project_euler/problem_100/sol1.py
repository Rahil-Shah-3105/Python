import logging
logger = logging.getLogger(__name__)
"""
Project Euler Problem 100: https://projecteuler.net/problem=100

If a box contains twenty-one coloured discs, composed of fifteen blue discs and
six red discs, and two discs were taken at random, it can be seen that
the probability of taking two blue discs, P(BB) = (15/21) x (14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue
discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs
in total, determine the number of blue discs that the box would contain.
"""


def solution(min_total: int = 10**12) -> int:
    """
    Returns the number of blue discs for the first arrangement to contain
    over min_total discs in total

    >>> solution(2)
    3

    >>> solution(4)
    15

    >>> solution(21)
    85
    """
    logger.debug(">>> Entering solution(min_total=%s)", min_total)

    prev_numerator = 1
    logger.debug("solution(min_total=%s): prev_numerator → %s", min_total, prev_numerator)
    prev_denominator = 0
    logger.debug("solution(min_total=%s): prev_denominator → %s", min_total, prev_denominator)

    numerator = 1
    logger.debug("solution(min_total=%s): numerator → %s", min_total, numerator)
    denominator = 1
    logger.debug("solution(min_total=%s): denominator → %s", min_total, denominator)

    while numerator <= 2 * min_total - 1:
        prev_numerator += 2 * numerator
        numerator += 2 * prev_numerator

        prev_denominator += 2 * denominator
        denominator += 2 * prev_denominator

    logger.debug("<<< Exiting solution(min_total=%s)", min_total)
    return (denominator + 1) // 2


if __name__ == "__main__":
    print(f"{solution() = }")
