import logging
logger = logging.getLogger(__name__)
def search(list_data: list, key: int, left: int = 0, right: int = 0) -> int:
    """
    Iterate through the array to find the index of key using recursion.
    :param list_data: the list to be searched
    :param key: the key to be searched
    :param left: the index of first element
    :param right: the index of last element
    :return: the index of key value if found, -1 otherwise.

    >>> search(list(range(0, 11)), 5)
    5
    >>> search([1, 2, 4, 5, 3], 4)
    2
    >>> search([1, 2, 4, 5, 3], 6)
    -1
    >>> search([5], 5)
    0
    >>> search([], 1)
    -1
    """
    logger.error(">>> Entering search(list_data=%s,key=%s,left=%s,right=%s)", list_data, key, left, right, extra={"event.action": "search", "logrite.list_data": list_data, "logrite.key": key, "logrite.left": left, "logrite.right": right})
    right = right or len(list_data) - 1
    logger.error("search(list_data=%s,key=%s,left=%s,right=%s): right → %s", list_data, key, left, right, right, extra={"event.action": "search", "logrite.list_data": list_data, "logrite.key": key, "logrite.left": left, "logrite.right": right})
    if left > right:
        return -1
    elif list_data[left] == key:
        return left
    elif list_data[right] == key:
        return right
    else:
        logger.warning("<<< Exiting search(list_data=%s,key=%s,left=%s,right=%s)", list_data, key, left, right, extra={"event.action": "search", "logrite.list_data": list_data, "logrite.key": key, "logrite.left": left, "logrite.right": right})
        return search(list_data, key, left + 1, right - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
