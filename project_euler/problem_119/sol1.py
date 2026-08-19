"""
Problem 119: https://projecteuler.net/problem=119

Name: Digit power sum

The number 512 is interesting because it is equal to the sum of its digits
raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number
with this property is 614656 = 28^4. We shall define an to be the nth term of
this sequence and insist that a number must contain at least two digits to have a sum.
You are given that a2 = 512 and a10 = 614656. Find a30
"""

import math
import logging
logger = logging.getLogger(__name__)


def digit_sum(n: int) -> int:
    """
    Returns the sum of the digits of the number.
    >>> digit_sum(123)
    6
    >>> digit_sum(456)
    15
    >>> digit_sum(78910)
    25
    """
    logger.debug(">>> Entering digit_sum(n=%s)", n)
    logger.debug("<<< Exiting digit_sum(n=%s)", n)
    return sum(int(digit) for digit in str(n))


def solution(n: int = 30) -> int:
    """
    Returns the value of 30th digit power sum.
    >>> solution(2)
    512
    >>> solution(5)
    5832
    >>> solution(10)
    614656
    """
    logger.debug(">>> Entering solution(n=%s)", n)
    digit_to_powers = []
    logger.debug("solution(n=%s): digit_to_powers → %s", n, digit_to_powers)
    for digit in range(2, 100):
        for power in range(2, 100):
            number = int(math.pow(digit, power))
            logger.debug("solution(n=%s): number → %s", n, number)
            if digit == digit_sum(number):
                digit_to_powers.append(number)

    digit_to_powers.sort()
    logger.debug("<<< Exiting solution(n=%s)", n)
    return digit_to_powers[n - 1]


if __name__ == "__main__":
    print(solution())
