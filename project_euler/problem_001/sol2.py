"""
Project Euler Problem 1: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import logging
logger = logging.getLogger(__name__)


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
    logger.error(">>> Entering solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})

    total = 0
    logger.error("solution(n=%s): total → %s", n, total, extra={"event.action": "solution", "logrite.n": n})
    terms = (n - 1) // 3
    logger.error("solution(n=%s): terms → %s", n, terms, extra={"event.action": "solution", "logrite.n": n})
    total += ((terms) * (6 + (terms - 1) * 3)) // 2  # total of an A.P.
    terms = (n - 1) // 5
    total += ((terms) * (10 + (terms - 1) * 5)) // 2
    terms = (n - 1) // 15
    total -= ((terms) * (30 + (terms - 1) * 15)) // 2
    logger.warning("<<< Exiting solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    return total


if __name__ == "__main__":
    print(f"{solution() = }")
