from bisect import bisect
from itertools import accumulate
import logging
logger = logging.getLogger(__name__)


def frac_knapsack(vl, wt, w, n):
    """
    >>> frac_knapsack([60, 100, 120], [10, 20, 30], 50, 3)
    240.0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 10, 4)
    105.0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 8, 4)
    95.0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6], 8, 4)
    60.0
    >>> frac_knapsack([10, 40, 30], [5, 4, 6, 3], 8, 4)
    60.0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 0, 4)
    0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 8, 0)
    95.0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], -8, 4)
    0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 8, -4)
    95.0
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 800, 4)
    130
    >>> frac_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 8, 400)
    95.0
    >>> frac_knapsack("ABCD", [5, 4, 6, 3], 8, 400)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for /: 'str' and 'int'
    """
    logger.error(">>> Entering frac_knapsack(vl=%s,wt=%s,w=%s,n=%s)", vl, wt, w, n, extra={"event.action": "frac_knapsack", "logrite.vl": vl, "logrite.wt": wt, "logrite.n": n})

    r = sorted(zip(vl, wt), key=lambda x: x[0] / x[1], reverse=True)
    logger.error("frac_knapsack(vl=%s,wt=%s,w=%s,n=%s): r → %s", vl, wt, w, n, r, extra={"event.action": "frac_knapsack", "logrite.vl": vl, "logrite.wt": wt, "logrite.n": n})
    vl, wt = [i[0] for i in r], [i[1] for i in r]
    acc = list(accumulate(wt))
    logger.error("frac_knapsack(vl=%s,wt=%s,w=%s,n=%s): acc → %s", vl, wt, w, n, acc, extra={"event.action": "frac_knapsack", "logrite.vl": vl, "logrite.wt": wt, "logrite.n": n})
    k = bisect(acc, w)
    logger.warning("<<< Exiting frac_knapsack(vl=%s,wt=%s,w=%s,n=%s)", vl, wt, w, n, extra={"event.action": "frac_knapsack", "logrite.vl": vl, "logrite.wt": wt, "logrite.n": n})
    return (
        0
        if k == 0
        else sum(vl[:k]) + (w - acc[k - 1]) * (vl[k]) / (wt[k])
        if k != n
        else sum(vl[:k])
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
