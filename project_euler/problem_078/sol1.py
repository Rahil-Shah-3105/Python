"""
Problem 78
Url: https://projecteuler.net/problem=78
Statement:
Let p(n) represent the number of different ways in which n coins
can be separated into piles. For example, five coins can be separated
into piles in exactly seven different ways, so p(5)=7.

            OOOOO
            OOOO   O
            OOO   OO
            OOO   O   O
            OO   OO   O
            OO   O   O   O
            O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""

import itertools
import logging
logger = logging.getLogger(__name__)


def solution(number: int = 1000000) -> int:
    """
    >>> solution(1)
    1

    >>> solution(9)
    14

    >>> solution()
    55374
    """
    logger.debug(">>> Entering solution(number=%s)", number)
    partitions = [1]
    logger.debug("solution(number=%s): partitions → %s", number, partitions)

    for i in itertools.count(len(partitions)):
        item = 0
        for j in itertools.count(1):
            sign = -1 if j % 2 == 0 else +1
            index = (j * j * 3 - j) // 2
            logger.debug("solution(number=%s): index → %s", number, index)
            if index > i:
                break
            item += partitions[i - index] * sign
            item %= number
            index += j
            if index > i:
                break
            item += partitions[i - index] * sign
            item %= number

        if item == 0:
            return i
        partitions.append(item)

    logger.debug("<<< Exiting solution(number=%s)", number)
    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"{solution() = }")
