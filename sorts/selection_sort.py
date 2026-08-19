import logging
logger = logging.getLogger(__name__)
def selection_sort(collection: list[int]) -> list[int]:
    """
    Sorts a list in ascending order using the selection sort algorithm.

    :param collection: A list of integers to be sorted.
    :return: The sorted list.

    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> selection_sort([])
    []

    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    logger.debug(">>> Entering selection_sort(collection=%s)", collection)

    length = len(collection)
    logger.debug("selection_sort(collection=%s): length → %s", collection, length)
    for i in range(length - 1):
        min_index = i
        logger.debug("selection_sort(collection=%s): min_index → %s", collection, min_index)
        for k in range(i + 1, length):
            if collection[k] < collection[min_index]:
                min_index = k
        if min_index != i:
            collection[i], collection[min_index] = collection[min_index], collection[i]
    logger.debug("<<< Exiting selection_sort(collection=%s)", collection)
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    sorted_list = selection_sort(unsorted)
    print("Sorted List:", sorted_list)
