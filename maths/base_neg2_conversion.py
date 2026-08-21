import logging
logger = logging.getLogger(__name__)
def decimal_to_negative_base_2(num: int) -> int:
    """
    This function returns the number negative base 2
        of the decimal number of the input data.

    Args:
        int: The decimal number to convert.

    Returns:
        int: The negative base 2 number.

    Examples:
        >>> decimal_to_negative_base_2(0)
        0
        >>> decimal_to_negative_base_2(-19)
        111101
        >>> decimal_to_negative_base_2(4)
        100
        >>> decimal_to_negative_base_2(7)
        11011
    """
    logger.debug(">>> Entering decimal_to_negative_base_2(num=%s)", num)
    if num == 0:
        return 0
    ans = ""
    logger.debug("decimal_to_negative_base_2(num=%s): ans → %s", num, ans)
    while num != 0:
        num, rem = divmod(num, -2)
        if rem < 0:
            rem += 2
            num += 1
        ans = str(rem) + ans
    logger.debug("<<< Exiting decimal_to_negative_base_2(num=%s)", num)
    return int(ans)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
