import logging
logger = logging.getLogger(__name__)
def butterfly_pattern(n: int) -> str:
    """
    Creates a butterfly pattern of size n and returns it as a string.

    >>> print(butterfly_pattern(3))
    *   *
    ** **
    *****
    ** **
    *   *
    >>> print(butterfly_pattern(5))
    *       *
    **     **
    ***   ***
    **** ****
    *********
    **** ****
    ***   ***
    **     **
    *       *
    """
    logger.debug(">>> Entering butterfly_pattern(n=%s)", n)
    result = []
    logger.debug("butterfly_pattern(n=%s): result → %s", n, result)

    # Upper part
    for i in range(1, n):
        left_stars = "*" * i
        logger.debug("butterfly_pattern(n=%s): left_stars → %s", n, left_stars)
        spaces = " " * (2 * (n - i) - 1)
        logger.debug("butterfly_pattern(n=%s): spaces → %s", n, spaces)
        right_stars = "*" * i
        logger.debug("butterfly_pattern(n=%s): right_stars → %s", n, right_stars)
        result.append(left_stars + spaces + right_stars)

    # Middle part
    result.append("*" * (2 * n - 1))

    # Lower part
    for i in range(n - 1, 0, -1):
        left_stars = "*" * i
        spaces = " " * (2 * (n - i) - 1)
        right_stars = "*" * i
        result.append(left_stars + spaces + right_stars)

    logger.debug("<<< Exiting butterfly_pattern(n=%s)", n)
    return "\n".join(result)


if __name__ == "__main__":
    n = int(input("Enter the size of the butterfly pattern: "))
    print(butterfly_pattern(n))
