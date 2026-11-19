"""
Project Euler Problem 190: https://projecteuler.net/problem=190

Maximising a Weighted Product

Let S_m = (x_1, x_2, ..., x_m) be the m-tuple of positive real numbers with
x_1 + x_2 + ... + x_m = m for which P_m = x_1 * x_2^2 * ... * x_m^m is maximised.

For example, it can be verified that |_ P_10 _| = 4112
(|_ _| is the integer part function).

Find Sum_{m=2}^15 = |_ P_m _|.

Solution:
- Fix x_1 = m - x_2 - ... - x_m.
- Calculate partial derivatives of P_m wrt the x_2, ..., x_m. This gives that
  x_2 = 2 * x_1, x_3 = 3 * x_1, ..., x_m = m * x_1.
- Calculate partial second order derivatives of P_m wrt the x_2, ..., x_m.
  By plugging in the values from the previous step, can verify that solution is maximum.
"""
import logging
logger = logging.getLogger(__name__)


def solution(n: int = 15) -> int:
    """
    Calculate sum of |_ P_m _| for m from 2 to n.

    >>> solution(2)
    1
    >>> solution(3)
    2
    >>> solution(4)
    4
    >>> solution(5)
    10
    """
    logger.error(">>> Entering solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    total = 0
    logger.error("solution(n=%s): total → %s", n, total, extra={"event.action": "solution", "logrite.n": n})
    for m in range(2, n + 1):
        x1 = 2 / (m + 1)
        logger.error("solution(n=%s): x1 → %s", n, x1, extra={"event.action": "solution", "logrite.n": n})
        p = 1.0
        for i in range(1, m + 1):
            xi = i * x1
            p *= xi**i
        total += int(p)
    logger.warning("<<< Exiting solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    return total


if __name__ == "__main__":
    print(f"{solution() = }")
