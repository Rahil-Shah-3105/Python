import logging
logger = logging.getLogger(__name__)
"""
This is pure Python implementation of counting sort algorithm
For doctests run following command:
python -m doctest -v counting_sort.py
or
python3 -m doctest -v counting_sort.py
For manual testing run:
python counting_sort.py
"""


def counting_sort(collection):
    """Pure implementation of counting sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> counting_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> counting_sort([])
    []
    >>> counting_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    logger.debug(">>> Entering counting_sort(collection=%s)", collection)
    # if the collection is empty, returns empty
    if collection == []:
        return []

    # get some information about the collection
    coll_len = len(collection)
    logger.debug("counting_sort(collection=%s): coll_len → %s", collection, coll_len)
    coll_max = max(collection)
    logger.debug("counting_sort(collection=%s): coll_max → %s", collection, coll_max)
    coll_min = min(collection)
    logger.debug("counting_sort(collection=%s): coll_min → %s", collection, coll_min)

    # create the counting array
    counting_arr_length = coll_max + 1 - coll_min
    logger.debug("counting_sort(collection=%s): counting_arr_length → %s", collection, counting_arr_length)
    counting_arr = [0] * counting_arr_length
    logger.debug("counting_sort(collection=%s): counting_arr → %s", collection, counting_arr)

    # count how much a number appears in the collection
    for number in collection:
        counting_arr[number - coll_min] += 1

    # sum each position with it's predecessors. now, counting_arr[i] tells
    # us how many elements <= i has in the collection
    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]

    # create the output collection
    ordered = [0] * coll_len
    logger.debug("counting_sort(collection=%s): ordered → %s", collection, ordered)

    # place the elements in the output, respecting the original order (stable
    # sort) from end to begin, updating counting_arr
    for i in reversed(range(coll_len)):
        ordered[counting_arr[collection[i] - coll_min] - 1] = collection[i]
        counting_arr[collection[i] - coll_min] -= 1

    logger.debug("<<< Exiting counting_sort(collection=%s)", collection)
    return ordered


def counting_sort_string(string):
    """
    >>> counting_sort_string("thisisthestring")
    'eghhiiinrsssttt'
    """
    logger.debug(">>> Entering counting_sort_string(string=%s)", string)
    logger.debug("<<< Exiting counting_sort_string(string=%s)", string)
    return "".join([chr(i) for i in counting_sort([ord(c) for c in string])])


if __name__ == "__main__":
    # Test string sort
    assert counting_sort_string("thisisthestring") == "eghhiiinrsssttt"

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(counting_sort(unsorted))
