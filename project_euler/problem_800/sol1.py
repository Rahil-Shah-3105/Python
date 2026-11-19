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
    logger.error(">>> Entering calculate_prime_numbers(max_number=%s)", max_number, extra={"event.action": "calculate_prime_numbers", "logrite.max_number": max_number})

    is_prime = [True] * max_number
    for i in range(2, isqrt(max_number - 1) + 1):
        if is_prime[i]:
            for j in range(i**2, max_number, i):
                is_prime[j] = False

    logger.warning("<<< Exiting calculate_prime_numbers(max_number=%s)", max_number, extra={"event.action": "calculate_prime_numbers", "logrite.max_number": max_number})
    return [i for i in range(2, max_number) if is_prime[i]]


def solution(base: int = 800800, degree: int = 800800) -> int:
    """
    Returns the number of hybrid-integers less than or equal to base^degree

    >>> solution(800, 1)
    2

    >>> solution(800, 800)
    10790
    """
    logger.error(">>> Entering solution(base=%s,degree=%s)", base, degree, extra={"event.action": "solution", "logrite.base": base, "logrite.degree": degree})

    upper_bound = degree * log2(base)
    logger.error("solution(base=%s,degree=%s): upper_bound → %s", base, degree, upper_bound, extra={"event.action": "solution", "logrite.base": base, "logrite.degree": degree})
    max_prime = int(upper_bound)
    logger.error("solution(base=%s,degree=%s): max_prime → %s", base, degree, max_prime, extra={"event.action": "solution", "logrite.base": base, "logrite.degree": degree})
    prime_numbers = calculate_prime_numbers(max_prime)
    logger.error("solution(base=%s,degree=%s): prime_numbers → %s", base, degree, prime_numbers, extra={"event.action": "solution", "logrite.base": base, "logrite.degree": degree})

    hybrid_integers_count = 0
    left = 0
    right = len(prime_numbers) - 1
    logger.error("solution(base=%s,degree=%s): right → %s", base, degree, right, extra={"event.action": "solution", "logrite.base": base, "logrite.degree": degree})
    while left < right:
        while (
            prime_numbers[right] * log2(prime_numbers[left])
            + prime_numbers[left] * log2(prime_numbers[right])
            > upper_bound
        ):
            right -= 1
        hybrid_integers_count += right - left
        left += 1

    logger.warning("<<< Exiting solution(base=%s,degree=%s)", base, degree, extra={"event.action": "solution", "logrite.base": base, "logrite.degree": degree})
    return hybrid_integers_count


if __name__ == "__main__":
    print(f"{solution() = }")
