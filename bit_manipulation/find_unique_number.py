import logging
logger = logging.getLogger(__name__)
def find_unique_number(arr: list[int]) -> int:
    """
    Given a list of integers where every element appears twice except for one,
    this function returns the element that appears only once using bitwise XOR.

    >>> find_unique_number([1, 1, 2, 2, 3])
    3
    >>> find_unique_number([4, 5, 4, 6, 6])
    5
    >>> find_unique_number([7])
    7
    >>> find_unique_number([10, 20, 10])
    20
    >>> find_unique_number([])
    Traceback (most recent call last):
        ...
    ValueError: input list must not be empty
    >>> find_unique_number([1, 'a', 1])
    Traceback (most recent call last):
        ...
    TypeError: all elements must be integers
    """
    logger.debug(">>> Entering find_unique_number(arr=%s)", arr)
    if not arr:
        raise ValueError("input list must not be empty")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("all elements must be integers")

    result = 0
    logger.debug("find_unique_number(arr=%s): result → %s", arr, result)
    for num in arr:
        result ^= num
    logger.debug("<<< Exiting find_unique_number(arr=%s)", arr)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
