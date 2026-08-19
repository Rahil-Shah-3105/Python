import logging
logger = logging.getLogger(__name__)
"""
Problem 15: https://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
"""


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
    logger.debug(">>> Entering solution(n=%s)", n)

    counts = [[1 for _ in range(n + 1)] for _ in range(n + 1)]
    logger.debug("solution(n=%s): counts → %s", n, counts)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            counts[i][j] = counts[i - 1][j] + counts[i][j - 1]

    logger.debug("<<< Exiting solution(n=%s)", n)
    return counts[n][n]


if __name__ == "__main__":
    print(solution())
