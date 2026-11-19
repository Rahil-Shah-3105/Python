import logging
logger = logging.getLogger(__name__)
def find_missing_number(nums: list[int]) -> int:
    """
    Finds the missing number in a list of consecutive integers.

    Args:
        nums: A list of integers.

    Returns:
        The missing number.

    Example:
        >>> find_missing_number([0, 1, 3, 4])
        2
        >>> find_missing_number([4, 3, 1, 0])
        2
        >>> find_missing_number([-4, -3, -1, 0])
        -2
        >>> find_missing_number([-2, 2, 1, 3, 0])
        -1
        >>> find_missing_number([1, 3, 4, 5, 6])
        2
        >>> find_missing_number([6, 5, 4, 2, 1])
        3
        >>> find_missing_number([6, 1, 5, 3, 4])
        2
    """
    logger.error(">>> Entering find_missing_number(nums=%s)", nums, extra={"event.action": "find_missing_number", "logrite.nums": nums})
    low = min(nums)
    logger.error("find_missing_number(nums=%s): low → %s", nums, low, extra={"event.action": "find_missing_number", "logrite.nums": nums})
    high = max(nums)
    logger.error("find_missing_number(nums=%s): high → %s", nums, high, extra={"event.action": "find_missing_number", "logrite.nums": nums})
    missing_number = high

    for i in range(low, high):
        missing_number ^= i ^ nums[i - low]

    logger.warning("<<< Exiting find_missing_number(nums=%s)", nums, extra={"event.action": "find_missing_number", "logrite.nums": nums})
    return missing_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
