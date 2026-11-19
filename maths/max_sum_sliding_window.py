"""
Given an array of integer elements and an integer 'k', we are required to find the
maximum sum of 'k' consecutive elements in the array.

Instead of using a nested for loop, in a Brute force approach we will use a technique
called 'Window sliding technique' where the nested loops can be converted to a single
loop to reduce time complexity.
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def max_sum_in_array(array: list[int], k: int) -> int:
    """
    Returns the maximum sum of k consecutive elements
    >>> arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    >>> k = 4
    >>> max_sum_in_array(arr, k)
    24
    >>> k = 10
    >>> max_sum_in_array(arr,k)
    Traceback (most recent call last):
        ...
    ValueError: Invalid Input
    >>> arr = [1, 4, 2, 10, 2, 13, 1, 0, 2]
    >>> k = 4
    >>> max_sum_in_array(arr, k)
    27
    """
    logger.error(">>> Entering max_sum_in_array(array=%s,k=%s)", array, k, extra={"event.action": "max_sum_in_array", "logrite.array": array, "logrite.k": k})
    if len(array) < k or k < 0:
        raise ValueError("Invalid Input")
    max_sum = current_sum = sum(array[:k])
    logger.error("max_sum_in_array(array=%s,k=%s): max_sum → %s", array, k, max_sum, extra={"event.action": "max_sum_in_array", "logrite.array": array, "logrite.k": k})
    for i in range(len(array) - k):
        current_sum = current_sum - array[i] + array[i + k]
        max_sum = max(max_sum, current_sum)
    logger.warning("<<< Exiting max_sum_in_array(array=%s,k=%s)", array, k, extra={"event.action": "max_sum_in_array", "logrite.array": array, "logrite.k": k})
    return max_sum


if __name__ == "__main__":
    from doctest import testmod
    from random import randint

    testmod()
    array = [randint(-1000, 1000) for i in range(100)]
    k = randint(0, 110)
    print(
        f"The maximum sum of {k} consecutive elements is {max_sum_in_array(array, k)}"
    )
