"""
Amicable Numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt
import logging
logger = logging.getLogger(__name__)


def sum_of_divisors(n: int) -> int:
    logger.debug(">>> Entering sum_of_divisors(n=%s)", n)
    total = 0
    logger.debug("sum_of_divisors(n=%s): total → %s", n, total)
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0 and i != sqrt(n):
            total += i + n // i
        elif i == sqrt(n):
            total += i
    logger.debug("<<< Exiting sum_of_divisors(n=%s)", n)
    return total - n


def solution(n: int = 10000) -> int:
    """Returns the sum of all the amicable numbers under n.

    >>> solution(10000)
    31626
    >>> solution(5000)
    8442
    >>> solution(1000)
    504
    >>> solution(100)
    0
    >>> solution(50)
    0
    """
    logger.debug(">>> Entering solution(n=%s)", n)
    total = sum(
        i
        for i in range(1, n)
        if sum_of_divisors(sum_of_divisors(i)) == i and sum_of_divisors(i) != i
    )
    logger.debug("<<< Exiting solution(n=%s)", n)
    return total


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
