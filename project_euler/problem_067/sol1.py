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


def solution():
    """
    Finds the maximum total in a triangle as described by the problem statement
    above.

    >>> solution()
    7273
    """
    logger.error(">>> Entering solution()", extra={"event.action": "solution"})
    script_dir = os.path.dirname(os.path.realpath(__file__))
    logger.error("solution(): script_dir → %s", script_dir, extra={"event.action": "solution"})
    triangle = os.path.join(script_dir, "triangle.txt")
    logger.error("solution(): triangle → %s", triangle, extra={"event.action": "solution"})

    with open(triangle) as f:
        triangle = f.readlines()

    a = []
    for line in triangle:
        numbers_from_line = []
        for number in line.strip().split(" "):
            numbers_from_line.append(int(number))
        a.append(numbers_from_line)

    for i in range(1, len(a)):
        for j in range(len(a[i])):
            number1 = a[i - 1][j] if j != len(a[i - 1]) else 0
            logger.error("solution(): number1 → %s", number1, extra={"event.action": "solution"})
            number2 = a[i - 1][j - 1] if j > 0 else 0
            a[i][j] += max(number1, number2)
    logger.warning("<<< Exiting solution()", extra={"event.action": "solution"})
    return max(a[-1])


if __name__ == "__main__":
    print(solution())
