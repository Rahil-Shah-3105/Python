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
    logger.error(">>> Entering solution()", extra={"event.action": "solution"})
    answer = 0
    decimal_context = decimal.Context(prec=105)
    logger.error("solution(): decimal_context → %s", decimal_context, extra={"event.action": "solution"})
    for i in range(2, 100):
        number = decimal.Decimal(i)
        logger.error("solution(): number → %s", number, extra={"event.action": "solution"})
        sqrt_number = number.sqrt(decimal_context)
        logger.error("solution(): sqrt_number → %s", sqrt_number, extra={"event.action": "solution"})
        if len(str(sqrt_number)) > 1:
            answer += int(str(sqrt_number)[0])
            sqrt_number_str = str(sqrt_number)[2:101]
            logger.error("solution(): sqrt_number_str → %s", sqrt_number_str, extra={"event.action": "solution"})
            answer += sum(int(x) for x in sqrt_number_str)
    logger.warning("<<< Exiting solution()", extra={"event.action": "solution"})
    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{solution() = }")
