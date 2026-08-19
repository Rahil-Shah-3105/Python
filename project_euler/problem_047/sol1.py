"""
Combinatoric selections

Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
"""

from functools import lru_cache
import logging
logger = logging.getLogger(__name__)


def unique_prime_factors(n: int) -> set:
    """
    Find unique prime factors of an integer.
    Tests include sorting because only the set matters,
    not the order in which it is produced.
    >>> sorted(set(unique_prime_factors(14)))
    [2, 7]
    >>> sorted(set(unique_prime_factors(644)))
    [2, 7, 23]
    >>> sorted(set(unique_prime_factors(646)))
    [2, 17, 19]
    """
    logger.debug(">>> Entering unique_prime_factors(n=%s)", n)
    i = 2
    factors = set()
    logger.debug("unique_prime_factors(n=%s): factors → %s", n, factors)
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    logger.debug("<<< Exiting unique_prime_factors(n=%s)", n)
    return factors


@lru_cache
def upf_len(num: int) -> int:
    """
    Memoize upf() length results for a given value.
    >>> upf_len(14)
    2
    """
    logger.debug(">>> Entering upf_len(num=%s)", num)
    logger.debug("<<< Exiting upf_len(num=%s)", num)
    return len(unique_prime_factors(num))


def equality(iterable: list) -> bool:
    """
    Check the equality of ALL elements in an iterable
    >>> equality([1, 2, 3, 4])
    False
    >>> equality([2, 2, 2, 2])
    True
    >>> equality([1, 2, 3, 2, 1])
    False
    """
    logger.debug(">>> Entering equality(iterable=%s)", iterable)
    logger.debug("<<< Exiting equality(iterable=%s)", iterable)
    return len(set(iterable)) in (0, 1)


def run(n: int) -> list[int]:
    """
    Runs core process to find problem solution.
    >>> run(3)
    [644, 645, 646]
    """
    logger.debug(">>> Entering run(n=%s)", n)

    # Incrementor variable for our group list comprehension.
    # This is the first number in each list of values
    # to test.
    base = 2
    logger.debug("run(n=%s): base → %s", n, base)

    while True:
        # Increment each value of a generated range
        group = [base + i for i in range(n)]
        logger.debug("run(n=%s): group → %s", n, group)

        # Run elements through the unique_prime_factors function
        # Append our target number to the end.
        checker = [upf_len(x) for x in group]
        logger.debug("run(n=%s): checker → %s", n, checker)
        checker.append(n)

        # If all numbers in the list are equal, return the group variable.
        if equality(checker):
            logger.debug("<<< Exiting run(n=%s)", n)
            return group

        # Increment our base variable by 1
        base += 1


def solution(n: int = 4) -> int | None:
    """Return the first value of the first four consecutive integers to have four
    distinct prime factors each.
    >>> solution()
    134043
    """
    logger.debug(">>> Entering solution(n=%s)", n)
    results = run(n)
    logger.debug("solution(n=%s): results → %s", n, results)
    logger.debug("<<< Exiting solution(n=%s)", n)
    return results[0] if len(results) else None


if __name__ == "__main__":
    print(solution())
