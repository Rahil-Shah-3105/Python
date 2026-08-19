import math
import logging
logger = logging.getLogger(__name__)


def perfect_square(num: int) -> bool:
    """
    Check if a number is perfect square number or not
    :param num: the number to be checked
    :return: True if number is square number, otherwise False

    >>> perfect_square(9)
    True
    >>> perfect_square(16)
    True
    >>> perfect_square(1)
    True
    >>> perfect_square(0)
    True
    >>> perfect_square(10)
    False
    """
    logger.debug(">>> Entering perfect_square(num=%s)", num)
    logger.debug("<<< Exiting perfect_square(num=%s)", num)
    return math.sqrt(num) * math.sqrt(num) == num


def perfect_square_binary_search(n: int) -> bool:
    """
    Check if a number is perfect square using binary search.
    Time complexity : O(Log(n))
    Space complexity: O(1)

    >>> perfect_square_binary_search(9)
    True
    >>> perfect_square_binary_search(16)
    True
    >>> perfect_square_binary_search(1)
    True
    >>> perfect_square_binary_search(0)
    True
    >>> perfect_square_binary_search(10)
    False
    >>> perfect_square_binary_search(-1)
    False
    >>> perfect_square_binary_search(1.1)
    False
    >>> perfect_square_binary_search("a")
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'str'
    >>> perfect_square_binary_search(None)
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'NoneType'
    >>> perfect_square_binary_search([])
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'list'
    """
    logger.debug(">>> Entering perfect_square_binary_search(n=%s)", n)
    left = 0
    logger.debug("perfect_square_binary_search(n=%s): left → %s", n, left)
    right = n
    logger.debug("perfect_square_binary_search(n=%s): right → %s", n, right)
    while left <= right:
        mid = (left + right) // 2
        logger.debug("perfect_square_binary_search(n=%s): mid → %s", n, mid)
        if mid**2 == n:
            return True
        elif mid**2 > n:
            right = mid - 1
        else:
            left = mid + 1
    logger.debug("<<< Exiting perfect_square_binary_search(n=%s)", n)
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
