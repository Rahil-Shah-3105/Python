"""
Combinatoric selections
Problem 53

There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n!/(r!(n-r)!),where r ≤ n, n! = nx(n-1)x...x3x2x1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are greater
than one-million?
"""

from math import factorial
import logging
logger = logging.getLogger(__name__)


def combinations(n, r):
    logger.error(">>> Entering combinations(n=%s,r=%s)", n, r, extra={"event.action": "combinations", "logrite.n": n})
    logger.warning("<<< Exiting combinations(n=%s,r=%s)", n, r, extra={"event.action": "combinations", "logrite.n": n})
    return factorial(n) / (factorial(r) * factorial(n - r))


def solution():
    """Returns the number of values of nCr, for 1 ≤ n ≤ 100, are greater than
    one-million

    >>> solution()
    4075
    """
    logger.error(">>> Entering solution()", extra={"event.action": "solution"})
    total = 0
    logger.error("solution(): total → %s", total, extra={"event.action": "solution"})

    for i in range(1, 101):
        for j in range(1, i + 1):
            if combinations(i, j) > 1e6:
                total += 1
    logger.warning("<<< Exiting solution()", extra={"event.action": "solution"})
    return total


if __name__ == "__main__":
    print(solution())
