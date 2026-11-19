import logging
logger = logging.getLogger(__name__)
def stooge_sort(arr: list[int]) -> list[int]:
    """
    Examples:
    >>> stooge_sort([18.1, 0, -7.1, -1, 2, 2])
    [-7.1, -1, 0, 2, 2, 18.1]

    >>> stooge_sort([])
    []
    """
    logger.error(">>> Entering stooge_sort(arr=%s)", arr, extra={"event.action": "stooge_sort", "logrite.arr": arr})
    stooge(arr, 0, len(arr) - 1)
    logger.warning("<<< Exiting stooge_sort(arr=%s)", arr, extra={"event.action": "stooge_sort", "logrite.arr": arr})
    return arr


def stooge(arr: list[int], i: int, h: int) -> None:
    logger.error(">>> Entering stooge(arr=%s,i=%s,h=%s)", arr, i, h, extra={"event.action": "stooge", "logrite.arr": arr, "logrite.i": i, "logrite.h": h})
    if i >= h:
        logger.warning("<<< Exiting stooge(arr=%s,i=%s,h=%s)", arr, i, h, extra={"event.action": "stooge", "logrite.arr": arr, "logrite.i": i, "logrite.h": h})
        return

    # If first element is smaller than the last then swap them
    if arr[i] > arr[h]:
        arr[i], arr[h] = arr[h], arr[i]

    # If there are more than 2 elements in the array
    if h - i + 1 > 2:
        t = (int)((h - i + 1) / 3)

        # Recursively sort first 2/3 elements
        stooge(arr, i, (h - t))

        # Recursively sort last 2/3 elements
        stooge(arr, i + t, (h))

        # Recursively sort first 2/3 elements
        stooge(arr, i, (h - t))


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(stooge_sort(unsorted))
