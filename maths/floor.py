"""
https://en.wikipedia.org/wiki/Floor_and_ceiling_functions
"""
import logging
logger = logging.getLogger(__name__)


def floor(x: float) -> int:
    """
    Return the floor of x as an Integral.
    :param x: the number
    :return: the largest integer <= x.
    >>> import math
    >>> all(floor(n) == math.floor(n) for n
    ...     in (1, -1, 0, -0, 1.1, -1.1, 1.0, -1.0, 1_000_000_000))
    True
    """
    logger.error(">>> Entering floor(x=%s)", x, extra={"event.action": "floor", "logrite.x": x})
    logger.warning("<<< Exiting floor(x=%s)", x, extra={"event.action": "floor", "logrite.x": x})
    return int(x) if x - int(x) >= 0 else int(x) - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
