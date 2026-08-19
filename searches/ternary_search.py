"""
This is a type of divide and conquer algorithm which divides the search space into
3 parts and finds the target value based on the property of the array or list
(usually monotonic property).

Time Complexity  : O(log3 N)
Space Complexity : O(1)
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)

# This is the precision for this function which can be altered.
# It is recommended for users to keep this number greater than or equal to 10.
precision = 10


# This is the linear search that will occur after the search space has become smaller.


def lin_search(left: int, right: int, array: list[int], target: int) -> int:
    """Perform linear search in list. Returns -1 if element is not found.

    Parameters
    ----------
    left : int
        left index bound.
    right : int
        right index bound.
    array : List[int]
        List of elements to be searched on
    target : int
        Element that is searched

    Returns
    -------
    int
        index of element that is looked for.

    Examples
    --------
    >>> lin_search(0, 4, [4, 5, 6, 7], 7)
    3
    >>> lin_search(0, 3, [4, 5, 6, 7], 7)
    -1
    >>> lin_search(0, 2, [-18, 2], -18)
    0
    >>> lin_search(0, 1, [5], 5)
    0
    >>> lin_search(0, 3, ['a', 'c', 'd'], 'c')
    1
    >>> lin_search(0, 3, [.1, .4 , -.1], .1)
    0
    >>> lin_search(0, 3, [.1, .4 , -.1], -.1)
    2
    """
    logger.debug(">>> Entering lin_search(left=%s,right=%s,array=%s,target=%s)", left, right, array, target)
    for i in range(left, right):
        if array[i] == target:
            return i
    logger.debug("<<< Exiting lin_search(left=%s,right=%s,array=%s,target=%s)", left, right, array, target)
    return -1


def ite_ternary_search(array: list[int], target: int) -> int:
    """Iterative method of the ternary search algorithm.
    >>> test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    >>> ite_ternary_search(test_list, 3)
    -1
    >>> ite_ternary_search(test_list, 13)
    4
    >>> ite_ternary_search([4, 5, 6, 7], 4)
    0
    >>> ite_ternary_search([4, 5, 6, 7], -10)
    -1
    >>> ite_ternary_search([-18, 2], -18)
    0
    >>> ite_ternary_search([5], 5)
    0
    >>> ite_ternary_search(['a', 'c', 'd'], 'c')
    1
    >>> ite_ternary_search(['a', 'c', 'd'], 'f')
    -1
    >>> ite_ternary_search([], 1)
    -1
    >>> ite_ternary_search([.1, .4 , -.1], .1)
    0
    """
    logger.debug(">>> Entering ite_ternary_search(array=%s,target=%s)", array, target)

    left = 0
    logger.debug("ite_ternary_search(array=%s,target=%s): left → %s", array, target, left)
    right = len(array)
    logger.debug("ite_ternary_search(array=%s,target=%s): right → %s", array, target, right)
    while left <= right:
        if right - left < precision:
            return lin_search(left, right, array, target)

        one_third = (left + right) // 3 + 1
        logger.debug("ite_ternary_search(array=%s,target=%s): one_third → %s", array, target, one_third)
        two_third = 2 * (left + right) // 3 + 1
        logger.debug("ite_ternary_search(array=%s,target=%s): two_third → %s", array, target, two_third)

        if array[one_third] == target:
            return one_third
        elif array[two_third] == target:
            return two_third

        elif target < array[one_third]:
            right = one_third - 1
        elif array[two_third] < target:
            left = two_third + 1

        else:
            left = one_third + 1
            right = two_third - 1
    logger.debug("<<< Exiting ite_ternary_search(array=%s,target=%s)", array, target)
    return -1


def rec_ternary_search(left: int, right: int, array: list[int], target: int) -> int:
    """Recursive method of the ternary search algorithm.

    >>> test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    >>> rec_ternary_search(0, len(test_list), test_list, 3)
    -1
    >>> rec_ternary_search(4, len(test_list), test_list, 42)
    8
    >>> rec_ternary_search(0, 2, [4, 5, 6, 7], 4)
    0
    >>> rec_ternary_search(0, 3, [4, 5, 6, 7], -10)
    -1
    >>> rec_ternary_search(0, 1, [-18, 2], -18)
    0
    >>> rec_ternary_search(0, 1, [5], 5)
    0
    >>> rec_ternary_search(0, 2, ['a', 'c', 'd'], 'c')
    1
    >>> rec_ternary_search(0, 2, ['a', 'c', 'd'], 'f')
    -1
    >>> rec_ternary_search(0, 0, [], 1)
    -1
    >>> rec_ternary_search(0, 3, [.1, .4 , -.1], .1)
    0
    """
    logger.debug(">>> Entering rec_ternary_search(left=%s,right=%s,array=%s,target=%s)", left, right, array, target)
    if left < right:
        if right - left < precision:
            return lin_search(left, right, array, target)
        one_third = (left + right) // 3 + 1
        logger.debug("rec_ternary_search(left=%s,right=%s,array=%s,target=%s): one_third → %s", left, right, array, target, one_third)
        two_third = 2 * (left + right) // 3 + 1
        logger.debug("rec_ternary_search(left=%s,right=%s,array=%s,target=%s): two_third → %s", left, right, array, target, two_third)

        if array[one_third] == target:
            return one_third
        elif array[two_third] == target:
            return two_third

        elif target < array[one_third]:
            return rec_ternary_search(left, one_third - 1, array, target)
        elif array[two_third] < target:
            return rec_ternary_search(two_third + 1, right, array, target)
        else:
            return rec_ternary_search(one_third + 1, two_third - 1, array, target)
    else:
        logger.debug("<<< Exiting rec_ternary_search(left=%s,right=%s,array=%s,target=%s)", left, right, array, target)
        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by comma:\n").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]
    assert collection == sorted(collection), f"List must be ordered.\n{collection}."
    target = int(input("Enter the number to be found in the list:\n").strip())
    result1 = ite_ternary_search(collection, target)
    result2 = rec_ternary_search(0, len(collection) - 1, collection, target)
    if result2 != -1:
        print(f"Iterative search: {target} found at positions: {result1}")
        print(f"Recursive search: {target} found at positions: {result2}")
    else:
        print("Not found")
