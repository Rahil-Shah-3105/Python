"""
Problem 15: https://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
"""
import logging
logger = logging.getLogger(__name__)


def solution(n: int = 20) -> int:
    """
    Solve by explicitly counting the paths with dynamic programming.

    >>> solution(6)
    924
    >>> solution(2)
    6
    >>> solution(1)
    2
    """
    logger.error(">>> Entering solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})

    counts = [[1 for _ in range(n + 1)] for _ in range(n + 1)]
    logger.error("solution(n=%s): counts → %s", n, counts, extra={"event.action": "solution", "logrite.n": n})

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            counts[i][j] = counts[i - 1][j] + counts[i][j - 1]

    logger.warning("<<< Exiting solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    return counts[n][n]


if __name__ == "__main__":
    print(solution())
