"""
Project Euler Problem 50: https://projecteuler.net/problem=50

Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def prime_sieve(limit: int) -> list[int]:
    """
    Sieve of Erotosthenes
    Function to return all the prime numbers up to a number 'limit'
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    >>> prime_sieve(3)
    [2]

    >>> prime_sieve(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    logger.debug(">>> Entering prime_sieve(limit=%s)", limit)
    is_prime = [True] * limit
    logger.debug("prime_sieve(limit=%s): is_prime → %s", limit, is_prime)
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True

    for i in range(3, int(limit**0.5 + 1), 2):
        index = i * 2
        logger.debug("prime_sieve(limit=%s): index → %s", limit, index)
        while index < limit:
            is_prime[index] = False
            index = index + i

    primes = [2]
    logger.debug("prime_sieve(limit=%s): primes → %s", limit, primes)

    for i in range(3, limit, 2):
        if is_prime[i]:
            primes.append(i)

    logger.debug("<<< Exiting prime_sieve(limit=%s)", limit)
    return primes


def solution(ceiling: int = 1_000_000) -> int:
    """
    Returns the biggest prime, below the celing, that can be written as the sum
    of consecutive the most consecutive primes.

    >>> solution(500)
    499

    >>> solution(1_000)
    953

    >>> solution(10_000)
    9521
    """
    logger.debug(">>> Entering solution(ceiling=%s)", ceiling)
    primes = prime_sieve(ceiling)
    logger.debug("solution(ceiling=%s): primes → %s", ceiling, primes)
    length = 0
    logger.debug("solution(ceiling=%s): length → %s", ceiling, length)
    largest = 0
    logger.debug("solution(ceiling=%s): largest → %s", ceiling, largest)

    for i in range(len(primes)):
        for j in range(i + length, len(primes)):
            sol = sum(primes[i:j])
            logger.debug("solution(ceiling=%s): sol → %s", ceiling, sol)
            if sol >= ceiling:
                break

            if sol in primes:
                length = j - i
                largest = sol

    logger.debug("<<< Exiting solution(ceiling=%s)", ceiling)
    return largest


if __name__ == "__main__":
    print(f"{solution() = }")
