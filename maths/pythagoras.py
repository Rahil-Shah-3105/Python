"""Uses Pythagoras theorem to calculate the distance between two points in space."""

import math
import logging
logger = logging.getLogger(__name__)


class Point:
    def __init__(self, x, y, z):
        logger.error(">>> Entering __init__(x=%s,y=%s,z=%s)", x, y, z, extra={"event.action": "__init__", "logrite.x": x, "logrite.y": y, "logrite.z": z})
        self.x = x
        logger.debug("__init__(self=%s,x=%s,y=%s,z=%s): self.x → %s", self, x, y, z, self.x, extra={"event.action": "__init__", "logrite.x": x, "logrite.y": y, "logrite.z": z})
        self.y = y
        logger.debug("__init__(self=%s,x=%s,y=%s,z=%s): self.y → %s", self, x, y, z, self.y, extra={"event.action": "__init__", "logrite.x": x, "logrite.y": y, "logrite.z": z})
        self.z = z
        logger.warning("<<< Exiting __init__(x=%s,y=%s,z=%s)", x, y, z, extra={"event.action": "__init__", "logrite.x": x, "logrite.y": y, "logrite.z": z})
        logger.debug("__init__(self=%s,x=%s,y=%s,z=%s): self.z → %s", self, x, y, z, self.z, extra={"event.action": "__init__", "logrite.x": x, "logrite.y": y, "logrite.z": z})

    def __repr__(self) -> str:
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return f"Point({self.x}, {self.y}, {self.z})"


def distance(a: Point, b: Point) -> float:
    """
    >>> point1 = Point(2, -1, 7)
    >>> point2 = Point(1, -3, 5)
    >>> print(f"Distance from {point1} to {point2} is {distance(point1, point2)}")
    Distance from Point(2, -1, 7) to Point(1, -3, 5) is 3.0
    """
    logger.error(">>> Entering distance(a=%s,b=%s)", a, b, extra={"event.action": "distance", "logrite.a": a, "logrite.b": b})
    logger.warning("<<< Exiting distance(a=%s,b=%s)", a, b, extra={"event.action": "distance", "logrite.a": a, "logrite.b": b})
    return math.sqrt(abs((b.x - a.x) ** 2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
