import logging
logger = logging.getLogger(__name__)
def quick_sort_3partition(sorting: list, left: int, right: int) -> None:
    """ "
    Python implementation of quick sort algorithm with 3-way partition.
    The idea of 3-way quick sort is based on "Dutch National Flag algorithm".

    :param sorting: sort list
    :param left: left endpoint of sorting
    :param right: right endpoint of sorting
    :return: None

    Examples:
    >>> array1 = [5, -1, -1, 5, 5, 24, 0]
    >>> quick_sort_3partition(array1, 0, 6)
    >>> array1
    [-1, -1, 0, 5, 5, 5, 24]
    >>> array2 = [9, 0, 2, 6]
    >>> quick_sort_3partition(array2, 0, 3)
    >>> array2
    [0, 2, 6, 9]
    >>> array3 = []
    >>> quick_sort_3partition(array3, 0, 0)
    >>> array3
    []
    """
    logger.debug(">>> Entering quick_sort_3partition(sorting=%s,left=%s,right=%s)", sorting, left, right)
    if right <= left:
        logger.debug("<<< Exiting quick_sort_3partition(sorting=%s,left=%s,right=%s)", sorting, left, right)
        return
    a = i = left
    b = right
    pivot = sorting[left]
    logger.debug("quick_sort_3partition(sorting=%s,left=%s,right=%s): pivot → %s", sorting, left, right, pivot)
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)


def quick_sort_lomuto_partition(sorting: list, left: int, right: int) -> None:
    """
    A pure Python implementation of quick sort algorithm(in-place)
    with Lomuto partition scheme:
    https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme

    :param sorting: sort list
    :param left: left endpoint of sorting
    :param right: right endpoint of sorting
    :return: None

    Examples:
    >>> nums1 = [0, 5, 3, 1, 2]
    >>> quick_sort_lomuto_partition(nums1, 0, 4)
    >>> nums1
    [0, 1, 2, 3, 5]
    >>> nums2 = []
    >>> quick_sort_lomuto_partition(nums2, 0, 0)
    >>> nums2
    []
    >>> nums3 = [-2, 5, 0, -4]
    >>> quick_sort_lomuto_partition(nums3, 0, 3)
    >>> nums3
    [-4, -2, 0, 5]
    """
    logger.debug(">>> Entering quick_sort_lomuto_partition(sorting=%s,left=%s,right=%s)", sorting, left, right)
    logger.debug("quick_sort_lomuto_partition(sorting=%s,left=%s,right=%s): pivot_index → %s", sorting, left, right, pivot_index)
    if left < right:
        logger.error("Exception in quick_sort_lomuto_partition(sorting=%s,left=%s,right=%s)", sorting, left, right, exc_info=True)
        pivot_index = lomuto_partition(sorting, left, right)
        quick_sort_lomuto_partition(sorting, left, pivot_index - 1)
        quick_sort_lomuto_partition(sorting, pivot_index + 1, right)
        logger.debug("<<< Exiting quick_sort_lomuto_partition(sorting=%s,left=%s,right=%s)", sorting, left, right)


def lomuto_partition(sorting: list, left: int, right: int) -> int:
    """
    Example:
    >>> lomuto_partition([1,5,7,6], 0, 3)
    2
    """
    logger.debug(">>> Entering lomuto_partition(sorting=%s,left=%s,right=%s)", sorting, left, right)
    pivot = sorting[right]
    logger.debug("lomuto_partition(sorting=%s,left=%s,right=%s): pivot → %s", sorting, left, right, pivot)
    store_index = left
    logger.debug("lomuto_partition(sorting=%s,left=%s,right=%s): store_index → %s", sorting, left, right, store_index)
    for i in range(left, right):
        if sorting[i] < pivot:
            sorting[store_index], sorting[i] = sorting[i], sorting[store_index]
            store_index += 1
    sorting[right], sorting[store_index] = sorting[store_index], sorting[right]
    logger.debug("<<< Exiting lomuto_partition(sorting=%s,left=%s,right=%s)", sorting, left, right)
    return store_index


def three_way_radix_quicksort(sorting: list) -> list:
    """
    Three-way radix quicksort:
    https://en.wikipedia.org/wiki/Quicksort#Three-way_radix_quicksort
    First divide the list into three parts.
    Then recursively sort the "less than" and "greater than" partitions.

    >>> three_way_radix_quicksort([])
    []
    >>> three_way_radix_quicksort([1])
    [1]
    >>> three_way_radix_quicksort([-5, -2, 1, -2, 0, 1])
    [-5, -2, -2, 0, 1, 1]
    >>> three_way_radix_quicksort([1, 2, 5, 1, 2, 0, 0, 5, 2, -1])
    [-1, 0, 0, 1, 1, 2, 2, 2, 5, 5]
    """
    logger.debug(">>> Entering three_way_radix_quicksort(sorting=%s)", sorting)
    if len(sorting) <= 1:
        logger.debug("<<< Exiting three_way_radix_quicksort(sorting=%s)", sorting)
        return sorting
    return (
        three_way_radix_quicksort([i for i in sorting if i < sorting[0]])
        + [i for i in sorting if i == sorting[0]]
        + three_way_radix_quicksort([i for i in sorting if i > sorting[0]])
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    quick_sort_3partition(unsorted, 0, len(unsorted) - 1)
    print(unsorted)
