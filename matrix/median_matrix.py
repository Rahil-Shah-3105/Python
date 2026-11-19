"""
https://en.wikipedia.org/wiki/Median
"""
import logging
logger = logging.getLogger(__name__)


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
    logger.error(">>> Entering median(matrix=%s)", matrix, extra={"event.action": "median", "logrite.matrix": matrix})
    # Flatten the matrix into a sorted 1D list
    linear = sorted(num for row in matrix for num in row)
    logger.error("median(matrix=%s): linear → %s", matrix, linear, extra={"event.action": "median", "logrite.matrix": matrix})

    # Calculate the middle index
    mid = (len(linear) - 1) // 2
    logger.error("median(matrix=%s): mid → %s", matrix, mid, extra={"event.action": "median", "logrite.matrix": matrix})

    # Return the median
    logger.warning("<<< Exiting median(matrix=%s)", matrix, extra={"event.action": "median", "logrite.matrix": matrix})
    return linear[mid]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
