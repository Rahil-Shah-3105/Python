#!/usr/bin/env python3

"""
Pure Python implementations of binary search algorithms

For doctests run the following command:
python3 -m doctest -v binary_search.py

For manual testing run:
python3 binary_search.py
"""

import bisect
from itertools import pairwise
import logging
logger = logging.getLogger(__name__)


def bisect_left(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> int:
    logger.error(">>> Entering bisect_left(sorted_collection=%s,item=%s,lo=%s,hi=%s)", sorted_collection, item, lo, hi, extra={"event.action": "bisect_left", "logrite.sorted_collection": sorted_collection, "logrite.item": item, "logrite.lo": lo, "logrite.hi": hi})
    """
    Locates the first element in a sorted array that is larger or equal to a given
    value.

    It has the same interface as
    https://docs.python.org/3/library/bisect.html#bisect.bisect_left .

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item to bisect
    :param lo: lowest index to consider (as in sorted_collection[lo:hi])
    :param hi: past the highest index to consider (as in sorted_collection[lo:hi])
    :return: index i such that all values in sorted_collection[lo:i] are < item and all
        values in sorted_collection[i:hi] are >= item.

    Examples:
    >>> bisect_left([0, 5, 7, 10, 15], 0)
    0
    >>> bisect_left([0, 5, 7, 10, 15], 6)
    2
    >>> bisect_left([0, 5, 7, 10, 15], 20)
    5
    >>> bisect_left([0, 5, 7, 10, 15], 15, 1, 3)
    3
    >>> bisect_left([0, 5, 7, 10, 15], 6, 2)
    2
    """
    if hi < 0:
        hi = len(sorted_collection)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        logger.error("bisect_left(sorted_collection=%s,item=%s,lo=%s,hi=%s): mid → %s", sorted_collection, item, lo, hi, mid, extra={"event.action": "bisect_left", "logrite.sorted_collection": sorted_collection, "logrite.item": item, "logrite.lo": lo, "logrite.hi": hi})
        if sorted_collection[mid] < item:
            lo = mid + 1
        else:
            hi = mid

    logger.warning("<<< Exiting bisect_left(sorted_collection=%s,item=%s,lo=%s,hi=%s)", sorted_collection, item, lo, hi, extra={"event.action": "bisect_left", "logrite.sorted_collection": sorted_collection, "logrite.item": item, "logrite.lo": lo, "logrite.hi": hi})
    return lo


def bisect_right(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> int:
    logger.error(">>> Entering bisect_right(sorted_collection=%s,item=%s,lo=%s,hi=%s)", sorted_collection, item, lo, hi, extra={"event.action": "bisect_right", "logrite.sorted_collection": sorted_collection, "logrite.item": item, "logrite.lo": lo, "logrite.hi": hi})
    """
    Locates the first element in a sorted array that is larger than a given value.

    It has the same interface as
    https://docs.python.org/3/library/bisect.html#bisect.bisect_right .

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item to bisect
    :param lo: lowest index to consider (as in sorted_collection[lo:hi])
    :param hi: past the highest index to consider (as in sorted_collection[lo:hi])
    :return: index i such that all values in sorted_collection[lo:i] are <= item and
        all values in sorted_collection[i:hi] are > item.

    Examples:
    >>> bisect_right([0, 5, 7, 10, 15], 0)
    1
    >>> bisect_right([0, 5, 7, 10, 15], 15)
    5
    >>> bisect_right([0, 5, 7, 10, 15], 6)
    2
    >>> bisect_right([0, 5, 7, 10, 15], 15, 1, 3)
    3
    >>> bisect_right([0, 5, 7, 10, 15], 6, 2)
    2
    """
    if hi < 0:
        hi = len(sorted_collection)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        logger.error("bisect_right(sorted_collection=%s,item=%s,lo=%s,hi=%s): mid → %s", sorted_collection, item, lo, hi, mid, extra={"event.action": "bisect_right", "logrite.sorted_collection": sorted_collection, "logrite.item": item, "logrite.lo": lo, "logrite.hi": hi})
        if sorted_collection[mid] <= item:
            lo = mid + 1
        else:
            hi = mid

    logger.warning("<<< Exiting bisect_right(sorted_collection=%s,item=%s,lo=%s,hi=%s)", sorted_collection, item, lo, hi, extra={"event.action": "bisect_right", "logrite.sorted_collection": sorted_collection, "logrite.item": item, "logrite.lo": lo, "logrite.hi": hi})
    return lo


def insort_left(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> None:
    logger.error(">>> Entering insort_left(sorted_collection=%s,item=%s,lo=%s,hi=%s)", sorted_collection, item, lo, hi, extra={"event.action": "insort_left", "logrite.sorted_collection": sorted_collection, "logrite.item": item, "logrite.lo": lo, "logrite.hi": hi})
    """
    Inserts a given value into a sorted array before other values with the same value.

    It has the same interface as
    https://docs.python.org/3/library/bisect.html#bisect.insort_left .

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item to insert
    :param lo: lowest index to consider (as in sorted_collection[lo:hi])
    :param hi: past the highest index to consider (as in sorted_collection[lo:hi])

    Examples:
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_left(sorted_collection, 6)
    >>> sorted_collection
    [0, 5, 6, 7, 10, 15]
    >>> sorted_collection = [(0, 0), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item = (5, 5)
    >>> insort_left(sorted_collection, item)
    >>> sorted_collection
    [(0, 0), (5, 5), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item is sorted_collection[1]
    True
    >>> item is sorted_collection[2]
    False
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_left(sorted_collection, 20)
    >>> sorted_collection
    [0, 5, 7, 10, 15, 20]
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_left(sorted_collection, 15, 1, 3)
    >>> sorted_collection
    [0, 5, 7, 15, 10, 15]
    """
    sorted_collection.insert(bisect_left(sorted_collection, item, lo, hi), item)
    logger.warning("<<< Exiting insort_left(sorted_collection=%s,item=%s,lo=%s,hi=%s)", sorted_collection, item, lo, hi, extra={"event.action": "insort_left", "logrite.sorted_collection": sorted_collection, "logrite.item": item, "logrite.lo": lo, "logrite.hi": hi})


def insort_right(
    sorted_collection: list[int], item: int, lo: int = 0, hi: int = -1
) -> None:
    logger.error(">>> Entering insort_right(sorted_collection=%s,item=%s,lo=%s,hi=%s)", sorted_collection, item, lo, hi, extra={"event.action": "insort_right", "logrite.sorted_collection": sorted_collection, "logrite.item": item, "logrite.lo": lo, "logrite.hi": hi})
    """
    Inserts a given value into a sorted array after other values with the same value.

    It has the same interface as
    https://docs.python.org/3/library/bisect.html#bisect.insort_right .

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item to insert
    :param lo: lowest index to consider (as in sorted_collection[lo:hi])
    :param hi: past the highest index to consider (as in sorted_collection[lo:hi])

    Examples:
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_right(sorted_collection, 6)
    >>> sorted_collection
    [0, 5, 6, 7, 10, 15]
    >>> sorted_collection = [(0, 0), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item = (5, 5)
    >>> insort_right(sorted_collection, item)
    >>> sorted_collection
    [(0, 0), (5, 5), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item is sorted_collection[1]
    False
    >>> item is sorted_collection[2]
    True
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_right(sorted_collection, 20)
    >>> sorted_collection
    [0, 5, 7, 10, 15, 20]
    >>> sorted_collection = [0, 5, 7, 10, 15]
    >>> insort_right(sorted_collection, 15, 1, 3)
    >>> sorted_collection
    [0, 5, 7, 15, 10, 15]
    """
    sorted_collection.insert(bisect_right(sorted_collection, item, lo, hi), item)
    logger.warning("<<< Exiting insort_right(sorted_collection=%s,item=%s,lo=%s,hi=%s)", sorted_collection, item, lo, hi, extra={"event.action": "insort_right", "logrite.sorted_collection": sorted_collection, "logrite.item": item, "logrite.lo": lo, "logrite.hi": hi})


def binary_search(sorted_collection: list[int], item: int) -> int:
    """Pure implementation of a binary search algorithm in Python

    Be careful collection must be ascending sorted otherwise, the result will be
    unpredictable

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of the found item or -1 if the item is not found

    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0
    >>> binary_search([0, 5, 7, 10, 15], 15)
    4
    >>> binary_search([0, 5, 7, 10, 15], 5)
    1
    >>> binary_search([0, 5, 7, 10, 15], 6)
    -1
    """
    logger.error(">>> Entering binary_search(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "binary_search", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
    if any(a > b for a, b in pairwise(sorted_collection)):
        raise ValueError("sorted_collection must be sorted in ascending order")
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        logger.error("binary_search(sorted_collection=%s,item=%s): midpoint → %s", sorted_collection, item, midpoint, extra={"event.action": "binary_search", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    logger.warning("<<< Exiting binary_search(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "binary_search", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
    return -1


def binary_search_std_lib(sorted_collection: list[int], item: int) -> int:
    """Pure implementation of a binary search algorithm in Python using stdlib

    Be careful collection must be ascending sorted otherwise, the result will be
    unpredictable

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of the found item or -1 if the item is not found

    Examples:
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 0)
    0
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 15)
    4
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 5)
    1
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 6)
    -1
    """
    logger.error(">>> Entering binary_search_std_lib(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "binary_search_std_lib", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
    if list(sorted_collection) != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    logger.warning("<<< Exiting binary_search_std_lib(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "binary_search_std_lib", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
    return -1


def binary_search_with_duplicates(sorted_collection: list[int], item: int) -> list[int]:
    """Pure implementation of a binary search algorithm in Python that supports
    duplicates.

    Resources used:
    https://stackoverflow.com/questions/13197552/using-binary-search-with-sorted-array-with-duplicates

    The collection must be sorted in ascending order; otherwise the result will be
    unpredictable. If the target appears multiple times, this function returns a
    list of all indexes where the target occurs. If the target is not found,
    this function returns an empty list.

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search for
    :return: a list of indexes where the item is found (empty list if not found)

    Examples:
    >>> binary_search_with_duplicates([0, 5, 7, 10, 15], 0)
    [0]
    >>> binary_search_with_duplicates([0, 5, 7, 10, 15], 15)
    [4]
    >>> binary_search_with_duplicates([1, 2, 2, 2, 3], 2)
    [1, 2, 3]
    >>> binary_search_with_duplicates([1, 2, 2, 2, 3], 4)
    []
    """
    logger.error(">>> Entering binary_search_with_duplicates(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "binary_search_with_duplicates", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
    if list(sorted_collection) != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
        logger.warning("<<< Exiting binary_search_with_duplicates(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "binary_search_with_duplicates", "logrite.sorted_collection": sorted_collection, "logrite.item": item})

    def lower_bound(sorted_collection: list[int], item: int) -> int:
        """
        Returns the index of the first element greater than or equal to the item.

        :param sorted_collection: The sorted list to search.
        :param item: The item to find the lower bound for.
        :return: The index where the item can be inserted while maintaining order.
        """
        logger.error(">>> Entering lower_bound(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "lower_bound", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
        left = 0
        right = len(sorted_collection)
        while left < right:
            midpoint = left + (right - left) // 2
            logger.error("lower_bound(sorted_collection=%s,item=%s): midpoint → %s", sorted_collection, item, midpoint, extra={"event.action": "lower_bound", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
            current_item = sorted_collection[midpoint]
            if current_item < item:
                left = midpoint + 1
            else:
                right = midpoint
        logger.warning("<<< Exiting lower_bound(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "lower_bound", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
        return left

    def upper_bound(sorted_collection: list[int], item: int) -> int:
        """
        Returns the index of the first element strictly greater than the item.

        :param sorted_collection: The sorted list to search.
        :param item: The item to find the upper bound for.
        :return: The index where the item can be inserted after all existing instances.
        """
        logger.error(">>> Entering upper_bound(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "upper_bound", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
        left = 0
        right = len(sorted_collection)
        while left < right:
            midpoint = left + (right - left) // 2
            logger.error("upper_bound(sorted_collection=%s,item=%s): midpoint → %s", sorted_collection, item, midpoint, extra={"event.action": "upper_bound", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
            current_item = sorted_collection[midpoint]
            if current_item <= item:
                left = midpoint + 1
            else:
                right = midpoint
        logger.warning("<<< Exiting upper_bound(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "upper_bound", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
        return left

    left = lower_bound(sorted_collection, item)
    right = upper_bound(sorted_collection, item)

    if left == len(sorted_collection) or sorted_collection[left] != item:
        return []
    return list(range(left, right))


def binary_search_by_recursion(
    sorted_collection: list[int], item: int, left: int = 0, right: int = -1
) -> int:
    """Pure implementation of a binary search algorithm in Python by recursion

    Be careful collection must be ascending sorted otherwise, the result will be
    unpredictable
    First recursion should be started with left=0 and right=(len(sorted_collection)-1)

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of the found item or -1 if the item is not found

    Examples:
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 0, 0, 4)
    0
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 15, 0, 4)
    4
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 5, 0, 4)
    1
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 6, 0, 4)
    -1
    """
    if right < 0:
        right = len(sorted_collection) - 1
    if list(sorted_collection) != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
    if right < left:
        return -1

    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(sorted_collection, item, left, midpoint - 1)
    else:
        logger.warning("<<< Exiting binary_search_by_recursion(sorted_collection=%s,item=%s,left=%s,right=%s)", sorted_collection, item, left, right, extra={"event.action": "binary_search_by_recursion", "logrite.sorted_collection": sorted_collection, "logrite.item": item, "logrite.left": left, "logrite.right": right})
        return binary_search_by_recursion(sorted_collection, item, midpoint + 1, right)


def exponential_search(sorted_collection: list[int], item: int) -> int:
    """Pure implementation of an exponential search algorithm in Python
    Resources used:
    https://en.wikipedia.org/wiki/Exponential_search

    Be careful collection must be ascending sorted otherwise, result will be
    unpredictable

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of the found item or -1 if the item is not found

    the order of this algorithm is O(lg I) where I is index position of item if exist

    Examples:
    >>> exponential_search([0, 5, 7, 10, 15], 0)
    0
    >>> exponential_search([0, 5, 7, 10, 15], 15)
    4
    >>> exponential_search([0, 5, 7, 10, 15], 5)
    1
    >>> exponential_search([0, 5, 7, 10, 15], 6)
    -1
    """
    logger.error(">>> Entering exponential_search(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "exponential_search", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
    if list(sorted_collection) != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
    bound = 1
    while bound < len(sorted_collection) and sorted_collection[bound] < item:
        bound *= 2
    left = bound // 2
    right = min(bound, len(sorted_collection) - 1)
    logger.error("exponential_search(sorted_collection=%s,item=%s): right → %s", sorted_collection, item, right, extra={"event.action": "exponential_search", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
    last_result = binary_search_by_recursion(
        sorted_collection=sorted_collection, item=item, left=left, right=right
    )
    logger.error("exponential_search(sorted_collection=%s,item=%s): last_result → %s", sorted_collection, item, last_result, extra={"event.action": "exponential_search", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
    if last_result is None:
        return -1
    logger.warning("<<< Exiting exponential_search(sorted_collection=%s,item=%s)", sorted_collection, item, extra={"event.action": "exponential_search", "logrite.sorted_collection": sorted_collection, "logrite.item": item})
    return last_result


searches = (  # Fastest to slowest...
    binary_search_std_lib,
    binary_search,
    exponential_search,
    binary_search_by_recursion,
)


if __name__ == "__main__":
    import doctest
    import timeit

    doctest.testmod()
    for search in searches:
        name = f"{search.__name__:>26}"
        print(f"{name}: {search([0, 5, 7, 10, 15], 10) = }")  # type: ignore[operator]

    print("\nBenchmarks...")
    setup = "collection = range(1000)"
    for search in searches:
        name = search.__name__
        print(
            f"{name:>26}:",
            timeit.timeit(
                f"{name}(collection, 500)", setup=setup, number=5_000, globals=globals()
            ),
        )

    user_input = input("\nEnter numbers separated by comma: ").strip()
    collection = sorted(int(item) for item in user_input.split(","))
    target = int(input("Enter a single number to be found in the list: "))
    result = binary_search(sorted_collection=collection, item=target)
    if result == -1:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at position {result} of {collection}.")
