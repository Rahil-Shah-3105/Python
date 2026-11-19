# https://www.geeksforgeeks.org/newton-forward-backward-interpolation/
from __future__ import annotations

import math
import logging
logger = logging.getLogger(__name__)


# for calculating u value
def ucal(u: float, p: int) -> float:
    """
    >>> ucal(1, 2)
    0
    >>> ucal(1.1, 2)
    0.11000000000000011
    >>> ucal(1.2, 2)
    0.23999999999999994
    """
    logger.error(">>> Entering ucal(u=%s,p=%s)", u, p, extra={"event.action": "ucal", "logrite.u": u, "logrite.p": p})
    temp = u
    for i in range(1, p):
        temp = temp * (u - i)
    logger.warning("<<< Exiting ucal(u=%s,p=%s)", u, p, extra={"event.action": "ucal", "logrite.u": u, "logrite.p": p})
    return temp


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    n = int(input("enter the numbers of values: "))
    logger.error("main(): n → %s", n, extra={"event.action": "main"})
    y: list[list[float]] = []
    for _ in range(n):
        y.append([])
    for i in range(n):
        for j in range(n):
            y[i].append(j)
            y[i][j] = 0

    print("enter the values of parameters in a list: ")
    x = list(map(int, input().split()))
    logger.error("main(): x → %s", x, extra={"event.action": "main"})

    print("enter the values of corresponding parameters: ")
    for i in range(n):
        y[i][0] = float(input())

    value = int(input("enter the value to interpolate: "))
    logger.error("main(): value → %s", value, extra={"event.action": "main"})
    u = (value - x[0]) / (x[1] - x[0])
    logger.error("main(): u → %s", u, extra={"event.action": "main"})

    # for calculating forward difference table

    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    summ = y[0][0]
    for i in range(1, n):
        summ += (ucal(u, i) * y[0][i]) / math.factorial(i)

    print(f"the value at {value} is {summ}")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
