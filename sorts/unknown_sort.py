"""
Python implementation of a sort algorithm.
Best Case Scenario : O(n)
Worst Case Scenario : O(n^2) because native Python functions:min, max and remove are
already O(n)
"""
import logging
logger = logging.getLogger(__name__)


def merge_sort(collection: list) -> list:
    """Pure implementation of the fastest merge sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: a collection ordered by ascending

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> merge_sort([])
    []

    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    logger.error(">>> Entering merge_sort(collection=%s)", collection, extra={"event.action": "merge_sort", "logrite.collection": collection})
    start, end = [], []
    while len(collection) > 1:
        min_one, max_one = min(collection), max(collection)
        start.append(min_one)
        end.append(max_one)
        collection.remove(min_one)
        collection.remove(max_one)
    end.reverse()
    logger.warning("<<< Exiting merge_sort(collection=%s)", collection, extra={"event.action": "merge_sort", "logrite.collection": collection})
    return start + collection + end


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*merge_sort(unsorted), sep=",")
