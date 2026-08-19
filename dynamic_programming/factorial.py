# Factorial of a number using memoization

from functools import lru_cache
import logging
logger = logging.getLogger(__name__)


@lru_cache
def factorial(num: int) -> int:
    """
    >>> factorial(7)
    5040
    >>> factorial(-1)
    Traceback (most recent call last):
      ...
    ValueError: Number should not be negative.
    >>> [factorial(i) for i in range(10)]
    [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    """
    logger.debug(">>> Entering factorial(num=%s)", num)
    if num < 0:
        raise ValueError("Number should not be negative.")

    logger.debug("<<< Exiting factorial(num=%s)", num)
    return 1 if num in (0, 1) else num * factorial(num - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
