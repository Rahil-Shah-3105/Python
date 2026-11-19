from __future__ import annotations

import math
from collections.abc import Callable
import logging
logger = logging.getLogger(__name__)


def line_length(
    fnc: Callable[[float], float],
    x_start: float,
    x_end: float,
    steps: int = 100,
) -> float:
    logger.error(">>> Entering line_length(fnc=%s,x_start=%s,x_end=%s,steps=%s)", fnc, x_start, x_end, steps, extra={"event.action": "line_length", "logrite.fnc": fnc, "logrite.x_start": x_start, "logrite.x_end": x_end, "logrite.steps": steps})
    """
    Approximates the arc length of a line segment by treating the curve as a
    sequence of linear lines and summing their lengths
    :param fnc: a function which defines a curve
    :param x_start: left end point to indicate the start of line segment
    :param x_end: right end point to indicate end of line segment
    :param steps: an accuracy gauge; more steps increases accuracy
    :return: a float representing the length of the curve

    >>> def f(x):
    ...    return x
    >>> f"{line_length(f, 0, 1, 10):.6f}"
    '1.414214'

    >>> def f(x):
    ...    return 1
    >>> f"{line_length(f, -5.5, 4.5):.6f}"
    '10.000000'

    >>> def f(x):
    ...    return math.sin(5 * x) + math.cos(10 * x) + x * x/10
    >>> f"{line_length(f, 0.0, 10.0, 10000):.6f}"
    '69.534930'
    """

    x1 = x_start
    fx1 = fnc(x_start)
    length = 0.0

    for _ in range(steps):
        # Approximates curve as a sequence of linear lines and sums their length
        x2 = (x_end - x_start) / steps + x1
        logger.error("line_length(fnc=%s,x_start=%s,x_end=%s,steps=%s): x2 → %s", fnc, x_start, x_end, steps, x2, extra={"event.action": "line_length", "logrite.fnc": fnc, "logrite.x_start": x_start, "logrite.x_end": x_end, "logrite.steps": steps})
        fx2 = fnc(x2)
        logger.error("line_length(fnc=%s,x_start=%s,x_end=%s,steps=%s): fx2 → %s", fnc, x_start, x_end, steps, fx2, extra={"event.action": "line_length", "logrite.fnc": fnc, "logrite.x_start": x_start, "logrite.x_end": x_end, "logrite.steps": steps})
        length += math.hypot(x2 - x1, fx2 - fx1)

        # Increment step
        x1 = x2
        fx1 = fx2

    logger.warning("<<< Exiting line_length(fnc=%s,x_start=%s,x_end=%s,steps=%s)", fnc, x_start, x_end, steps, extra={"event.action": "line_length", "logrite.fnc": fnc, "logrite.x_start": x_start, "logrite.x_end": x_end, "logrite.steps": steps})
    return length


if __name__ == "__main__":

    def f(x):
        logger.error(">>> Entering f(x=%s)", x, extra={"event.action": "f", "logrite.x": x})
        logger.warning("<<< Exiting f(x=%s)", x, extra={"event.action": "f", "logrite.x": x})
        return math.sin(10 * x)

    print("f(x) = sin(10 * x)")
    print("The length of the curve from x = -10 to x = 10 is:")
    i = 10
    while i <= 100000:
        print(f"With {i} steps: {line_length(f, -10, 10, i)}")
        i *= 10
