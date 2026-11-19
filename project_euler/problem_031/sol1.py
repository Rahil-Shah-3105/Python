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
import logging
logger = logging.getLogger(__name__)


def one_pence() -> int:
    logger.error(">>> Entering one_pence()", extra={"event.action": "one_pence"})
    logger.warning("<<< Exiting one_pence()", extra={"event.action": "one_pence"})
    return 1


def two_pence(x: int) -> int:
    logger.error(">>> Entering two_pence(x=%s)", x, extra={"event.action": "two_pence", "logrite.x": x})
    logger.warning("<<< Exiting two_pence(x=%s)", x, extra={"event.action": "two_pence", "logrite.x": x})
    return 0 if x < 0 else two_pence(x - 2) + one_pence()


def five_pence(x: int) -> int:
    logger.error(">>> Entering five_pence(x=%s)", x, extra={"event.action": "five_pence", "logrite.x": x})
    logger.warning("<<< Exiting five_pence(x=%s)", x, extra={"event.action": "five_pence", "logrite.x": x})
    return 0 if x < 0 else five_pence(x - 5) + two_pence(x)


def ten_pence(x: int) -> int:
    logger.error(">>> Entering ten_pence(x=%s)", x, extra={"event.action": "ten_pence", "logrite.x": x})
    logger.warning("<<< Exiting ten_pence(x=%s)", x, extra={"event.action": "ten_pence", "logrite.x": x})
    return 0 if x < 0 else ten_pence(x - 10) + five_pence(x)


def twenty_pence(x: int) -> int:
    logger.error(">>> Entering twenty_pence(x=%s)", x, extra={"event.action": "twenty_pence", "logrite.x": x})
    logger.warning("<<< Exiting twenty_pence(x=%s)", x, extra={"event.action": "twenty_pence", "logrite.x": x})
    return 0 if x < 0 else twenty_pence(x - 20) + ten_pence(x)


def fifty_pence(x: int) -> int:
    logger.error(">>> Entering fifty_pence(x=%s)", x, extra={"event.action": "fifty_pence", "logrite.x": x})
    logger.warning("<<< Exiting fifty_pence(x=%s)", x, extra={"event.action": "fifty_pence", "logrite.x": x})
    return 0 if x < 0 else fifty_pence(x - 50) + twenty_pence(x)


def one_pound(x: int) -> int:
    logger.error(">>> Entering one_pound(x=%s)", x, extra={"event.action": "one_pound", "logrite.x": x})
    logger.warning("<<< Exiting one_pound(x=%s)", x, extra={"event.action": "one_pound", "logrite.x": x})
    return 0 if x < 0 else one_pound(x - 100) + fifty_pence(x)


def two_pound(x: int) -> int:
    logger.error(">>> Entering two_pound(x=%s)", x, extra={"event.action": "two_pound", "logrite.x": x})
    logger.warning("<<< Exiting two_pound(x=%s)", x, extra={"event.action": "two_pound", "logrite.x": x})
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
    logger.error(">>> Entering solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    logger.warning("<<< Exiting solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    return two_pound(n)


if __name__ == "__main__":
    print(solution(int(input().strip())))
