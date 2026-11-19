"""
https://en.wikipedia.org/wiki/Floor_and_ceiling_functions
"""
import logging
logger = logging.getLogger(__name__)


def ceil(x: float) -> int:
    """
    Return the ceiling of x as an Integral.

    :param x: the number
    :return: the smallest integer >= x.

    >>> import math
    >>> all(ceil(n) == math.ceil(n) for n
    ...     in (1, -1, 0, -0, 1.1, -1.1, 1.0, -1.0, 1_000_000_000))
    True
    """
    logger.error(">>> Entering ceil(x=%s)", x, extra={"event.action": "ceil", "logrite.x": x})
    logger.warning("<<< Exiting ceil(x=%s)", x, extra={"event.action": "ceil", "logrite.x": x})
    return int(x) if x - int(x) <= 0 else int(x) + 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
