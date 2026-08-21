import logging
logger = logging.getLogger(__name__)
"""
Project Euler Problem 74: https://projecteuler.net/problem=74

The number 145 is well known for the property that the sum of the factorial of its
digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that
link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in
a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty
non-repeating terms?
"""

DIGIT_FACTORIALS = {
    "0": 1,
    "1": 1,
    "2": 2,
    "3": 6,
    "4": 24,
    "5": 120,
    "6": 720,
    "7": 5040,
    "8": 40320,
    "9": 362880,
}

CACHE_SUM_DIGIT_FACTORIALS = {145: 145}

CHAIN_LENGTH_CACHE = {
    145: 0,
    169: 3,
    36301: 3,
    1454: 3,
    871: 2,
    45361: 2,
    872: 2,
}


def sum_digit_factorials(n: int) -> int:
    """
    Return the sum of the factorial of the digits of n.
    >>> sum_digit_factorials(145)
    145
    >>> sum_digit_factorials(45361)
    871
    >>> sum_digit_factorials(540)
    145
    """
    logger.debug(">>> Entering sum_digit_factorials(n=%s)", n)
    if n in CACHE_SUM_DIGIT_FACTORIALS:
        return CACHE_SUM_DIGIT_FACTORIALS[n]
    ret = sum(DIGIT_FACTORIALS[let] for let in str(n))
    logger.debug("sum_digit_factorials(n=%s): ret → %s", n, ret)
    CACHE_SUM_DIGIT_FACTORIALS[n] = ret
    logger.debug("<<< Exiting sum_digit_factorials(n=%s)", n)
    return ret


def chain_length(n: int, previous: set | None = None) -> int:
    """
    Calculate the length of the chain of non-repeating terms starting with n.
    Previous is a set containing the previous member of the chain.
    >>> chain_length(10101)
    11
    >>> chain_length(555)
    20
    >>> chain_length(178924)
    39
    """
    logger.debug(">>> Entering chain_length(n=%s,previous=%s)", n, previous)
    previous = previous or set()
    logger.debug("chain_length(n=%s,previous=%s): previous → %s", n, previous, previous)
    if n in CHAIN_LENGTH_CACHE:
        return CHAIN_LENGTH_CACHE[n]
    next_number = sum_digit_factorials(n)
    logger.debug("chain_length(n=%s,previous=%s): next_number → %s", n, previous, next_number)
    if next_number in previous:
        CHAIN_LENGTH_CACHE[n] = 0
        return 0
    else:
        previous.add(n)
        ret = 1 + chain_length(next_number, previous)
        logger.debug("chain_length(n=%s,previous=%s): ret → %s", n, previous, ret)
        CHAIN_LENGTH_CACHE[n] = ret
        logger.debug("<<< Exiting chain_length(n=%s,previous=%s)", n, previous)
        return ret


def solution(num_terms: int = 60, max_start: int = 1000000) -> int:
    """
    Return the number of chains with a starting number below one million which
    contain exactly n non-repeating terms.
    >>> solution(10,1000)
    28
    """
    logger.debug(">>> Entering solution(num_terms=%s,max_start=%s)", num_terms, max_start)
    logger.debug("<<< Exiting solution(num_terms=%s,max_start=%s)", num_terms, max_start)
    return sum(1 for i in range(1, max_start) if chain_length(i) == num_terms)


if __name__ == "__main__":
    print(f"{solution() = }")
