"""Uses Pythagoras theorem to calculate the distance between two points in space."""

import math
import logging
logger = logging.getLogger(__name__)


class Point:
    def __init__(self, x, y, z):
        logger.debug(">>> Entering __init__(x=%s,y=%s,z=%s)", x, y, z)
        self.x = x
        logger.debug("__init__(self=%s,x=%s,y=%s,z=%s): self.x → %s", self, x, y, z, self.x)
        self.y = y
        logger.debug("__init__(self=%s,x=%s,y=%s,z=%s): self.y → %s", self, x, y, z, self.y)
        self.z = z
        logger.debug("__init__(self=%s,x=%s,y=%s,z=%s): self.z → %s", self, x, y, z, self.z)
        logger.debug("<<< Exiting __init__(x=%s,y=%s,z=%s)", x, y, z)

    def __repr__(self) -> str:
        logger.debug(">>> Entering __repr__()")
        logger.debug("<<< Exiting __repr__()")
        return f"Point({self.x}, {self.y}, {self.z})"


def distance(a: Point, b: Point) -> float:
    """
    >>> point1 = Point(2, -1, 7)
    >>> point2 = Point(1, -3, 5)
    >>> print(f"Distance from {point1} to {point2} is {distance(point1, point2)}")
    Distance from Point(2, -1, 7) to Point(1, -3, 5) is 3.0
    """
    logger.debug(">>> Entering distance(a=%s,b=%s)", a, b)
    logger.debug("<<< Exiting distance(a=%s,b=%s)", a, b)
    return math.sqrt(abs((b.x - a.x) ** 2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
