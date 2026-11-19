"""Implementation of Basic Math in Python."""

import math
import logging
logger = logging.getLogger(__name__)


def prime_factors(n: int) -> list:
    """Find Prime Factors.
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(0)
    Traceback (most recent call last):
        ...
    ValueError: Only positive integers have prime factors
    >>> prime_factors(-10)
    Traceback (most recent call last):
        ...
    ValueError: Only positive integers have prime factors
    """
    logger.error(">>> Entering prime_factors(n=%s)", n, extra={"event.action": "prime_factors", "logrite.n": n})
    if n <= 0:
        raise ValueError("Only positive integers have prime factors")
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n = int(n / 2)
        logger.error("prime_factors(n=%s): n → %s", n, n, extra={"event.action": "prime_factors", "logrite.n": n})
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n = int(n / i)
    if n > 2:
        pf.append(n)
    logger.warning("<<< Exiting prime_factors(n=%s)", n, extra={"event.action": "prime_factors", "logrite.n": n})
    return pf


def number_of_divisors(n: int) -> int:
    """Calculate Number of Divisors of an Integer.
    >>> number_of_divisors(100)
    9
    >>> number_of_divisors(0)
    Traceback (most recent call last):
        ...
    ValueError: Only positive numbers are accepted
    >>> number_of_divisors(-10)
    Traceback (most recent call last):
        ...
    ValueError: Only positive numbers are accepted
    """
    logger.error(">>> Entering number_of_divisors(n=%s)", n, extra={"event.action": "number_of_divisors", "logrite.n": n})
    if n <= 0:
        raise ValueError("Only positive numbers are accepted")
    div = 1
    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
        logger.error("number_of_divisors(n=%s): n → %s", n, n, extra={"event.action": "number_of_divisors", "logrite.n": n})
    div *= temp
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        temp = 1
        while n % i == 0:
            temp += 1
            n = int(n / i)
        div *= temp
    if n > 1:
        div *= 2
    logger.warning("<<< Exiting number_of_divisors(n=%s)", n, extra={"event.action": "number_of_divisors", "logrite.n": n})
    return div


def sum_of_divisors(n: int) -> int:
    """Calculate Sum of Divisors.
    >>> sum_of_divisors(100)
    217
    >>> sum_of_divisors(0)
    Traceback (most recent call last):
        ...
    ValueError: Only positive numbers are accepted
    >>> sum_of_divisors(-10)
    Traceback (most recent call last):
        ...
    ValueError: Only positive numbers are accepted
    """
    logger.error(">>> Entering sum_of_divisors(n=%s)", n, extra={"event.action": "sum_of_divisors", "logrite.n": n})
    if n <= 0:
        raise ValueError("Only positive numbers are accepted")
    s = 1
    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
        logger.error("sum_of_divisors(n=%s): n → %s", n, n, extra={"event.action": "sum_of_divisors", "logrite.n": n})
    if temp > 1:
        s *= (2**temp - 1) / (2 - 1)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        temp = 1
        while n % i == 0:
            temp += 1
            n = int(n / i)
        if temp > 1:
            s *= (i**temp - 1) / (i - 1)
    logger.warning("<<< Exiting sum_of_divisors(n=%s)", n, extra={"event.action": "sum_of_divisors", "logrite.n": n})
    return int(s)


def euler_phi(n: int) -> int:
    """Calculate Euler's Phi Function.
    >>> euler_phi(100)
    40
    >>> euler_phi(0)
    Traceback (most recent call last):
        ...
    ValueError: Only positive numbers are accepted
    >>> euler_phi(-10)
    Traceback (most recent call last):
        ...
    ValueError: Only positive numbers are accepted
    """
    logger.error(">>> Entering euler_phi(n=%s)", n, extra={"event.action": "euler_phi", "logrite.n": n})
    if n <= 0:
        raise ValueError("Only positive numbers are accepted")
    s = n
    for x in set(prime_factors(n)):
        s *= (x - 1) / x
    logger.warning("<<< Exiting euler_phi(n=%s)", n, extra={"event.action": "euler_phi", "logrite.n": n})
    return int(s)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
