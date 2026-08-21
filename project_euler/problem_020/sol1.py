import logging
logger = logging.getLogger(__name__)
"""
Problem 20: https://projecteuler.net/problem=20

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial(num: int) -> int:
    """Find the factorial of a given number n"""
    logger.debug(">>> Entering factorial(num=%s)", num)
    fact = 1
    logger.debug("factorial(num=%s): fact → %s", num, fact)
    for i in range(1, num + 1):
        fact *= i
    logger.debug("<<< Exiting factorial(num=%s)", num)
    return fact


def split_and_add(number: int) -> int:
    """Split number digits and add them."""
    logger.debug(">>> Entering split_and_add(number=%s)", number)
    sum_of_digits = 0
    logger.debug("split_and_add(number=%s): sum_of_digits → %s", number, sum_of_digits)
    while number > 0:
        last_digit = number % 10
        logger.debug("split_and_add(number=%s): last_digit → %s", number, last_digit)
        sum_of_digits += last_digit
        number = number // 10  # Removing the last_digit from the given number
    logger.debug("<<< Exiting split_and_add(number=%s)", number)
    return sum_of_digits


def solution(num: int = 100) -> int:
    """Returns the sum of the digits in the factorial of num
    >>> solution(100)
    648
    >>> solution(50)
    216
    >>> solution(10)
    27
    >>> solution(5)
    3
    >>> solution(3)
    6
    >>> solution(2)
    2
    >>> solution(1)
    1
    """
    logger.debug(">>> Entering solution(num=%s)", num)
    nfact = factorial(num)
    logger.debug("solution(num=%s): nfact → %s", num, nfact)
    result = split_and_add(nfact)
    logger.debug("solution(num=%s): result → %s", num, result)
    logger.debug("<<< Exiting solution(num=%s)", num)
    return result


if __name__ == "__main__":
    print(solution(int(input("Enter the Number: ").strip())))
