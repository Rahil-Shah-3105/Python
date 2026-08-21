import logging
logger = logging.getLogger(__name__)
"""
Project Euler Problem 129: https://projecteuler.net/problem=129

A number consisting entirely of ones is called a repunit. We shall define R(k) to be
a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there
always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least
such value of k; for example, A(7) = 6 and A(41) = 5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.
"""


def least_divisible_repunit(divisor: int) -> int:
    """
    Return the least value k such that the Repunit of length k is divisible by divisor.
    >>> least_divisible_repunit(7)
    6
    >>> least_divisible_repunit(41)
    5
    >>> least_divisible_repunit(1234567)
    34020
    """
    logger.debug(">>> Entering least_divisible_repunit(divisor=%s)", divisor)
    if divisor % 5 == 0 or divisor % 2 == 0:
        return 0
    repunit = 1
    logger.debug("least_divisible_repunit(divisor=%s): repunit → %s", divisor, repunit)
    repunit_index = 1
    logger.debug("least_divisible_repunit(divisor=%s): repunit_index → %s", divisor, repunit_index)
    while repunit:
        repunit = (10 * repunit + 1) % divisor
        repunit_index += 1
    logger.debug("<<< Exiting least_divisible_repunit(divisor=%s)", divisor)
    return repunit_index


def solution(limit: int = 1000000) -> int:
    """
    Return the least value of n for which least_divisible_repunit(n)
    first exceeds limit.
    >>> solution(10)
    17
    >>> solution(100)
    109
    >>> solution(1000)
    1017
    """
    logger.debug(">>> Entering solution(limit=%s)", limit)
    divisor = limit - 1
    logger.debug("solution(limit=%s): divisor → %s", limit, divisor)
    if divisor % 2 == 0:
        divisor += 1
    while least_divisible_repunit(divisor) <= limit:
        divisor += 2
    logger.debug("<<< Exiting solution(limit=%s)", limit)
    return divisor


if __name__ == "__main__":
    print(f"{solution() = }")
