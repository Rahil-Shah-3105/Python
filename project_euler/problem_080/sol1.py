"""
Project Euler Problem 80: https://projecteuler.net/problem=80
Author: Sandeep Gupta
Problem statement: For the first one hundred natural numbers, find the total of
the digital sums of the first one hundred decimal digits for all the irrational
square roots.
Time: 5 October 2020, 18:30
"""

import decimal
import logging
logger = logging.getLogger(__name__)


def solution() -> int:
    """
    To evaluate the sum, Used decimal python module to calculate the decimal
    places up to 100, the most important thing would be take calculate
    a few extra places for decimal otherwise there will be rounding
    error.

    >>> solution()
    40886
    """
    logger.debug(">>> Entering solution()")
    answer = 0
    logger.debug("solution(): answer → %s", answer)
    decimal_context = decimal.Context(prec=105)
    logger.debug("solution(): decimal_context → %s", decimal_context)
    for i in range(2, 100):
        number = decimal.Decimal(i)
        logger.debug("solution(): number → %s", number)
        sqrt_number = number.sqrt(decimal_context)
        logger.debug("solution(): sqrt_number → %s", sqrt_number)
        if len(str(sqrt_number)) > 1:
            answer += int(str(sqrt_number)[0])
            sqrt_number_str = str(sqrt_number)[2:101]
            logger.debug("solution(): sqrt_number_str → %s", sqrt_number_str)
            answer += sum(int(x) for x in sqrt_number_str)
    logger.debug("<<< Exiting solution()")
    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{solution() = }")
