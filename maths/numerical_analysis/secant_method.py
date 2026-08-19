"""
Implementing Secant method in Python
Author: dimgrichr
"""

from math import exp
import logging
logger = logging.getLogger(__name__)


def f(x: float) -> float:
    """
    >>> f(5)
    39.98652410600183
    """
    logger.debug(">>> Entering f(x=%s)", x)
    logger.debug("<<< Exiting f(x=%s)", x)
    return 8 * x - 2 * exp(-x)


def secant_method(lower_bound: float, upper_bound: float, repeats: int) -> float:
    """
    >>> secant_method(1, 3, 2)
    0.2139409276214589
    """
    logger.debug(">>> Entering secant_method(lower_bound=%s,upper_bound=%s,repeats=%s)", lower_bound, upper_bound, repeats)
    x0 = lower_bound
    x1 = upper_bound
    for _ in range(repeats):
        x0, x1 = x1, x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    logger.debug("<<< Exiting secant_method(lower_bound=%s,upper_bound=%s,repeats=%s)", lower_bound, upper_bound, repeats)
    return x1


if __name__ == "__main__":
    print(f"Example: {secant_method(1, 3, 2)}")
