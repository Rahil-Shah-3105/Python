from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def median(nums: list) -> int | float:
    """
    Find median of a list of numbers.
    Wiki: https://en.wikipedia.org/wiki/Median

    >>> median([0])
    0
    >>> median([4, 1, 3, 2])
    2.5
    >>> median([2, 70, 6, 50, 20, 8, 4])
    8

    Args:
        nums: List of nums

    Returns:
        Median.
    """
    logger.debug(">>> Entering median(nums=%s)", nums)
    # The sorted function returns list[SupportsRichComparisonT@sorted]
    # which does not support `+`
    logger.debug("<<< Exiting median(nums=%s)", nums)
    sorted_list: list[int] = sorted(nums)
    length = len(sorted_list)
    logger.debug("median(nums=%s): length → %s", nums, length)
    mid_index = length >> 1
    logger.debug("median(nums=%s): mid_index → %s", nums, mid_index)
    return (
        (sorted_list[mid_index] + sorted_list[mid_index - 1]) / 2
        if length % 2 == 0
        else sorted_list[mid_index]
    )


def main():
    logger.debug(">>> Entering main()")
    import doctest

    doctest.testmod()
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
