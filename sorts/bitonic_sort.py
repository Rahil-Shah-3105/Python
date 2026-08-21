"""
Python program for Bitonic Sort.

Note that this program works only when size of input is a power of 2.
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def comp_and_swap(array: list[int], index1: int, index2: int, direction: int) -> None:
    """Compare the value at given index1 and index2 of the array and swap them as per
    the given direction.

    The parameter direction indicates the sorting direction, ASCENDING(1) or
    DESCENDING(0); if (a[i] > a[j]) agrees with the direction, then a[i] and a[j] are
    interchanged.

    >>> arr = [12, 42, -21, 1]
    >>> comp_and_swap(arr, 1, 2, 1)
    >>> arr
    [12, -21, 42, 1]

    >>> comp_and_swap(arr, 1, 2, 0)
    >>> arr
    [12, 42, -21, 1]

    >>> comp_and_swap(arr, 0, 3, 1)
    >>> arr
    [1, 42, -21, 12]

    >>> comp_and_swap(arr, 0, 3, 0)
    >>> arr
    [12, 42, -21, 1]
    """
    logger.debug(">>> Entering comp_and_swap(array=%s,index1=%s,index2=%s,direction=%s)", array, index1, index2, direction)
    if (direction == 1 and array[index1] > array[index2]) or (
        direction == 0 and array[index1] < array[index2]
    ):
        array[index1], array[index2] = array[index2], array[index1]
        logger.debug("<<< Exiting comp_and_swap(array=%s,index1=%s,index2=%s,direction=%s)", array, index1, index2, direction)


def bitonic_merge(array: list[int], low: int, length: int, direction: int) -> None:
    """
    It recursively sorts a bitonic sequence in ascending order, if direction = 1, and in
    descending if direction = 0.
    The sequence to be sorted starts at index position low, the parameter length is the
    number of elements to be sorted.

    >>> arr = [12, 42, -21, 1]
    >>> bitonic_merge(arr, 0, 4, 1)
    >>> arr
    [-21, 1, 12, 42]

    >>> bitonic_merge(arr, 0, 4, 0)
    >>> arr
    [42, 12, 1, -21]
    """
    logger.debug(">>> Entering bitonic_merge(array=%s,low=%s,length=%s,direction=%s)", array, low, length, direction)
    if length > 1:
        middle = int(length / 2)
        logger.debug("bitonic_merge(array=%s,low=%s,length=%s,direction=%s): middle → %s", array, low, length, direction, middle)
        for i in range(low, low + middle):
            comp_and_swap(array, i, i + middle, direction)
        bitonic_merge(array, low, middle, direction)
        bitonic_merge(array, low + middle, middle, direction)
        logger.debug("<<< Exiting bitonic_merge(array=%s,low=%s,length=%s,direction=%s)", array, low, length, direction)


def bitonic_sort(array: list[int], low: int, length: int, direction: int) -> None:
    """
    This function first produces a bitonic sequence by recursively sorting its two
    halves in opposite sorting orders, and then calls bitonic_merge to make them in the
    same order.

    >>> arr = [12, 34, 92, -23, 0, -121, -167, 145]
    >>> bitonic_sort(arr, 0, 8, 1)
    >>> arr
    [-167, -121, -23, 0, 12, 34, 92, 145]

    >>> bitonic_sort(arr, 0, 8, 0)
    >>> arr
    [145, 92, 34, 12, 0, -23, -121, -167]
    """
    logger.debug(">>> Entering bitonic_sort(array=%s,low=%s,length=%s,direction=%s)", array, low, length, direction)
    if length > 1:
        middle = int(length / 2)
        logger.debug("bitonic_sort(array=%s,low=%s,length=%s,direction=%s): middle → %s", array, low, length, direction, middle)
        bitonic_sort(array, low, middle, 1)
        bitonic_sort(array, low + middle, middle, 0)
        bitonic_merge(array, low, length, direction)
        logger.debug("<<< Exiting bitonic_sort(array=%s,low=%s,length=%s,direction=%s)", array, low, length, direction)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item.strip()) for item in user_input.split(",")]

    bitonic_sort(unsorted, 0, len(unsorted), 1)
    print("\nSorted array in ascending order is: ", end="")
    print(*unsorted, sep=", ")

    bitonic_merge(unsorted, 0, len(unsorted), 0)
    print("Sorted array in descending order is: ", end="")
    print(*unsorted, sep=", ")
