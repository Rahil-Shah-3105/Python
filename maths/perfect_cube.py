import logging
logger = logging.getLogger(__name__)
def perfect_cube(n: int) -> bool:
    """
    Check if a number is a perfect cube or not.

    >>> perfect_cube(27)
    True
    >>> perfect_cube(4)
    False
    """
    logger.debug(">>> Entering perfect_cube(n=%s)", n)
    val = n ** (1 / 3)
    logger.debug("perfect_cube(n=%s): val → %s", n, val)
    logger.debug("<<< Exiting perfect_cube(n=%s)", n)
    return (val * val * val) == n


def perfect_cube_binary_search(n: int) -> bool:
    """
    Check if a number is a perfect cube or not using binary search.
    Time complexity : O(Log(n))
    Space complexity: O(1)

    >>> perfect_cube_binary_search(27)
    True
    >>> perfect_cube_binary_search(64)
    True
    >>> perfect_cube_binary_search(4)
    False
    >>> perfect_cube_binary_search("a")
    Traceback (most recent call last):
        ...
    TypeError: perfect_cube_binary_search() only accepts integers
    >>> perfect_cube_binary_search(0.1)
    Traceback (most recent call last):
        ...
    TypeError: perfect_cube_binary_search() only accepts integers
    """
    logger.debug(">>> Entering perfect_cube_binary_search(n=%s)", n)
    if not isinstance(n, int):
        raise TypeError("perfect_cube_binary_search() only accepts integers")
    if n < 0:
        n = -n
    left = 0
    logger.debug("perfect_cube_binary_search(n=%s): left → %s", n, left)
    right = n
    logger.debug("perfect_cube_binary_search(n=%s): right → %s", n, right)
    while left <= right:
        mid = left + (right - left) // 2
        logger.debug("perfect_cube_binary_search(n=%s): mid → %s", n, mid)
        if mid * mid * mid == n:
            return True
        elif mid * mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1
    logger.debug("<<< Exiting perfect_cube_binary_search(n=%s)", n)
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
