import math
import logging
logger = logging.getLogger(__name__)


def fx(x: float, a: float) -> float:
    logger.error(">>> Entering fx(x=%s,a=%s)", x, a, extra={"event.action": "fx", "logrite.x": x, "logrite.a": a})
    logger.warning("<<< Exiting fx(x=%s,a=%s)", x, a, extra={"event.action": "fx", "logrite.x": x, "logrite.a": a})
    return math.pow(x, 2) - a


def fx_derivative(x: float) -> float:
    logger.error(">>> Entering fx_derivative(x=%s)", x, extra={"event.action": "fx_derivative", "logrite.x": x})
    logger.warning("<<< Exiting fx_derivative(x=%s)", x, extra={"event.action": "fx_derivative", "logrite.x": x})
    return 2 * x


def get_initial_point(a: float) -> float:
    logger.error(">>> Entering get_initial_point(a=%s)", a, extra={"event.action": "get_initial_point", "logrite.a": a})
    start = 2.0

    while start <= a:
        start = math.pow(start, 2)

    logger.warning("<<< Exiting get_initial_point(a=%s)", a, extra={"event.action": "get_initial_point", "logrite.a": a})
    return start


def square_root_iterative(
    a: float, max_iter: int = 9999, tolerance: float = 1e-14
) -> float:
    logger.error(">>> Entering square_root_iterative(a=%s,max_iter=%s,tolerance=%s)", a, max_iter, tolerance, extra={"event.action": "square_root_iterative", "logrite.a": a, "logrite.max_iter": max_iter, "logrite.tolerance": tolerance})
    """
    Square root approximated using Newton's method.
    https://en.wikipedia.org/wiki/Newton%27s_method

    >>> all(abs(square_root_iterative(i) - math.sqrt(i)) <= 1e-14 for i in range(500))
    True

    >>> square_root_iterative(-1)
    Traceback (most recent call last):
        ...
    ValueError: math domain error

    >>> square_root_iterative(4)
    2.0

    >>> square_root_iterative(3.2)
    1.788854381999832

    >>> square_root_iterative(140)
    11.832159566199232
    """

    if a < 0:
        raise ValueError("math domain error")

    value = get_initial_point(a)
    logger.error("square_root_iterative(a=%s,max_iter=%s,tolerance=%s): value → %s", a, max_iter, tolerance, value, extra={"event.action": "square_root_iterative", "logrite.a": a, "logrite.max_iter": max_iter, "logrite.tolerance": tolerance})

    for _ in range(max_iter):
        prev_value = value
        value = value - fx(value, a) / fx_derivative(value)
        if abs(prev_value - value) < tolerance:
            return value

    logger.warning("<<< Exiting square_root_iterative(a=%s,max_iter=%s,tolerance=%s)", a, max_iter, tolerance, extra={"event.action": "square_root_iterative", "logrite.a": a, "logrite.max_iter": max_iter, "logrite.tolerance": tolerance})
    return value


if __name__ == "__main__":
    from doctest import testmod

    testmod()
