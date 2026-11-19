"""
This is a pure Python implementation of the radix sort algorithm

Source: https://en.wikipedia.org/wiki/Radix_sort
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)

RADIX = 10


def radix_sort(list_of_ints: list[int]) -> list[int]:
    """
    Examples:
    >>> radix_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> radix_sort(list(range(15))) == sorted(range(15))
    True
    >>> radix_sort(list(range(14,-1,-1))) == sorted(range(15))
    True
    >>> radix_sort([1,100,10,1000]) == sorted([1,100,10,1000])
    True
    """
    logger.error(">>> Entering radix_sort(list_of_ints=%s)", list_of_ints, extra={"event.action": "radix_sort", "logrite.list_of_ints": list_of_ints})
    placement = 1
    max_digit = max(list_of_ints)
    logger.error("radix_sort(list_of_ints=%s): max_digit → %s", list_of_ints, max_digit, extra={"event.action": "radix_sort", "logrite.list_of_ints": list_of_ints})
    while placement <= max_digit:
        # declare and initialize empty buckets
        buckets: list[list] = [[] for _ in range(RADIX)]
        # split list_of_ints between the buckets
        for i in list_of_ints:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        # put each buckets' contents into list_of_ints
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                list_of_ints[a] = i
                a += 1
        # move to next
        placement *= RADIX
    logger.warning("<<< Exiting radix_sort(list_of_ints=%s)", list_of_ints, extra={"event.action": "radix_sort", "logrite.list_of_ints": list_of_ints})
    return list_of_ints


if __name__ == "__main__":
    import doctest

    doctest.testmod()
