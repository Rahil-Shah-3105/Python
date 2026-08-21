"""Segmented Sieve."""

import math
import logging
logger = logging.getLogger(__name__)


def sieve(n: int) -> list[int]:
    """
    Segmented Sieve.

    Examples:
    >>> sieve(8)
    [2, 3, 5, 7]

    >>> sieve(27)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]

    >>> sieve(0)
    Traceback (most recent call last):
        ...
    ValueError: Number 0 must instead be a positive integer

    >>> sieve(-1)
    Traceback (most recent call last):
        ...
    ValueError: Number -1 must instead be a positive integer

    >>> sieve(22.2)
    Traceback (most recent call last):
        ...
    ValueError: Number 22.2 must instead be a positive integer
    """
    logger.debug(">>> Entering sieve(n=%s)", n)

    if n <= 0 or isinstance(n, float):
        msg = f"Number {n} must instead be a positive integer"
        logger.debug("sieve(n=%s): msg → %s", n, msg)
        raise ValueError(msg)

    in_prime = []
    logger.debug("sieve(n=%s): in_prime → %s", n, in_prime)
    start = 2
    logger.debug("sieve(n=%s): start → %s", n, start)
    end = int(math.sqrt(n))  # Size of every segment
    logger.debug("sieve(n=%s): end → %s", n, end)
    temp = [True] * (end + 1)
    prime = []
    logger.debug("sieve(n=%s): prime → %s", n, prime)

    while start <= end:
        if temp[start] is True:
            in_prime.append(start)
            for i in range(start * start, end + 1, start):
                temp[i] = False
        start += 1
    prime += in_prime

    low = end + 1
    logger.debug("sieve(n=%s): low → %s", n, low)
    high = min(2 * end, n)
    logger.debug("sieve(n=%s): high → %s", n, high)

    while low <= n:
        temp = [True] * (high - low + 1)
        for each in in_prime:
            t = math.floor(low / each) * each
            logger.debug("sieve(n=%s): t → %s", n, t)
            if t < low:
                t += each

            for j in range(t, high + 1, each):
                temp[j - low] = False

        for j in range(len(temp)):
            if temp[j] is True:
                prime.append(j + low)

        low = high + 1
        high = min(high + end, n)

    logger.debug("<<< Exiting sieve(n=%s)", n)
    return prime


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"{sieve(10**6) = }")
