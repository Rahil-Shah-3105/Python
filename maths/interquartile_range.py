"""
An implementation of interquartile range (IQR) which is a measure of statistical
dispersion, which is the spread of the data.

The function takes the list of numeric values as input and returns the IQR.

Script inspired by this Wikipedia article:
https://en.wikipedia.org/wiki/Interquartile_range
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def find_median(nums: list[int | float]) -> float:
    """
    This is the implementation of the median.
    :param nums: The list of numeric nums
    :return: Median of the list
    >>> find_median(nums=([1, 2, 2, 3, 4]))
    2
    >>> find_median(nums=([1, 2, 2, 3, 4, 4]))
    2.5
    >>> find_median(nums=([-1, 2, 0, 3, 4, -4]))
    1.5
    >>> find_median(nums=([1.1, 2.2, 2, 3.3, 4.4, 4]))
    2.65
    """
    logger.debug(">>> Entering find_median(nums=%s)", nums)
    div, mod = divmod(len(nums), 2)
    if mod:
        return nums[div]
    logger.debug("<<< Exiting find_median(nums=%s)", nums)
    return (nums[div] + nums[(div) - 1]) / 2


def interquartile_range(nums: list[int | float]) -> float:
    """
    Return the interquartile range for a list of numeric values.
    :param nums: The list of numeric values.
    :return: interquartile range

    >>> interquartile_range(nums=[4, 1, 2, 3, 2])
    2.0
    >>> interquartile_range(nums = [-2, -7, -10, 9, 8, 4, -67, 45])
    17.0
    >>> interquartile_range(nums = [-2.1, -7.1, -10.1, 9.1, 8.1, 4.1, -67.1, 45.1])
    17.2
    >>> interquartile_range(nums = [0, 0, 0, 0, 0])
    0.0
    >>> interquartile_range(nums=[])
    Traceback (most recent call last):
    ...
    ValueError: The list is empty. Provide a non-empty list.
    """
    logger.debug(">>> Entering interquartile_range(nums=%s)", nums)
    if not nums:
        raise ValueError("The list is empty. Provide a non-empty list.")
    nums.sort()
    length = len(nums)
    logger.debug("interquartile_range(nums=%s): length → %s", nums, length)
    div, mod = divmod(length, 2)
    q1 = find_median(nums[:div])
    logger.debug("interquartile_range(nums=%s): q1 → %s", nums, q1)
    half_length = sum((div, mod))
    logger.debug("interquartile_range(nums=%s): half_length → %s", nums, half_length)
    q3 = find_median(nums[half_length:length])
    logger.debug("interquartile_range(nums=%s): q3 → %s", nums, q3)
    logger.debug("<<< Exiting interquartile_range(nums=%s)", nums)
    return q3 - q1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
