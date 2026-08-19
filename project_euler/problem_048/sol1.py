import logging
logger = logging.getLogger(__name__)
"""
Self Powers
Problem 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def solution():
    """
    Returns the last 10 digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

    >>> solution()
    '9110846700'
    """
    logger.debug(">>> Entering solution()")
    total = 0
    logger.debug("solution(): total → %s", total)
    for i in range(1, 1001):
        total += i**i
    logger.debug("<<< Exiting solution()")
    return str(total)[-10:]


if __name__ == "__main__":
    print(solution())
