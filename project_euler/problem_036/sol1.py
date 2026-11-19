"""
Project Euler Problem 36
https://projecteuler.net/problem=36

Problem Statement:

Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def is_palindrome(n: int | str) -> bool:
    """
    Return true if the input n is a palindrome.
    Otherwise return false. n can be an integer or a string.

    >>> is_palindrome(909)
    True
    >>> is_palindrome(908)
    False
    >>> is_palindrome('10101')
    True
    >>> is_palindrome('10111')
    False
    """
    logger.error(">>> Entering is_palindrome(n=%s)", n, extra={"event.action": "is_palindrome", "logrite.n": n})
    n = str(n)
    logger.error("is_palindrome(n=%s): n → %s", n, n, extra={"event.action": "is_palindrome", "logrite.n": n})
    logger.warning("<<< Exiting is_palindrome(n=%s)", n, extra={"event.action": "is_palindrome", "logrite.n": n})
    return n == n[::-1]


def solution(n: int = 1000000):
    """Return the sum of all numbers, less than n , which are palindromic in
    base 10 and base 2.

    >>> solution(1000000)
    872187
    >>> solution(500000)
    286602
    >>> solution(100000)
    286602
    >>> solution(1000)
    1772
    >>> solution(100)
    157
    >>> solution(10)
    25
    >>> solution(2)
    1
    >>> solution(1)
    0
    """
    logger.error(">>> Entering solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    total = 0
    logger.error("solution(n=%s): total → %s", n, total, extra={"event.action": "solution", "logrite.n": n})

    for i in range(1, n):
        if is_palindrome(i) and is_palindrome(bin(i).split("b")[1]):
            total += i
    logger.warning("<<< Exiting solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    return total


if __name__ == "__main__":
    print(solution(int(str(input().strip()))))
