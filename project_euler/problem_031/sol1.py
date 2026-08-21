import logging
logger = logging.getLogger(__name__)
"""
Coin sums
Problem 31: https://projecteuler.net/problem=31

In England the currency is made up of pound, f, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, f1 (100p) and f2 (200p).
It is possible to make f2 in the following way:

1xf1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can f2 be made using any number of coins?
"""


def one_pence() -> int:
    logger.debug(">>> Entering one_pence()")
    logger.debug("<<< Exiting one_pence()")
    return 1


def two_pence(x: int) -> int:
    logger.debug(">>> Entering two_pence(x=%s)", x)
    logger.debug("<<< Exiting two_pence(x=%s)", x)
    return 0 if x < 0 else two_pence(x - 2) + one_pence()


def five_pence(x: int) -> int:
    logger.debug(">>> Entering five_pence(x=%s)", x)
    logger.debug("<<< Exiting five_pence(x=%s)", x)
    return 0 if x < 0 else five_pence(x - 5) + two_pence(x)


def ten_pence(x: int) -> int:
    logger.debug(">>> Entering ten_pence(x=%s)", x)
    logger.debug("<<< Exiting ten_pence(x=%s)", x)
    return 0 if x < 0 else ten_pence(x - 10) + five_pence(x)


def twenty_pence(x: int) -> int:
    logger.debug(">>> Entering twenty_pence(x=%s)", x)
    logger.debug("<<< Exiting twenty_pence(x=%s)", x)
    return 0 if x < 0 else twenty_pence(x - 20) + ten_pence(x)


def fifty_pence(x: int) -> int:
    logger.debug(">>> Entering fifty_pence(x=%s)", x)
    logger.debug("<<< Exiting fifty_pence(x=%s)", x)
    return 0 if x < 0 else fifty_pence(x - 50) + twenty_pence(x)


def one_pound(x: int) -> int:
    logger.debug(">>> Entering one_pound(x=%s)", x)
    logger.debug("<<< Exiting one_pound(x=%s)", x)
    return 0 if x < 0 else one_pound(x - 100) + fifty_pence(x)


def two_pound(x: int) -> int:
    logger.debug(">>> Entering two_pound(x=%s)", x)
    logger.debug("<<< Exiting two_pound(x=%s)", x)
    return 0 if x < 0 else two_pound(x - 200) + one_pound(x)


def solution(n: int = 200) -> int:
    """Returns the number of different ways can n pence be made using any number of
    coins?

    >>> solution(500)
    6295434
    >>> solution(200)
    73682
    >>> solution(50)
    451
    >>> solution(10)
    11
    """
    logger.debug(">>> Entering solution(n=%s)", n)
    logger.debug("<<< Exiting solution(n=%s)", n)
    return two_pound(n)


if __name__ == "__main__":
    print(solution(int(input().strip())))
