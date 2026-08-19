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
    logger.debug(">>> Entering find_missing_number(nums=%s)", nums)
    low = min(nums)
    logger.debug("find_missing_number(nums=%s): low → %s", nums, low)
    high = max(nums)
    logger.debug("find_missing_number(nums=%s): high → %s", nums, high)
    missing_number = high
    logger.debug("find_missing_number(nums=%s): missing_number → %s", nums, missing_number)

    for i in range(low, high):
        missing_number ^= i ^ nums[i - low]

    logger.debug("<<< Exiting find_missing_number(nums=%s)", nums)
    return missing_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
