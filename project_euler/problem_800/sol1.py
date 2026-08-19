"""
Project Euler Problem 800: https://projecteuler.net/problem=800

An integer of the form p^q q^p with prime numbers p != q is called a hybrid-integer.
For example, 800 = 2^5 5^2 is a hybrid-integer.

We define C(n) to be the number of hybrid-integers less than or equal to n.
You are given C(800) = 2 and C(800^800) = 10790

Find C(800800^800800)
"""

from math import isqrt, log2
import logging
logger = logging.getLogger(__name__)


def calculate_prime_numbers(max_number: int) -> list[int]:
    """
    Returns prime numbers below max_number

    >>> calculate_prime_numbers(10)
    [2, 3, 5, 7]
    """
    logger.debug(">>> Entering calculate_prime_numbers(max_number=%s)", max_number)

    is_prime = [True] * max_number
    logger.debug("calculate_prime_numbers(max_number=%s): is_prime → %s", max_number, is_prime)
    for i in range(2, isqrt(max_number - 1) + 1):
        if is_prime[i]:
            for j in range(i**2, max_number, i):
                is_prime[j] = False

    logger.debug("<<< Exiting calculate_prime_numbers(max_number=%s)", max_number)
    return [i for i in range(2, max_number) if is_prime[i]]


def solution(base: int = 800800, degree: int = 800800) -> int:
    """
    Returns the number of hybrid-integers less than or equal to base^degree

    >>> solution(800, 1)
    2

    >>> solution(800, 800)
    10790
    """
    logger.debug(">>> Entering solution(base=%s,degree=%s)", base, degree)

    upper_bound = degree * log2(base)
    logger.debug("solution(base=%s,degree=%s): upper_bound → %s", base, degree, upper_bound)
    max_prime = int(upper_bound)
    logger.debug("solution(base=%s,degree=%s): max_prime → %s", base, degree, max_prime)
    prime_numbers = calculate_prime_numbers(max_prime)
    logger.debug("solution(base=%s,degree=%s): prime_numbers → %s", base, degree, prime_numbers)

    hybrid_integers_count = 0
    logger.debug("solution(base=%s,degree=%s): hybrid_integers_count → %s", base, degree, hybrid_integers_count)
    left = 0
    logger.debug("solution(base=%s,degree=%s): left → %s", base, degree, left)
    right = len(prime_numbers) - 1
    logger.debug("solution(base=%s,degree=%s): right → %s", base, degree, right)
    while left < right:
        while (
            prime_numbers[right] * log2(prime_numbers[left])
            + prime_numbers[left] * log2(prime_numbers[right])
            > upper_bound
        ):
            right -= 1
        hybrid_integers_count += right - left
        left += 1

    logger.debug("<<< Exiting solution(base=%s,degree=%s)", base, degree)
    return hybrid_integers_count


if __name__ == "__main__":
    print(f"{solution() = }")
