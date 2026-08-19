"""
This is an implementation of Pigeon Hole Sort.
For doctests run following command:

python3 -m doctest -v pigeon_sort.py
or
python -m doctest -v pigeon_sort.py

For manual testing run:
python pigeon_sort.py
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def pigeon_sort(array: list[int]) -> list[int]:
    """
    Implementation of pigeon hole sort algorithm
    :param array: Collection of comparable items
    :return: Collection sorted in ascending order
    >>> pigeon_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> pigeon_sort([])
    []
    >>> pigeon_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    logger.debug(">>> Entering pigeon_sort(array=%s)", array)
    if len(array) == 0:
        return array

    _min, _max = min(array), max(array)

    # Compute the variables
    holes_range = _max - _min + 1
    logger.debug("pigeon_sort(array=%s): holes_range → %s", array, holes_range)
    holes, holes_repeat = [0] * holes_range, [0] * holes_range

    # Make the sorting.
    for i in array:
        index = i - _min
        logger.debug("pigeon_sort(array=%s): index → %s", array, index)
        holes[index] = i
        holes_repeat[index] += 1

    # Makes the array back by replacing the numbers.
    index = 0
    for i in range(holes_range):
        while holes_repeat[i] > 0:
            array[index] = holes[i]
            index += 1
            holes_repeat[i] -= 1

    # Returns the sorted array.
    logger.debug("<<< Exiting pigeon_sort(array=%s)", array)
    return array


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by comma:\n")
    unsorted = [int(x) for x in user_input.split(",")]
    print(pigeon_sort(unsorted))
