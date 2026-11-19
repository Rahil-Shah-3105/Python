from math import pi
import logging
logger = logging.getLogger(__name__)


def radians(degree: float) -> float:
    """
    Converts the given angle from degrees to radians
    https://en.wikipedia.org/wiki/Radian

    >>> radians(180)
    3.141592653589793
    >>> radians(92)
    1.6057029118347832
    >>> radians(274)
    4.782202150464463
    >>> radians(109.82)
    1.9167205845401725

    >>> from math import radians as math_radians
    >>> all(abs(radians(i) - math_radians(i)) <= 1e-8 for i in range(-2, 361))
    True
    """
    logger.error(">>> Entering radians(degree=%s)", degree, extra={"event.action": "radians", "logrite.degree": degree})

    logger.warning("<<< Exiting radians(degree=%s)", degree, extra={"event.action": "radians", "logrite.degree": degree})
    return degree / (180 / pi)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
