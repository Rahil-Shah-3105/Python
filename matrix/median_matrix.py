import logging
logger = logging.getLogger(__name__)
"""
https://en.wikipedia.org/wiki/Median
"""


def median(matrix: list[list[int]]) -> int:
    """
    Calculate the median of a sorted matrix.

    Args:
        matrix: A 2D matrix of integers.

    Returns:
        The median value of the matrix.

    Examples:
        >>> matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
        >>> median(matrix)
        5

        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> median(matrix)
        3
    """
    logger.debug(">>> Entering median(matrix=%s)", matrix)
    # Flatten the matrix into a sorted 1D list
    linear = sorted(num for row in matrix for num in row)
    logger.debug("median(matrix=%s): linear → %s", matrix, linear)

    # Calculate the middle index
    mid = (len(linear) - 1) // 2
    logger.debug("median(matrix=%s): mid → %s", matrix, mid)

    # Return the median
    logger.debug("<<< Exiting median(matrix=%s)", matrix)
    return linear[mid]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
