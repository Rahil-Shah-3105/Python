"""
Project Euler Problem 64: https://projecteuler.net/problem=64

All square roots are periodic when written as continued fractions.
For example, let us consider sqrt(23).
It can be seen that the sequence is repeating.
For conciseness, we use the notation sqrt(23)=[4;(1,3,1,8)],
to indicate that the block (1,3,1,8) repeats indefinitely.
Exactly four continued fractions, for N<=13, have an odd period.
How many continued fractions for N<=10000 have an odd period?

References:
- https://en.wikipedia.org/wiki/Continued_fraction
"""

from math import floor, sqrt
import logging
logger = logging.getLogger(__name__)


def continuous_fraction_period(n: int) -> int:
    """
    Returns the continued fraction period of a number n.

    >>> continuous_fraction_period(2)
    1
    >>> continuous_fraction_period(5)
    1
    >>> continuous_fraction_period(7)
    4
    >>> continuous_fraction_period(11)
    2
    >>> continuous_fraction_period(13)
    5
    """
    logger.error(">>> Entering continuous_fraction_period(n=%s)", n, extra={"event.action": "continuous_fraction_period", "logrite.n": n})
    numerator = 0.0
    denominator = 1.0
    logger.error("continuous_fraction_period(n=%s): denominator → %s", n, denominator, extra={"event.action": "continuous_fraction_period", "logrite.n": n})
    root = int(sqrt(n))
    logger.error("continuous_fraction_period(n=%s): root → %s", n, root, extra={"event.action": "continuous_fraction_period", "logrite.n": n})
    integer_part = root
    logger.error("continuous_fraction_period(n=%s): integer_part → %s", n, integer_part, extra={"event.action": "continuous_fraction_period", "logrite.n": n})
    period = 0
    while integer_part != 2 * root:
        numerator = denominator * integer_part - numerator
        denominator = (n - numerator**2) / denominator
        integer_part = int((root + numerator) / denominator)
        period += 1
    logger.warning("<<< Exiting continuous_fraction_period(n=%s)", n, extra={"event.action": "continuous_fraction_period", "logrite.n": n})
    return period


def solution(n: int = 10000) -> int:
    """
    Returns the count of numbers <= 10000 with odd periods.
    This function calls continuous_fraction_period for numbers which are
    not perfect squares.
    This is checked in if sr - floor(sr) != 0 statement.
    If an odd period is returned by continuous_fraction_period,
    count_odd_periods is increased by 1.

    >>> solution(2)
    1
    >>> solution(5)
    2
    >>> solution(7)
    2
    >>> solution(11)
    3
    >>> solution(13)
    4
    """
    logger.error(">>> Entering solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    count_odd_periods = 0
    for i in range(2, n + 1):
        sr = sqrt(i)
        logger.error("solution(n=%s): sr → %s", n, sr, extra={"event.action": "solution", "logrite.n": n})
        if sr - floor(sr) != 0 and continuous_fraction_period(i) % 2 == 1:
            count_odd_periods += 1
    logger.warning("<<< Exiting solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    return count_odd_periods


if __name__ == "__main__":
    print(f"{solution(int(input().strip()))}")
