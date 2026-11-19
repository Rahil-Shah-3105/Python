"""
Project Euler Problem 3: https://projecteuler.net/problem=3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

References:
    - https://en.wikipedia.org/wiki/Prime_number#Unique_factorization
"""
import logging
logger = logging.getLogger(__name__)


def solution(n: int = 600851475143) -> int:
    """
    Returns the largest prime factor of a given number n.

    >>> solution(13195)
    29
    >>> solution(10)
    5
    >>> solution(17)
    17
    >>> solution(3.4)
    3
    >>> solution(0)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater than or equal to one.
    >>> solution(-17)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater than or equal to one.
    >>> solution([])
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or castable to int.
    >>> solution("asd")
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or castable to int.
    """
    logger.error(">>> Entering solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})

    try:
        n = int(n)
    except TypeError, ValueError:
        logger.error("Exception in solution(n=%s)", n, exc_info=True, extra={"event.action": "solution", "event.category": "process", "logrite.n": n})
        raise TypeError("Parameter n must be int or castable to int.")
    if n <= 0:
        raise ValueError("Parameter n must be greater than or equal to one.")
    i = 2
    ans = 0
    if n == 2:
        return 2
    while n > 2:
        while n % i != 0:
            i += 1
        ans = i
        while n % i == 0:
            n = n // i
        i += 1
    logger.warning("<<< Exiting solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    return int(ans)


if __name__ == "__main__":
    print(f"{solution() = }")
