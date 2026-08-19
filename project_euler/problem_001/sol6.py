import logging
logger = logging.getLogger(__name__)
"""
Project Euler Problem 1: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solution(n: int = 1000) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """
    logger.debug(">>> Entering solution(n=%s)", n)

    a = 3
    result = 0
    logger.debug("solution(n=%s): result → %s", n, result)
    while a < n:
        if a % 3 == 0 or a % 5 == 0:
            result += a
        elif a % 15 == 0:
            result -= a
        a += 1
    logger.debug("<<< Exiting solution(n=%s)", n)
    return result


if __name__ == "__main__":
    print(f"{solution() = }")
