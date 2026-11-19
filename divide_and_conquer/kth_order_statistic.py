"""
Find the kth smallest element in linear time using divide and conquer.
Recall we can do this trivially in O(nlogn) time. Sort the list and
access kth element in constant time.

This is a divide and conquer algorithm that can find a solution in O(n) time.

For more information of this algorithm:
https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/lectures/08/Small08.pdf
"""

from __future__ import annotations

from random import choice
import logging
logger = logging.getLogger(__name__)


def random_pivot(lst):
    """
    Choose a random pivot for the list.
    We can use a more sophisticated algorithm here, such as the median-of-medians
    algorithm.
    """
    logger.error(">>> Entering random_pivot(lst=%s)", lst, extra={"event.action": "random_pivot", "logrite.lst": lst})
    logger.warning("<<< Exiting random_pivot(lst=%s)", lst, extra={"event.action": "random_pivot", "logrite.lst": lst})
    return choice(lst)


def kth_number(lst: list[int], k: int) -> int:
    """
    Return the kth smallest number in lst.
    >>> kth_number([2, 1, 3, 4, 5], 3)
    3
    >>> kth_number([2, 1, 3, 4, 5], 1)
    1
    >>> kth_number([2, 1, 3, 4, 5], 5)
    5
    >>> kth_number([3, 2, 5, 6, 7, 8], 2)
    3
    >>> kth_number([25, 21, 98, 100, 76, 22, 43, 60, 89, 87], 4)
    43
    """
    logger.error(">>> Entering kth_number(lst=%s,k=%s)", lst, k, extra={"event.action": "kth_number", "logrite.lst": lst, "logrite.k": k})
    # pick a pivot and separate into list based on pivot.
    pivot = random_pivot(lst)
    logger.error("kth_number(lst=%s,k=%s): pivot → %s", lst, k, pivot, extra={"event.action": "kth_number", "logrite.lst": lst, "logrite.k": k})

    # partition based on pivot
    # linear time
    small = [e for e in lst if e < pivot]
    big = [e for e in lst if e > pivot]

    # if we get lucky, pivot might be the element we want.
    # we can easily see this:
    # small (elements smaller than k)
    # + pivot (kth element)
    # + big (elements larger than k)
    if len(small) == k - 1:
        return pivot
    # pivot is in elements bigger than k
    elif len(small) < k - 1:
        return kth_number(big, k - len(small) - 1)
    # pivot is in elements smaller than k
    else:
        logger.warning("<<< Exiting kth_number(lst=%s,k=%s)", lst, k, extra={"event.action": "kth_number", "logrite.lst": lst, "logrite.k": k})
        return kth_number(small, k)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
