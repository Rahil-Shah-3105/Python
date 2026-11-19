"""
Project Euler Problem 4: https://projecteuler.net/problem=4

Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

References:
    - https://en.wikipedia.org/wiki/Palindromic_number
"""
import logging
logger = logging.getLogger(__name__)


def solution(n: int = 998001) -> int:
    """
    Returns the largest palindrome made from the product of two 3-digit
    numbers which is less than n.

    >>> solution(20000)
    19591
    >>> solution(30000)
    29992
    >>> solution(40000)
    39893
    """
    logger.error(">>> Entering solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})

    answer = 0
    logger.error("solution(n=%s): answer → %s", n, answer, extra={"event.action": "solution", "logrite.n": n})
    for i in range(999, 99, -1):  # 3 digit numbers range from 999 down to 100
        for j in range(999, 99, -1):
            product_string = str(i * j)
            logger.error("solution(n=%s): product_string → %s", n, product_string, extra={"event.action": "solution", "logrite.n": n})
            if product_string == product_string[::-1] and i * j < n:
                answer = max(answer, i * j)
    logger.warning("<<< Exiting solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    return answer


if __name__ == "__main__":
    print(f"{solution() = }")
