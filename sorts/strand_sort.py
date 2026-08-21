import operator
import logging
logger = logging.getLogger(__name__)


def strand_sort(arr: list, reverse: bool = False, solution: list | None = None) -> list:
    """
    Strand sort implementation
    source: https://en.wikipedia.org/wiki/Strand_sort

    :param arr: Unordered input list
    :param reverse: Descent ordering flag
    :param solution: Ordered items container

    Examples:
    >>> strand_sort([4, 2, 5, 3, 0, 1])
    [0, 1, 2, 3, 4, 5]

    >>> strand_sort([4, 2, 5, 3, 0, 1], reverse=True)
    [5, 4, 3, 2, 1, 0]
    """
    logger.debug(">>> Entering strand_sort(arr=%s,reverse=%s,solution=%s)", arr, reverse, solution)
    _operator = operator.lt if reverse else operator.gt
    logger.debug("strand_sort(arr=%s,reverse=%s,solution=%s): _operator → %s", arr, reverse, solution, _operator)
    solution = solution or []

    if not arr:
        return solution

    sublist = [arr.pop(0)]
    logger.debug("strand_sort(arr=%s,reverse=%s,solution=%s): sublist → %s", arr, reverse, solution, sublist)
    for i, item in enumerate(arr):
        if _operator(item, sublist[-1]):
            sublist.append(item)
            arr.pop(i)

    #  merging sublist into solution list
    if not solution:
        solution.extend(sublist)
    else:
        while sublist:
            item = sublist.pop(0)
            logger.debug("strand_sort(arr=%s,reverse=%s,solution=%s): item → %s", arr, reverse, solution, item)
            for i, xx in enumerate(solution):
                if not _operator(item, xx):
                    solution.insert(i, item)
                    break
            else:
                solution.append(item)

    strand_sort(arr, reverse, solution)
    logger.debug("<<< Exiting strand_sort(arr=%s,reverse=%s,solution=%s)", arr, reverse, solution)
    return solution


if __name__ == "__main__":
    assert strand_sort([4, 3, 5, 1, 2]) == [1, 2, 3, 4, 5]
    assert strand_sort([4, 3, 5, 1, 2], reverse=True) == [5, 4, 3, 2, 1]
