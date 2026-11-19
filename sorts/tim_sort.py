from typing import Any
import logging
logger = logging.getLogger(__name__)


def binary_search(lst: list[Any], item: Any, start: int, end: int) -> int:
    logger.error(">>> Entering binary_search(lst=%s,item=%s,start=%s,end=%s)", lst, item, start, end, extra={"event.action": "binary_search", "logrite.lst": lst, "logrite.item": item, "logrite.start": start, "logrite.end": end})
    if start == end:
        return start if lst[start] > item else start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if lst[mid] < item:
        return binary_search(lst, item, mid + 1, end)
    elif lst[mid] > item:
        return binary_search(lst, item, start, mid - 1)
    else:
        logger.warning("<<< Exiting binary_search(lst=%s,item=%s,start=%s,end=%s)", lst, item, start, end, extra={"event.action": "binary_search", "logrite.lst": lst, "logrite.item": item, "logrite.start": start, "logrite.end": end})
        return mid


def insertion_sort(lst: list[Any]) -> list[Any]:
    logger.error(">>> Entering insertion_sort(lst=%s)", lst, extra={"event.action": "insertion_sort", "logrite.lst": lst})
    length = len(lst)
    logger.error("insertion_sort(lst=%s): length → %s", lst, length, extra={"event.action": "insertion_sort", "logrite.lst": lst})

    for index in range(1, length):
        value = lst[index]
        pos = binary_search(lst, value, 0, index - 1)
        logger.error("insertion_sort(lst=%s): pos → %s", lst, pos, extra={"event.action": "insertion_sort", "logrite.lst": lst})
        lst = [*lst[:pos], value, *lst[pos:index], *lst[index + 1 :]]

    logger.warning("<<< Exiting insertion_sort(lst=%s)", lst, extra={"event.action": "insertion_sort", "logrite.lst": lst})
    return lst


def merge(left: list[Any], right: list[Any]) -> list[Any]:
    logger.error(">>> Entering merge(left=%s,right=%s)", left, right, extra={"event.action": "merge", "logrite.left": left, "logrite.right": right})
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0], *merge(left[1:], right)]

    logger.warning("<<< Exiting merge(left=%s,right=%s)", left, right, extra={"event.action": "merge", "logrite.left": left, "logrite.right": right})
    return [right[0], *merge(left, right[1:])]


def tim_sort(lst: list[Any] | tuple[Any, ...] | str) -> list[Any]:
    """
    >>> tim_sort("Python")
    ['P', 'h', 'n', 'o', 't', 'y']
    >>> tim_sort((1.1, 1, 0, -1, -1.1))
    [-1.1, -1, 0, 1, 1.1]
    >>> tim_sort(list(reversed(list(range(7)))))
    [0, 1, 2, 3, 4, 5, 6]
    >>> tim_sort([3, 2, 1]) == insertion_sort([3, 2, 1])
    True
    >>> tim_sort([3, 2, 1]) == sorted([3, 2, 1])
    True
    """
    logger.error(">>> Entering tim_sort(lst=%s)", lst, extra={"event.action": "tim_sort", "logrite.lst": lst})
    length = len(lst)
    logger.error("tim_sort(lst=%s): length → %s", lst, length, extra={"event.action": "tim_sort", "logrite.lst": lst})
    runs, sorted_runs = [], []
    new_run = [lst[0]]
    sorted_array: list[Any] = []
    logger.error("tim_sort(lst=%s): sorted_array → %s", lst, sorted_array, extra={"event.action": "tim_sort", "logrite.lst": lst})
    i = 1
    while i < length:
        if lst[i] < lst[i - 1]:
            runs.append(new_run)
            new_run = [lst[i]]
        else:
            new_run.append(lst[i])
        i += 1
    runs.append(new_run)

    for run in runs:
        sorted_runs.append(insertion_sort(run))
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    logger.warning("<<< Exiting tim_sort(lst=%s)", lst, extra={"event.action": "tim_sort", "logrite.lst": lst})
    return sorted_array


def main():
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    lst = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
    sorted_lst = tim_sort(lst)
    logger.error("main(): sorted_lst → %s", sorted_lst, extra={"event.action": "main"})
    print(sorted_lst)
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
