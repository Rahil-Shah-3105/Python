import logging
logger = logging.getLogger(__name__)
"""
 == Krishnamurthy Number ==
It is also known as Peterson Number
A Krishnamurthy Number is a number whose sum of the
factorial of the digits equals to the original
number itself.

For example: 145 = 1! + 4! + 5!
    So, 145 is a Krishnamurthy Number
"""


def factorial(digit: int) -> int:
    """
    >>> factorial(3)
    6
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    """
    logger.debug(">>> Entering factorial(digit=%s)", digit)

    logger.debug("<<< Exiting factorial(digit=%s)", digit)
    return 1 if digit in (0, 1) else (digit * factorial(digit - 1))


def krishnamurthy(number: int) -> bool:
    """
    >>> krishnamurthy(145)
    True
    >>> krishnamurthy(240)
    False
    >>> krishnamurthy(1)
    True
    """
    logger.debug(">>> Entering krishnamurthy(number=%s)", number)

    fact_sum = 0
    duplicate = number
    logger.debug("krishnamurthy(number=%s): duplicate → %s", number, duplicate)
    while duplicate > 0:
        duplicate, digit = divmod(duplicate, 10)
        fact_sum += factorial(digit)
    logger.debug("<<< Exiting krishnamurthy(number=%s)", number)
    return fact_sum == number


if __name__ == "__main__":
    print("Program to check whether a number is a Krisnamurthy Number or not.")
    number = int(input("Enter number: ").strip())
    print(
        f"{number} is {'' if krishnamurthy(number) else 'not '}a Krishnamurthy Number."
    )
