from maths.greatest_common_divisor import greatest_common_divisor
import logging
logger = logging.getLogger(__name__)

"""
Project Euler Problem 5: https://projecteuler.net/problem=5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is _evenly divisible_ by all
of the numbers from 1 to 20?

References:
    - https://en.wiktionary.org/wiki/evenly_divisible
    - https://en.wikipedia.org/wiki/Euclidean_algorithm
    - https://en.wikipedia.org/wiki/Least_common_multiple
"""


def lcm(x: int, y: int) -> int:
    """
    Least Common Multiple.

    Using the property that lcm(a, b) * greatest_common_divisor(a, b) = a*b

    >>> lcm(3, 15)
    15
    >>> lcm(1, 27)
    27
    >>> lcm(13, 27)
    351
    >>> lcm(64, 48)
    192
    """
    logger.debug(">>> Entering lcm(x=%s,y=%s)", x, y)

    logger.debug("<<< Exiting lcm(x=%s,y=%s)", x, y)
    return (x * y) // greatest_common_divisor(x, y)


def solution(n: int = 20) -> int:
    """
    Returns the smallest positive number that is evenly divisible (divisible
    with no remainder) by all of the numbers from 1 to n.

    >>> solution(10)
    2520
    >>> solution(15)
    360360
    >>> solution(22)
    232792560
    """
    logger.debug(">>> Entering solution(n=%s)", n)

    logger.error("Exception in solution(n=%s)", n, exc_info=True)
    g = 1
    logger.debug("solution(n=%s): g → %s", n, g)
    for i in range(1, n + 1):
        g = lcm(g, i)
    logger.debug("<<< Exiting solution(n=%s)", n)
    return g


if __name__ == "__main__":
    print(f"{solution() = }")
