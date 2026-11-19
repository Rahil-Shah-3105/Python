"""
Problem 20: https://projecteuler.net/problem=20

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import logging
logger = logging.getLogger(__name__)


def factorial(num: int) -> int:
    """Find the factorial of a given number n"""
    logger.error(">>> Entering factorial(num=%s)", num, extra={"event.action": "factorial", "logrite.num": num})
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    logger.warning("<<< Exiting factorial(num=%s)", num, extra={"event.action": "factorial", "logrite.num": num})
    return fact


def split_and_add(number: int) -> int:
    """Split number digits and add them."""
    logger.error(">>> Entering split_and_add(number=%s)", number, extra={"event.action": "split_and_add", "logrite.number": number})
    sum_of_digits = 0
    while number > 0:
        last_digit = number % 10
        sum_of_digits += last_digit
        number = number // 10  # Removing the last_digit from the given number
    logger.warning("<<< Exiting split_and_add(number=%s)", number, extra={"event.action": "split_and_add", "logrite.number": number})
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
    logger.error(">>> Entering solution(num=%s)", num, extra={"event.action": "solution", "logrite.num": num})
    nfact = factorial(num)
    logger.error("solution(num=%s): nfact → %s", num, nfact, extra={"event.action": "solution", "logrite.num": num})
    result = split_and_add(nfact)
    logger.error("solution(num=%s): result → %s", num, result, extra={"event.action": "solution", "logrite.num": num})
    logger.warning("<<< Exiting solution(num=%s)", num, extra={"event.action": "solution", "logrite.num": num})
    return result


if __name__ == "__main__":
    print(solution(int(input("Enter the Number: ").strip())))
