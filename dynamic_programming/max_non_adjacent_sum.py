# Video Explanation: https://www.youtube.com/watch?v=6w60Zi1NtL8&feature=emb_logo

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def maximum_non_adjacent_sum(nums: list[int]) -> int:
    """
    Find the maximum non-adjacent sum of the integers in the nums input list

    >>> maximum_non_adjacent_sum([1, 2, 3])
    4
    >>> maximum_non_adjacent_sum([1, 5, 3, 7, 2, 2, 6])
    18
    >>> maximum_non_adjacent_sum([-1, -5, -3, -7, -2, -2, -6])
    0
    >>> maximum_non_adjacent_sum([499, 500, -3, -7, -2, -2, -6])
    500
    """
    logger.debug(">>> Entering maximum_non_adjacent_sum(nums=%s)", nums)
    if not nums:
        return 0
    max_including = nums[0]
    logger.debug("maximum_non_adjacent_sum(nums=%s): max_including → %s", nums, max_including)
    max_excluding = 0
    logger.debug("maximum_non_adjacent_sum(nums=%s): max_excluding → %s", nums, max_excluding)
    for num in nums[1:]:
        max_including, max_excluding = (
            max_excluding + num,
            max(max_including, max_excluding),
        )
    logger.debug("<<< Exiting maximum_non_adjacent_sum(nums=%s)", nums)
    return max(max_excluding, max_including)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
