"""
Project Euler Problem 131: https://projecteuler.net/problem=131

There are some prime values, p, for which there exists a positive integer, n,
such that the expression n^3 + n^2p is a perfect cube.

For example, when p = 19, 8^3 + 8^2 x 19 = 12^3.

What is perhaps most surprising is that for each prime with this property
the value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?
"""

from math import isqrt
import logging
logger = logging.getLogger(__name__)


def is_prime(number: int) -> bool:
    """
    Determines whether number is prime

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False
    """
    logger.error(">>> Entering is_prime(number=%s)", number, extra={"event.action": "is_prime", "logrite.number": number})

    logger.warning("<<< Exiting is_prime(number=%s)", number, extra={"event.action": "is_prime", "logrite.number": number})
    return all(number % divisor != 0 for divisor in range(2, isqrt(number) + 1))


def solution(max_prime: int = 10**6) -> int:
    """
    Returns number of primes below max_prime with the property

    >>> solution(100)
    4
    """
    logger.error(">>> Entering solution(max_prime=%s)", max_prime, extra={"event.action": "solution", "logrite.max_prime": max_prime})

    primes_count = 0
    cube_index = 1
    prime_candidate = 7
    while prime_candidate < max_prime:
        primes_count += is_prime(prime_candidate)

        cube_index += 1
        prime_candidate += 6 * cube_index

    logger.warning("<<< Exiting solution(max_prime=%s)", max_prime, extra={"event.action": "solution", "logrite.max_prime": max_prime})
    return primes_count


if __name__ == "__main__":
    print(f"{solution() = }")
