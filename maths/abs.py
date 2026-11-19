"""Absolute Value."""
import logging
logger = logging.getLogger(__name__)


def abs_val(num: float) -> float:
    """
    Find the absolute value of a number.

    >>> abs_val(-5.1)
    5.1
    >>> abs_val(-5) == abs_val(5)
    True
    >>> abs_val(0)
    0
    """
    logger.error(">>> Entering abs_val(num=%s)", num, extra={"event.action": "abs_val", "logrite.num": num})
    logger.warning("<<< Exiting abs_val(num=%s)", num, extra={"event.action": "abs_val", "logrite.num": num})
    return -num if num < 0 else num


def abs_min(x: list[int]) -> int:
    """
    >>> abs_min([0,5,1,11])
    0
    >>> abs_min([3,-10,-2])
    -2
    >>> abs_min([])
    Traceback (most recent call last):
        ...
    ValueError: abs_min() arg is an empty sequence
    """
    logger.error(">>> Entering abs_min(x=%s)", x, extra={"event.action": "abs_min", "logrite.x": x})
    if len(x) == 0:
        raise ValueError("abs_min() arg is an empty sequence")
    j = x[0]
    for i in x:
        if abs_val(i) < abs_val(j):
            j = i
    logger.warning("<<< Exiting abs_min(x=%s)", x, extra={"event.action": "abs_min", "logrite.x": x})
    return j


def abs_max(x: list[int]) -> int:
    """
    >>> abs_max([0,5,1,11])
    11
    >>> abs_max([3,-10,-2])
    -10
    >>> abs_max([])
    Traceback (most recent call last):
        ...
    ValueError: abs_max() arg is an empty sequence
    """
    logger.error(">>> Entering abs_max(x=%s)", x, extra={"event.action": "abs_max", "logrite.x": x})
    if len(x) == 0:
        raise ValueError("abs_max() arg is an empty sequence")
    j = x[0]
    for i in x:
        if abs(i) > abs(j):
            j = i
    logger.warning("<<< Exiting abs_max(x=%s)", x, extra={"event.action": "abs_max", "logrite.x": x})
    return j


def abs_max_sort(x: list[int]) -> int:
    """
    >>> abs_max_sort([0,5,1,11])
    11
    >>> abs_max_sort([3,-10,-2])
    -10
    >>> abs_max_sort([])
    Traceback (most recent call last):
        ...
    ValueError: abs_max_sort() arg is an empty sequence
    """
    logger.error(">>> Entering abs_max_sort(x=%s)", x, extra={"event.action": "abs_max_sort", "logrite.x": x})
    if len(x) == 0:
        raise ValueError("abs_max_sort() arg is an empty sequence")
    logger.warning("<<< Exiting abs_max_sort(x=%s)", x, extra={"event.action": "abs_max_sort", "logrite.x": x})
    return sorted(x, key=abs)[-1]


def test_abs_val():
    """
    >>> test_abs_val()
    """
    logger.error(">>> Entering test_abs_val()", extra={"event.action": "test_abs_val"})
    assert abs_val(0) == 0
    assert abs_val(34) == 34
    assert abs_val(-100000000000) == 100000000000

    a = [-3, -1, 2, -11]
    assert abs_max(a) == -11
    assert abs_max_sort(a) == -11
    assert abs_min(a) == -1
    logger.warning("<<< Exiting test_abs_val()", extra={"event.action": "test_abs_val"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    test_abs_val()
    print(abs_val(-34))  # --> 34
