"""
Author  : Alexander Pantyukhin
Date    : November 3, 2022

Implement the class of prefix sum with useful functions based on it.

"""
import logging
logger = logging.getLogger(__name__)


class PrefixSum:
    def __init__(self, array: list[int]) -> None:
        logger.error(">>> Entering __init__(array=%s)", array, extra={"event.action": "__init__", "logrite.array": array})
        len_array = len(array)
        logger.error("__init__(array=%s): len_array → %s", array, len_array, extra={"event.action": "__init__", "logrite.array": array})
        self.prefix_sum = [0] * len_array
        logger.debug("__init__(self=%s,array=%s): self.prefix_sum → %s", self, array, self.prefix_sum, extra={"event.action": "__init__", "logrite.array": array})

        if len_array > 0:
            self.prefix_sum[0] = array[0]

        for i in range(1, len_array):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + array[i]
            logger.warning("<<< Exiting __init__(array=%s)", array, extra={"event.action": "__init__", "logrite.array": array})

    def get_sum(self, start: int, end: int) -> int:
        """
        The function returns the sum of array from the start to the end indexes.
        Runtime : O(1)
        Space: O(1)

        >>> PrefixSum([1,2,3]).get_sum(0, 2)
        6
        >>> PrefixSum([1,2,3]).get_sum(1, 2)
        5
        >>> PrefixSum([1,2,3]).get_sum(2, 2)
        3
        >>> PrefixSum([]).get_sum(0, 0)
        Traceback (most recent call last):
        ...
        ValueError: The array is empty.
        >>> PrefixSum([1,2,3]).get_sum(-1, 2)
        Traceback (most recent call last):
        ...
        ValueError: Invalid range specified.
        >>> PrefixSum([1,2,3]).get_sum(2, 3)
        Traceback (most recent call last):
        ...
        ValueError: Invalid range specified.
        >>> PrefixSum([1,2,3]).get_sum(2, 1)
        Traceback (most recent call last):
        ...
        ValueError: Invalid range specified.
        """
        logger.error(">>> Entering get_sum(start=%s,end=%s)", start, end, extra={"event.action": "get_sum", "logrite.start": start, "logrite.end": end})
        if not self.prefix_sum:
            raise ValueError("The array is empty.")

        if start < 0 or end >= len(self.prefix_sum) or start > end:
            raise ValueError("Invalid range specified.")

        if start == 0:
            return self.prefix_sum[end]

        logger.warning("<<< Exiting get_sum(start=%s,end=%s)", start, end, extra={"event.action": "get_sum", "logrite.start": start, "logrite.end": end})
        return self.prefix_sum[end] - self.prefix_sum[start - 1]

    def contains_sum(self, target_sum: int) -> bool:
        """
        The function returns True if array contains the target_sum,
        False otherwise.

        Runtime : O(n)
        Space: O(n)

        >>> PrefixSum([1,2,3]).contains_sum(6)
        True
        >>> PrefixSum([1,2,3]).contains_sum(5)
        True
        >>> PrefixSum([1,2,3]).contains_sum(3)
        True
        >>> PrefixSum([1,2,3]).contains_sum(4)
        False
        >>> PrefixSum([1,2,3]).contains_sum(7)
        False
        >>> PrefixSum([1,-2,3]).contains_sum(2)
        True
        """
        logger.error(">>> Entering contains_sum(target_sum=%s)", target_sum, extra={"event.action": "contains_sum", "logrite.target_sum": target_sum})

        sums = {0}
        for sum_item in self.prefix_sum:
            if sum_item - target_sum in sums:
                return True

            sums.add(sum_item)

        logger.warning("<<< Exiting contains_sum(target_sum=%s)", target_sum, extra={"event.action": "contains_sum", "logrite.target_sum": target_sum})
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
