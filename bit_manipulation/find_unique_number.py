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
    logger.error(">>> Entering find_unique_number(arr=%s)", arr, extra={"event.action": "find_unique_number", "logrite.arr": arr})
    if not arr:
        raise ValueError("input list must not be empty")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("all elements must be integers")

    result = 0
    logger.error("find_unique_number(arr=%s): result → %s", arr, result, extra={"event.action": "find_unique_number", "logrite.arr": arr})
    for num in arr:
        result ^= num
    logger.warning("<<< Exiting find_unique_number(arr=%s)", arr, extra={"event.action": "find_unique_number", "logrite.arr": arr})
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
