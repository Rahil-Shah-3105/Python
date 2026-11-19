"""
Problem 20: https://projecteuler.net/problem=20

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import logging
logger = logging.getLogger(__name__)


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
    fact = 1
    result = 0
    logger.error("solution(num=%s): result → %s", num, result, extra={"event.action": "solution", "logrite.num": num})
    for i in range(1, num + 1):
        fact *= i

    for j in str(fact):
        result += int(j)

    logger.warning("<<< Exiting solution(num=%s)", num, extra={"event.action": "solution", "logrite.num": num})
    return result


if __name__ == "__main__":
    print(solution(int(input("Enter the Number: ").strip())))
