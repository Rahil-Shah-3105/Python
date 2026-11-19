"""
Problem Statement:
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.
"""

import os
import logging
logger = logging.getLogger(__name__)


def solution() -> int:
    """
    Finds the maximum total in a triangle as described by the problem statement
    above.
    >>> solution()
    7273
    """
    logger.error(">>> Entering solution()", extra={"event.action": "solution"})
    script_dir = os.path.dirname(os.path.realpath(__file__))
    logger.error("solution(): script_dir → %s", script_dir, extra={"event.action": "solution"})
    triangle_path = os.path.join(script_dir, "triangle.txt")
    logger.error("solution(): triangle_path → %s", triangle_path, extra={"event.action": "solution"})

    with open(triangle_path) as in_file:
        triangle = [[int(i) for i in line.split()] for line in in_file]
        logger.error("solution(): triangle → %s", triangle, extra={"event.action": "solution"})

    while len(triangle) != 1:
        last_row = triangle.pop()
        logger.error("solution(): last_row → %s", last_row, extra={"event.action": "solution"})
        curr_row = triangle[-1]
        for j in range(len(last_row) - 1):
            curr_row[j] += max(last_row[j], last_row[j + 1])
    logger.warning("<<< Exiting solution()", extra={"event.action": "solution"})
    return triangle[0][0]


if __name__ == "__main__":
    print(solution())
