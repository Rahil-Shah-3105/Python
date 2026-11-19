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
    logger.error(">>> Entering perfect_square(num=%s)", num, extra={"event.action": "perfect_square", "logrite.num": num})
    logger.warning("<<< Exiting perfect_square(num=%s)", num, extra={"event.action": "perfect_square", "logrite.num": num})
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
    logger.error(">>> Entering perfect_square_binary_search(n=%s)", n, extra={"event.action": "perfect_square_binary_search", "logrite.n": n})
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        logger.error("perfect_square_binary_search(n=%s): mid → %s", n, mid, extra={"event.action": "perfect_square_binary_search", "logrite.n": n})
        if mid**2 == n:
            return True
        elif mid**2 > n:
            right = mid - 1
        else:
            left = mid + 1
    logger.warning("<<< Exiting perfect_square_binary_search(n=%s)", n, extra={"event.action": "perfect_square_binary_search", "logrite.n": n})
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
