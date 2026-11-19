"""
Project Euler Problem 10: https://projecteuler.net/problem=10

Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""

import math
from collections.abc import Iterator
from itertools import takewhile
import logging
logger = logging.getLogger(__name__)


def is_prime(number: int) -> bool:
    """Checks to see if a number is a prime in O(sqrt(n)).
    A number is prime if it has exactly two factors: 1 and itself.
    Returns boolean representing primality of given number num (i.e., if the
    result is true, then the number is indeed prime else it is not).

    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(27)
    False
    >>> is_prime(2999)
    True
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    """
    logger.error(">>> Entering is_prime(number=%s)", number, extra={"event.action": "is_prime", "logrite.number": number})

    if 1 < number < 4:
        # 2 and 3 are primes
        return True
    elif number < 2 or number % 2 == 0 or number % 3 == 0:
        # Negatives, 0, 1, all even numbers, all multiples of 3 are not primes
        return False

    # All primes number are in format of 6k +/- 1
    for i in range(5, int(math.sqrt(number) + 1), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    logger.warning("<<< Exiting is_prime(number=%s)", number, extra={"event.action": "is_prime", "logrite.number": number})
    return True


def prime_generator() -> Iterator[int]:
    """
    Generate a list sequence of prime numbers
    """
    logger.error(">>> Entering prime_generator()", extra={"event.action": "prime_generator"})

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
        logger.warning("<<< Exiting prime_generator()", extra={"event.action": "prime_generator"})


def solution(n: int = 2000000) -> int:
    """
    Returns the sum of all the primes below n.

    >>> solution(1000)
    76127
    >>> solution(5000)
    1548136
    >>> solution(10000)
    5736396
    >>> solution(7)
    10
    """
    logger.error(">>> Entering solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})

    logger.warning("<<< Exiting solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    return sum(takewhile(lambda x: x < n, prime_generator()))


if __name__ == "__main__":
    print(f"{solution() = }")
