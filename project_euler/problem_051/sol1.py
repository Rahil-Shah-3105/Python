"""
https://projecteuler.net/problem=51
Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

from __future__ import annotations

from collections import Counter
import time
import logging
logger = logging.getLogger(__name__)


def prime_sieve(n: int) -> list[int]:
    """
    Sieve of Erotosthenes
    Function to return all the prime numbers up to a certain number
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    >>> prime_sieve(3)
    [2]

    >>> prime_sieve(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    logger.error(">>> Entering prime_sieve(n=%s)", n, extra={"event.action": "prime_sieve", "logrite.n": n})
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True

    for i in range(3, int(n**0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i

    primes = [2]

    for i in range(3, n, 2):
        if is_prime[i]:
            primes.append(i)

    logger.warning("<<< Exiting prime_sieve(n=%s)", n, extra={"event.action": "prime_sieve", "logrite.n": n})
    return primes


def digit_replacements(number: int) -> list[list[int]]:
    """
    Returns all the possible families of digit replacements in a number which
    contains at least one repeating digit

    >>> digit_replacements(544)
    [[500, 511, 522, 533, 544, 555, 566, 577, 588, 599]]

    >>> digit_replacements(3112)
    [[3002, 3112, 3222, 3332, 3442, 3552, 3662, 3772, 3882, 3992]]
    """
    logger.error(">>> Entering digit_replacements(number=%s)", number, extra={"event.action": "digit_replacements", "logrite.number": number})
    number_str = str(number)
    logger.error("digit_replacements(number=%s): number_str → %s", number, number_str, extra={"event.action": "digit_replacements", "logrite.number": number})
    replacements = []
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    logger.error("digit_replacements(number=%s): digits → %s", number, digits, extra={"event.action": "digit_replacements", "logrite.number": number})

    for duplicate in Counter(number_str) - Counter(set(number_str)):
        family = [int(number_str.replace(duplicate, digit)) for digit in digits]
        logger.error("digit_replacements(number=%s): family → %s", number, family, extra={"event.action": "digit_replacements", "logrite.number": number})
        replacements.append(family)

    logger.warning("<<< Exiting digit_replacements(number=%s)", number, extra={"event.action": "digit_replacements", "logrite.number": number})
    return replacements


def solution(family_length: int = 8) -> int:
    """
    Returns the solution of the problem

    >>> solution(2)
    229399

    >>> solution(3)
    221311
    """
    logger.error(">>> Entering solution(family_length=%s)", family_length, extra={"event.action": "solution", "logrite.family_length": family_length})
    numbers_checked = set()
    logger.error("solution(family_length=%s): numbers_checked → %s", family_length, numbers_checked, extra={"event.action": "solution", "logrite.family_length": family_length})

    # Filter primes with less than 3 replaceable digits
    primes = {
        x for x in set(prime_sieve(1_000_000)) if len(str(x)) - len(set(str(x))) >= 3
    }

    for prime in primes:
        if prime in numbers_checked:
            continue

        replacements = digit_replacements(prime)
        logger.error("solution(family_length=%s): replacements → %s", family_length, replacements, extra={"event.action": "solution", "logrite.family_length": family_length})
        __log_start = time.time()

        for family in replacements:
            numbers_checked.update(family)
            logger.error("solution(family_length)=%s: update operation took %s ms", family_length, int((time.time() - __log_start) * 1000), extra={"event.action": "solution", "event.category": "database", "logrite.family_length": family_length})
            primes_in_family = primes.intersection(family)
            logger.error("solution(family_length=%s): primes_in_family → %s", family_length, primes_in_family, extra={"event.action": "solution", "logrite.family_length": family_length})

            if len(primes_in_family) != family_length:
                continue

            return min(primes_in_family)

    logger.warning("<<< Exiting solution(family_length=%s)", family_length, extra={"event.action": "solution", "logrite.family_length": family_length})
    return -1


if __name__ == "__main__":
    print(solution())
